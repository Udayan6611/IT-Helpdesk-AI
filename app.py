from flask import Flask, render_template, request
from transformers import pipeline

app = Flask(__name__)

# Load the AI model (this happens once when the server starts)
print("Loading AI Model... This might take a minute...")
classifier = pipeline("zero-shot-classification", model="typeform/distilbert-base-uncased-mnli")
print("Model Loaded Successfully!")

# The categories we want the AI to choose from
TICKET_CATEGORIES = ["Hardware Issue", "Networking and Internet", "Software and Access", "Account Password Reset"]

@app.route("/")
def home():
    return render_template("index.html")

# This route catches the data when the user clicks "Submit"
@app.route("/submit", methods=["POST"])
def submit_ticket():
    # 1. Grab the text the user typed in the form
    user_complaint = request.form.get("complaint")
    
    # 2. Feed the text to the AI and ask it to categorize it
    ai_result = classifier(user_complaint, TICKET_CATEGORIES)
    
    # 3. Extract the top prediction category from the AI
    predicted_category = ai_result['labels'][0]
    
    # 4. Send the result to a new webpage to show the user
    return render_template("result.html", complaint=user_complaint, category=predicted_category)

if __name__ == "__main__":
    app.run(debug=True)