from transformers import pipeline
from preprocess import preprocess   #Importing the function preprocess from preprocess.py

# Checking the install of transformers
# Qquestion 1
## print("Transformers installed successfully !! ")


# Load Hugging Face Emotion Model
# Question 2
classifier = pipeline(
    "text-classification",
    model="bhadresh-savani/distilbert-base-uncased-emotion"
    )


# Question 3
# Defining the predict_emotion(text) function
def predict_emotion(text):

    # a. preprocess text
    tokens = preprocess(text)

    # b. join tokens
    cleaned_text = " ".join(tokens)

    # c. classify
    result = classifier(cleaned_text)

    # d. extract label and score
    label = result[0]['label']
    score = result[0]['score']

    return label, score


## # Question 4
## # Testing 10 Sentences
##  test_data = [
## 
##     ("I am so happy that I got the job.", "joy"),
##     ("Today has been an amazing day and I feel wonderful.", "joy"),
## 
##     ("I feel lonely and depressed today.", "sadness"),
##     ("I am heartbroken after hearing the bad news.", "sadness"),
## 
##     ("I am furious that nobody listened to me.", "anger"),
##     ("His rude behaviour made me extremely angry.", "anger"),
## 
##     ("I am scared about tomorrow's exam.", "fear"),
##     ("The strange noise at night frightened me.", "fear"),
## 
##     ("I love spending time with my family.", "love"),
##     ("I was shocked when I unexpectedly won the competition.", "surprise")
## ]
## 
## correct = 0
## total = len(test_data)
## 
## print("\nEMOTION CLASSIFICATION RESULTS")
## 
## results_file = open("results.txt", "w")
## 
## for sentence, expected_label in test_data:
## 
##     predicted_label, confidence = predict_emotion(sentence)
## 
## # this is to save the results in the file named result.txt of Question 6
## 
##     results_file.write(f"Sentence: {sentence}\n")
##     results_file.write(f"Expected Emotion: {expected_label}\n")
##     results_file.write(f"Predicted Emotion: {predicted_label}\n")
##     results_file.write(f"Confidence Score: {round(confidence, 4)}\n")
##     results_file.write("-" * 50 + "\n")
## 
## 
## # this is to print the results for viewers
## 
##     print("\nSentence:", sentence)
##     print("Expected Emotion:", expected_label)
##     print("Predicted Emotion:", predicted_label)
##     print("Confidence Score:", round(confidence, 4))
## 
##     if predicted_label.lower() == expected_label.lower():
##         correct += 1
## 
## 
## 
## # Question 5
## # Summary
## print("\nSUMMARY")
## print("Correct Predictions:", correct)
## print("Total Sentences:", total)
## 
## accuracy = (correct / total) * 100
## 
## print("Accuracy:", round(accuracy, 2), "%")
## 
## if correct >= 8:
##     print("The model correctly labelled at least 8 out of 10 sentences.")
## else:
##     print("The model did NOT correctly label at least 8 out of 10 sentences.")