from flask import Flask, jsonify, request
from flask_cors import CORS
import traceback

from Week3 import predict_emotion
from lastfm_fetcher import fetch_tracks

app = Flask(__name__)
CORS(app)

@app.route("/", methods=["GET"])
def health_check():
    return jsonify({"status": "ok"})

@app.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    if not data or "text" not in data:
        return jsonify({
            "error": "Missing 'text' in request body."
        }), 400

    text = data["text"]

    try:
        emotion, confidence = predict_emotion(text)

        tracks = fetch_tracks(emotion)

        return jsonify({
            "emotion": emotion,
            "confidence": confidence,
            "tracks": tracks
        })

    except Exception as e:
        traceback.print_exc()

        return jsonify({
            "error": str(e)
        }), 500

if __name__ == "__main__":
    app.run(debug=True)