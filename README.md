# Rule-Based Chatbot

This is a simple rule-based chatbot built with Flask. It responds to predefined keywords and phrases with specific responses. This chatbot serves as a basic example of how to create and deploy a chatbot using Flask.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Introduction

This project demonstrates how to create a rule-based chatbot using Flask. The chatbot responds to user input based on predefined rules and can handle a variety of simple queries.

## Features

- Responds to greetings and common queries
- Provides information about its purpose and creator
- Tells a simple joke
- Easy to extend with new rules

## Installation

### Prerequisites

Make sure you have Python 3.7 or higher installed on your system.

### Steps

1. **Clone the repository:**

   ```sh
   git clone https://github.com/shahram8708/rule-based-chatbot.git
   cd rule-based-chatbot
   ```

2. **Create a virtual environment:**

   ```sh
   python -m venv venv
   ```

3. **Activate the virtual environment:**

   - On Windows:

     ```sh
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```sh
     source venv/bin/activate
     ```

4. **Install the required dependencies:**

   ```sh
   pip install -r requirements.txt
   ```

## Usage

1. **Run the Flask application:**

   ```sh
   python app.py
   ```

2. **Open your web browser and navigate to:**

   ```
   http://127.0.0.1:5000/
   ```

3. **Interact with the chatbot** by typing messages into the input field and clicking "Send".

### Adding New Rules

To add new rules, modify the `get_bot_response` function in `app.py`. Add new `elif` blocks to handle additional queries.

```python
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
```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
