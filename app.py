from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']
    response = get_bot_response(user_message)
    return jsonify({'response': response})

def get_bot_response(message):
    message = message.lower()
    
    if "hello" in message:
        return "Hello! How can I help you today?"
    elif "how are you" in message:
        return "I'm just a bot, but I'm doing great! How about you?"
    elif "evan" in message:
        return "I'm a simple rule-based chatbot."
    elif "bye" in message:
        return "Goodbye! Have a great day!"
    elif "what is your purpose" in message:
        return "My purpose is to assist you with information."
    elif "how old are you" in message:
        return "I don't have an age, as I am just a computer program."
    elif "tell me a joke" in message:
        return "Why don't scientists trust atoms? Because they make up everything!"
    elif "who created you" in message:
        return "I was created by developers at Evan."
    else:
        return "I'm not sure how to respond to that. Can you ask something else?"

if __name__ == '__main__':
    app.run(debug=True)
