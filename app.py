# imports
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

app = Flask(__name__)  # FIX: was _name_ (missing double underscores)

# Create chatbot
englishBot = ChatBot(
    "Chatterbot",
    storage_adapter="chatterbot.storage.SQLStorageAdapter"
)

# Train the chatbot on English corpus
trainer = ChatterBotCorpusTrainer(englishBot)
trainer.train("chatterbot.corpus.english")

# Define app routes
@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get")
# Function for the bot response
def get_bot_response():
    userText = request.args.get('msg')
    return str(englishBot.get_response(userText))

if __name__ == "__main__":  # FIX: was _name_ and "_main_"
    app.run(debug=True)