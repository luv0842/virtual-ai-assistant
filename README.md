# 🤖 AI Irika – AI-Powered Chatbot

**AI Irika** is a locally running AI chatbot built using Python, Flask, TinyLlama, and MongoDB. It provides an interactive web-based chat interface where users can ask questions and receive AI-generated responses.

The application uses **Ollama** to run the TinyLlama language model locally and MongoDB to store conversation history.

## 🚀 Features

- **AI-Powered Conversations:** Generates responses using the TinyLlama LLM.
- **Local AI Processing:** Runs the AI model locally through Ollama.
- **Interactive Chat Interface:** Clean and responsive chatbot UI.
- **Chat History Storage:** Saves user messages and AI responses in MongoDB.
- **Flask Backend:** Handles user requests and AI communication.
- **Error Handling:** Handles connection errors, request timeouts, and unexpected errors.
- **Automatic Scrolling:** Automatically scrolls to the latest conversation.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Flask | Web framework |
| HTML5 | Webpage structure |
| CSS3 | User interface styling |
| JavaScript | Chat interface behavior |
| MongoDB | Chat history database |
| PyMongo | MongoDB connectivity |
| Ollama | Local AI model execution |
| TinyLlama | Large Language Model |
| Requests | API communication |

## 📂 Project Structure

```text
AI-Irika/
│
├── app.py                 # Flask backend
├── index.html             # Chatbot frontend
│
└── README.md              # Project documentation
```

**Note:** Flask's `render_template()` expects the HTML file inside a `templates` folder. Organize the project as follows before running:

```text
AI-Irika/
│
├── app.py
├── templates/
│   └── index.html
└── README.md
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd AI-Irika
```

### 2. Install Required Libraries

```bash
pip install flask pymongo requests
```

### 3. Install and Start MongoDB

Install MongoDB Community Server and ensure that the MongoDB service is running.

The application connects to:

```text
mongodb://localhost:27017/
```

### 4. Install Ollama

Download Ollama from:

https://ollama.com/

Pull the TinyLlama model:

```bash
ollama pull tinyllama
```

Make sure Ollama is running and accessible at:

```text
http://localhost:11434
```

### 5. Run the Application

```bash
python app.py
```

### 6. Open in Browser

Visit:

```text
http://127.0.0.1:5000/
```

Start chatting with AI Irika!

## 🗄️ Database Structure

The application uses MongoDB.

**Database:** `ai_assistant`

**Collection:** `chat_history`

Each conversation is stored with the following fields:

| Field | Description |
|---|---|
| user_message | Message entered by the user |
| bot_reply | AI-generated response |
| time | Date and time of conversation |

## 🔄 How It Works

1. User enters a message through the chatbot interface.
2. Flask receives the message using a POST request.
3. The backend sends the prompt to Ollama.
4. TinyLlama processes the prompt and generates a response.
5. The response is displayed on the webpage.
6. User messages and AI responses are saved in MongoDB.

## 🔮 Future Enhancements

- User authentication and login system.
- Multiple chat sessions.
- Delete and manage chat history.
- Voice input and text-to-speech functionality.
- Improved UI with dark mode.
- Support for multiple AI models.
- Deploy the application online.
- Streaming AI responses in real time.

## 👨‍💻 Author

**Luv Goswami**

Project: AI Irika – AI Chatbot

## 📜 License

This project is developed for educational and learning purposes. You are welcome to modify and improve it.
