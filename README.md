# VibeCheck

VibeCheck is a text-based mood predictor that recommends songs based on the user's detected emotion.

The application analyses one or more sentences entered by the user, predicts the emotion using a Hugging Face transformer model, and displays:

- Detected emotion
- Confidence score
- Recommended songs from Last.fm

## Supported emotions

- Joy
- Sadness
- Anger
- Fear
- Love
- Surprise

A higher confidence score indicates that the model is more confident about its prediction.

---

## Tech Stack

- Python
- Flask
- Hugging Face Transformers
- Last.fm API
- React
- Vite

---

# Running the project locally

## 1. Clone the repository

```bash
git clone <your-github-repository-url>
cd Vibecheck-endterm
```

---

## Backend Setup

### 2. Go to the backend folder

```bash
cd vibecheck-backend
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

Windows:

```bash
venv\Scripts\activate
```

macOS/Linux:

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Create a Last.fm account

Generate your own:

- API Key
- API Secret

### 7. Create a `.env` file

Inside the `vibecheck-backend` folder, create a file named:

```
.env
```

Add:

```text
LASTFM_API_KEY=your_api_key
LASTFM_API_SECRET=your_api_secret
```

### 8. Start the backend

```bash
python app.py
```

The backend should run on:

```
http://127.0.0.1:5000
```

---

# Frontend Setup

Open a new terminal.

### 9. Go to the frontend folder

```bash
cd vibecheck-frontend
```

### 10. Update the API URL

Open:

```
src/App.jsx
```

Replace:

```javascript
https://vibecheck-endterm.onrender.com/predict
```

with

```javascript
http://127.0.0.1:5000/predict
```

### 11. Install frontend dependencies

```bash
npm install
```

### 12. Start the frontend

```bash
npm run dev
```

### 13. Open the local website

Open the URL displayed in the terminal (usually `http://localhost:5173`).

You can now enter text into the textbox and receive an emotion prediction along with song recommendations.
