from flask import Flask, render_template, request, send_from_directory
import cv2
import keras
import numpy as np
from keras.models import load_model

model_1 =load_model("breast_cancer_model.h5")
COUNT = 0
app = Flask(__name__)

app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 1

@app.route("/")

def main():
    return render_template("home.html")

@app.route("/forms")
def forms():
    return render_template("lungh_cancer.html")

@app.route("/About")
def About():
    return render_template("about.html")

@app.route("/terms")
def terms():
    return render_template("terms.html")

@app.route("/privacy")
def privacy():
    return render_template("privacy.html")

@app.route("/Service")
def Service():
    return render_template("service.html")

@app.route("/Contact")
def Contact():
    return render_template("Contact.html")

@app.route("/learn")
def learn():
    return render_template("learn.html")

@app.route("/breast_cancer")
def breast_cancer():
    return render_template("breast_cancer.html")

@app.route("/about")
def about():
    return render_template('about.html')

@app.route('/breast_cancer_detection',methods=['POST'])
def breast_cancer_detection():
    global COUNT
    img = request.files['image']

    img.save('static/{}.jpg'.format(COUNT))    
    img_arr = cv2.imread('static/{}.jpg'.format(COUNT))

    img_arr = cv2.resize(img_arr, (255,255))
    img_arr = img_arr / 255.0
    img_arr = img_arr.reshape(1, 255,255,3)
    prediction = model.predict(img_arr)
    #print(prediction)
    return render_template('prediction.html', data=prediction)
@app.route('/load_img')
def load_img():
    global COUNT
    return send_from_directory('static', "{}.jpg".format(COUNT-1))
if __name__== "__main__":
    app.run(debug=True)