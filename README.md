
# AI Chatbot with Web Search

## This project is a simple, yet powerful AI chatbot application built with a Python backend and a modern HTML/CSS/JavaScript frontend. The chatbot uses the DuckDuckGo Search API to provide intelligent, real-time responses to a wide range of user queries, going far beyond simple, hard-coded replies.

![Screenshot 2025-06-28 231622](https://github.com/user-attachments/assets/e2465e60-3eda-4cb4-9c8a-3b8d267f3174)


## Features

- **Intelligent Responses:** Utilizes the DuckDuckGo Search API to answer questions about current events, facts, and general knowledge.
- **Modern UI:** A clean, visually appealing chat interface with a gradient background, animated chat bubbles, and a typing indicator.
- **Responsive Design:** The interface is fully responsive and works well on both desktop and mobile browsers.
- **Separated Concerns:** The project follows best practices by keeping the Python backend, HTML structure, and CSS styling in separate files.

## Tech Stack

- **Backend:** Python, Flask
- **Frontend:** HTML, Tailwind CSS, JavaScript
- **Web Search:** `duckduckgo-search` Python library

## Project Structure

```
/
|-- app.py             # The main Flask application
|-- static/
|   `-- style.css      # All custom CSS rules
|-- templates/
|   `-- index.html     # The main HTML file for the chat interface
`-- README.md          # This file
```

## Setup and Installation

Follow these steps to get the project running on your local machine.

**1. Clone the repository (or download the files):**

If this were a Git repository, you would clone it. Since you have the files, ensure they are in the correct structure as shown above.

**2. Install the required Python libraries:**

Open your terminal or command prompt and navigate to the project directory. Then, install Flask and the DuckDuckGo Search library using pip:

```bash
pip install Flask duckduckgo-search
```

## How to Run the Application

With the dependencies installed, you can start the Flask server by running the following command in your terminal:

```bash
python app.py
```

The server will start, and you will see output indicating that it is running (usually on `http://127.0.0.1:5000`).

## How to Use

1.  Open your web browser and navigate to `http://127.0.0.1:5000`.
2.  The chat interface will load.
3.  Type a message in the input box at the bottom and press **Enter** or click the **Send** button.
4.  The chatbot will respond with an answer based on its web search capabilities.

#
