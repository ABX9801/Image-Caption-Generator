from flask import Flask,request
from flask_uploads import UploadSet, configure_uploads, IMAGES
from flask import render_template
from utility import caption

app = Flask(__name__)

photos = UploadSet('photos',IMAGES)
path = 'static/img'
app.config['UPLOADED_PHOTOS_DEST'] = 'static/img'
configure_uploads(app,photos)

@app.route("/",methods=["GET", "POST"])
def homepage():
    return render_template('homepage.html')

@app.route("/upload",methods=["GET","POST"])
def upload():
    description = None
    p=None
    if request.method == "POST" and 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        p = path+'/'+filename
        description = caption(p)
    return render_template('upload.html',cp=description,src = p)

@app.route('/developer',methods=["GET","POST"])
def developer():
    return render_template('dev.html')