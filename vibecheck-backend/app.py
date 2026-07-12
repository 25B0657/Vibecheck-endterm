from flask import Flask, jsonify, request
from flask_cors import CORS

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
        print("Step 1: Calling predict_emotion()")

        emotion, confidence = predict_emotion(text)

        print("Step 2: Calling fetch_tracks()")

        tracks = fetch_tracks(emotion)

        print("Step 3: Returning response")

        return jsonify({
            "emotion": emotion,
            "confidence": confidence,
            "tracks": tracks
        })

    except Exception as e:
        print("ERROR:", e)

        return jsonify({
            "error": str(e)
        }), 500


if __name__ == "__main__":
    app.run(debug=True)