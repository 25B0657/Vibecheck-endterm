import { useState } from "react";
import SongCard from "./SongCard";
import "./App.css";

function App() {
  const [text, setText] = useState("");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  async function checkVibe() {
    setLoading(true);
    setError("");
    setResult(null);

    try {
      const response = await fetch("http://localhost:5000/predict", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          text: text,
        }),
      });

      if (!response.ok) {
        const errorData = await response.json();
        throw new Error(errorData.error || "Something went wrong.");
      }

      const data = await response.json();
      setResult(data);
    } catch (error) {
      setError(
        "Unable to connect to the server. Please make sure the Flask backend is running and try again."
      );
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="App">
      <h1>Vibe Check</h1>

      <textarea
        placeholder="Type how you're feeling..."
        value={text}
        onChange={(e) => setText(e.target.value)}
        rows={5}
        cols={40}
      />

      <br />
      <br />

      <button onClick={checkVibe} disabled={loading}>
        {loading ? "Loading... Please wait" : "Check My Vibe"}
      </button>

      {error && (
        <p style={{ color: "red", fontWeight: "bold" }}>
          {error}
        </p>
      )}

      {result && (
        <>
          <div className="result">
            <h2>Detected Emotion: {result.emotion}</h2>

            <p>
              <strong>Confidence:</strong>{" "}
              {(result.confidence * 100).toFixed(2)}%
            </p>

            <h3>Recommended Songs</h3>
          </div>

          <div
            style={{
              display: "flex",
              flexWrap: "wrap",
              gap: "20px",
              justifyContent: "center",
              marginTop: "20px",
            }}
          >
            {result.tracks.map((track, index) => (
              <SongCard
                key={index}
                song={track}
              />
            ))}
          </div>
        </>
      )}
    </div>
  );
}

export default App;