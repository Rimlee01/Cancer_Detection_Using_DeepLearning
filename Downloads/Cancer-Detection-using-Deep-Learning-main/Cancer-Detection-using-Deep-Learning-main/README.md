# Cancer Detection Using Deep Learning (CNN)

This project is a small end-to-end experiment where I use a Convolutional Neural Network (CNN) to help with cancer detection from medical data.  
The main idea is to build a simple but practical pipeline that can:

- Train a deep learning model for cancer classification  
- Save the model  
- Load it in a web app  
- Allow a user to make predictions through a browser interface  

It’s not meant to replace real medical systems, but to show how deep learning can be used in healthcare workflows and to practice the full ML lifecycle: data → model → deployment.

---

## 1. Project Overview

The project is split into two main parts:

1. **Model Development** – done inside the Jupyter notebook `breast_cancer.ipynb`.  
2. **Web Application** – handled by `main.py` using a simple Flask-based interface with HTML/CSS files inside the `static/` and `tamplates/` folders.

The trained model (and preprocessing steps) is stored in `pipe.pkl`, which the web app loads to make predictions.

---

## 2. What the Project Does

- Preprocesses the input data (cleaning, scaling/normalizing, etc.)
- Trains a CNN-based model for binary cancer classification (for example: benign vs malignant)
- Evaluates the model using accuracy and other metrics
- Saves the trained pipeline to a `.pkl` file
- Exposes a minimal web interface where a user can input data and get a model prediction

The main goal was to understand how to move from a notebook experiment to something that feels like a small “tool” instead of just code.

---

## 3. Tech Stack

- **Language:** Python  
- **Deep Learning:** TensorFlow / Keras (for the CNN model)  
- **Data Handling:** NumPy, Pandas  
- **Model Persistence:** `pickle` / `joblib` (saved as `pipe.pkl`)  
- **Web Framework:** Flask  
- **Frontend:** HTML, CSS (inside `tamplates/` and `static/` folders)  
- **Environment:** Jupyter Notebook for experimentation

---

## 4. Project Structure

```text
Cancer-Detection-using-Deep-Learning/
│
├── breast_cancer.ipynb     # Notebook for data exploration, training, and evaluation
├── main.py                 # Flask app for serving predictions through a web interface
├── pipe.pkl                # Saved model / pipeline used by the web app
│
├── static/                 # CSS, images, and other static assets
│   └── ...                 # (styles, images, etc.)
│
└── tamplates/              # HTML templates for the Flask app (index page, result page, etc.)
    └── ...                 # (Jinja2 templates)
