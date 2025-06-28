from flask import Flask, request, jsonify, render_template
from duckduckgo_search import DDGS

# Create a Flask web server
app = Flask(__name__)

# Define the logic to get a response using DuckDuckGo search
def get_bot_response(user_message):
    """
    Uses DuckDuckGo search to get a response to the user's message,
    with some basic conversational fallbacks.
    """
    # Convert message to lowercase for keyword matching
    lowered_message = user_message.lower()

    # Basic conversational replies
    if "hello" in lowered_message or "hi" in lowered_message:
        return "Hello! How can I help you today?"
    if "how are you" in lowered_message:
        return "I'm a bot, but I'm running smoothly! What can I look up for you?"
    if "your name" in lowered_message:
        return "I am an AI assistant powered by DuckDuckGo search."
    if "bye" in lowered_message:
        return "Goodbye! Have a great day."

    try:
        # If not a basic greeting, use the DDGS tool to get a response
        with DDGS() as ddgs:
            # We ask for one result and return the body (snippet)
            results = ddgs.text(user_message, max_results=1)
            if results:
                return results[0]['body']
        
        # If no results are found
        return "Sorry, I couldn't find an answer to that. Could you try rephrasing your question?"
    except Exception as e:
        print(f"Error during web search: {e}")
        return "Sorry, I'm having trouble connecting to the internet right now. Please try again later."

# Define the main route to serve the HTML file
@app.route("/")
def index():
    """
    Serves the main HTML page.
    """
    return render_template("index.html")

# Define the chat API route
@app.route("/chat", methods=["POST"])
def chat():
    """
    Handles the chat API requests.
    """
    user_message = request.json.get("message")
    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    bot_response = get_bot_response(user_message)
    return jsonify({"response": bot_response})

# Run the Flask development server
if __name__ == "__main__":
    app.run(debug=True)