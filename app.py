import os
import pickle
from flask import Flask, jsonify, request

app = Flask(__name__)
current_dir = os.getcwd()


# model = pickle.load(
#     open("I:\\Desktop\\ML\\nlp\\slang_detector_model\\artefacts\\rf_model.pkl", "rb"))


# vec = pickle.load(open(
#     "I:\\Desktop\\ML\\nlp\\slang_detector_model\\artefacts\\count_vectorizer.pkl", "rb"))


model = pickle.load(
    open(os.path.join(current_dir, "artefacts", "rf_model.pkl"), "rb"))


vec = pickle.load(
    open(os.path.join(current_dir, "artefacts", "count_vectorizer.pkl"), "rb"))


@app.get('/')
def index():
    return jsonify({"resp": "OK", "status": 200})


@app.post('/predict')
def predict():
    body = request.json
    comment = body["comment"]

    vectorized_comment = vec.transform([comment])
    pred = model.predict(vectorized_comment)

    return jsonify({"isToxic": bool(pred[0])})


app.run(host="0.0.0.0", port=8000)
