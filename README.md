This is the code repository for the text based mood predictor. 
Vibecheck is a text based mood predictor developed to suggest users songs based on the mood deteced from their provided text. 
It support moods like happiness, sadness, anger, love, joy etc. 
Users can enter one or more sentences as text. 
As an output, the algorithm shows the detected mood with the confidence score. 
The better the confidence score accurate the pridicted mood. 

Tech stack : python, flask 2.12.0, hugging face model provided, last.fm, react, vite. 

Setup instructions to run it locally: (Enter the code given below in powercell)

1. Clone the repository:
git clone <your-github-repository-url>
cd Vibecheck-endterm

2. Go to the Vibecheck-backend folder
cd vibecheck-backend

3. create a venv:
python -m venv venv

4. Activate the venv:
venv\Scripts\activate

5. Install all the required packages:
pip install -r requirements.txt

6. Create a Last.fm API account and generate your api key and secrete key. (Copy it to notepad or keep a screenshot of the keys with you for safety)

7. Inside the vibecheck-backend folder create a file named .env   Paste the code given below in the file.
LASTFM_API_KEY=your_api_key
LASTFM_API_SECRET=your_api_secret

8. Start the backend
python app.py
It will give you a link on which your backend will be running. 

Now open a new terminal. You now need to setup your frontend. 

9. Go to the frontend folder
cd vibecheck-frontend

10. Install all the required dependencies:
npm install

11. Start the React application:
npm run dev

