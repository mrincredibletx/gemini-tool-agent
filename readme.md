# 🤖 Gemini Tool Agent

<p align="center">
  <b>An AI-powered web-based chat agent built with Python and Flask.</b>
</p>

<p align="center">
  Ask questions, interact with an AI assistant, and receive responses through a clean and responsive chat interface.
</p>

---

## 📌 About The Project

**Gemini Tool Agent** is a lightweight AI chat application that provides a simple web interface for interacting with an AI backend.

The application uses **Flask** as the backend server and **HTML, CSS, and JavaScript** for the frontend.

Users can enter questions through the chat interface, and the message is sent to the Flask backend using a REST API endpoint. The backend processes the request and returns the AI-generated response without refreshing the page.

---

## ✨ Features

- 🤖 AI-powered chat interface
- 💬 Real-time chat experience
- ⚡ Flask backend
- 🎨 Modern dark-themed UI
- 📱 Responsive design
- ⌨️ Press **Enter** to send messages
- 🚀 Send button for submitting questions
- ⏳ AI response loading animation
- 👤 User and AI message bubbles
- 🔄 Dynamic chat updates without page refresh
- 🔐 Environment variable support for API keys
- 🧩 Easy to extend and customize

---

## 🖥️ Preview

The application provides a simple AI chat interface where users can:

```text
┌─────────────────────────────────────────────┐
│ 🤖 Gemini Tool Agent                        │
│ Ask anything and get an AI-powered response │
├─────────────────────────────────────────────┤
│                                             │
│        ✨ Hello! 👋                         │
│        I'm your AI assistant.               │
│                                             │
│ 👤 What is semantic search?                 │
│                                             │
│ 🤖 Semantic search understands the meaning  │
│    and context of a query...                │
│                                             │
├─────────────────────────────────────────────┤
│ Ask anything...                     [Send]  │
└─────────────────────────────────────────────┘
```

---

## 🛠️ Tech Stack

### Frontend

- HTML5
- CSS3
- JavaScript

### Backend

- Python
- Flask

### AI

- Gemini API / AI Backend

### Development Tools

- Visual Studio Code
- Git
- GitHub

---

## 📁 Project Structure

```text
AI-DOC/
│
├── app.py
│
├── static/
│   └── style.css
│
├── templates/
│   └── index.html
│
├── .gitignore
│
└── README.md
```

---

# 🚀 Getting Started

Follow the steps below to run the project locally.

---

## 1️⃣ Clone the Repository

Clone the project from GitHub:

```bash
git clone https://github.com/YOUR_USERNAME/gemini-tool-agent.git
```

Navigate into the project:

```bash
cd gemini-tool-agent
```

---

## 2️⃣ Create a Virtual Environment

It is recommended to use a virtual environment.

### Windows

```bash
python -m venv .venv
```

Activate the environment:

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv .venv
```

Activate it:

```bash
source .venv/bin/activate
```

---

## 3️⃣ Install Dependencies

Install Flask:

```bash
pip install flask
```

If the project contains a `requirements.txt` file, install all dependencies using:

```bash
pip install -r requirements.txt
```

---

# 🔑 API Configuration

If the application uses an AI API such as Gemini, configure your API key using environment variables.

Create a `.env` file in the project root:

```text
AI-DOC/
│
├── .env
├── app.py
├── static/
├── templates/
└── README.md
```

Add your API key:

```env
GEMINI_API_KEY=your_api_key_here
```

### ⚠️ Important

**Never upload your API key to GitHub.**

Make sure `.env` is included in your `.gitignore` file:

```gitignore
.env
.env.*
.venv/
__pycache__/
*.pyc
```

---

# ▶️ Running the Application

Start the Flask server:

```bash
python app.py
```

You should see something similar to:

```text
 * Running on http://127.0.0.1:5000
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

The Gemini Tool Agent interface should now be available.

---

# 💬 How It Works

The application follows a simple client-server architecture.

```text
                User
                 │
                 ▼
        ┌─────────────────┐
        │   Web Interface │
        │ HTML/CSS/JS     │
        └────────┬────────┘
                 │
                 │ POST /chat
                 ▼
        ┌─────────────────┐
        │ Flask Backend   │
        │     app.py      │
        └────────┬────────┘
                 │
                 ▼
        ┌─────────────────┐
        │   AI Backend    │
        │ Gemini / AI API │
        └────────┬────────┘
                 │
                 ▼
        ┌─────────────────┐
        │ AI Generated    │
        │ Response        │
        └────────┬────────┘
                 │
                 ▼
        ┌─────────────────┐
        │   Chat UI       │
        │ Displays Reply  │
        └─────────────────┘
```

### Request Flow

1. The user enters a question.
2. JavaScript captures the message.
3. JavaScript sends a `POST` request to `/chat`.
4. Flask receives the request.
5. Flask sends the request to the configured AI backend.
6. The AI generates a response.
7. Flask returns the response as JSON.
8. JavaScript displays the response in the chat interface.
9. The page does not need to reload.

---

# 🔌 API Endpoint

## POST `/chat`

The frontend communicates with the Flask backend through this endpoint.

### Request

```json
{
  "message": "What is semantic search?"
}
```

### Response

```json
{
  "reply": "Semantic search understands the meaning and context of a query."
}
```

---

# 🎨 User Interface

The application includes a modern responsive interface with:

### 🤖 AI Header

Displays the application name and AI assistant information.

### 💬 Chat Area

Displays the conversation between the user and AI.

### 👤 User Messages

User messages appear on the right side of the chat.

### 🤖 AI Messages

AI responses appear on the left side.

### ⏳ Loading Animation

A loading animation appears while waiting for the AI response.

### ⌨️ Keyboard Support

Users can press:

```text
Enter
```

to send a message.

### 📱 Responsive Design

The interface adapts to smaller screen sizes such as mobile devices and tablets.

---

# 🔒 Security

For production deployments, follow these security practices:

- Never hard-code API keys.
- Use environment variables for secrets.
- Never commit `.env` files.
- Validate user input.
- Sanitize user-generated content.
- Use HTTPS.
- Add authentication if required.
- Add rate limiting.
- Keep dependencies updated.
- Do not expose sensitive server information.

---

# 🧪 Development

Run the application locally:

```bash
python app.py
```

During development, Flask can be used with debug mode.

After modifying frontend files, refresh the browser:

```text
Ctrl + F5
```

---

# 🐛 Troubleshooting

## Flask is not installed

If you get:

```text
ModuleNotFoundError: No module named 'flask'
```

Run:

```bash
pip install flask
```

Or:

```bash
python -m pip install flask
```

---

## `TemplateNotFound: index.html`

Make sure your project structure is:

```text
AI-DOC/
│
├── app.py
│
└── templates/
    └── index.html
```

The `index.html` file must be inside the `templates` folder.

---

## CSS is not loading

Make sure the structure is:

```text
AI-DOC/
│
├── app.py
│
├── static/
│   └── style.css
│
└── templates/
    └── index.html
```

And your HTML should load the stylesheet using:

```html
<link rel="stylesheet" href="{{ url_for('static', filename='style.css') }}">
```

---

## Port Already in Use

If port `5000` is already being used, stop the existing Flask process or configure another port.

Example:

```python
app.run(port=5001)
```

Then open:

```text
http://127.0.0.1:5001
```

---

# 🚧 Future Improvements

The project can be extended with several features.

- 📄 PDF and document upload
- 📚 Document-based question answering
- 🔎 Semantic search
- 🧠 Conversation memory
- 💾 Chat history
- 👤 User authentication
- 🎙️ Voice input
- 🔊 AI voice responses
- 🌙 Light/Dark theme switcher
- 📊 AI usage analytics
- 🌐 Multi-language support
- 📱 Progressive Web App
- ☁️ Cloud deployment
- 🔗 Multiple AI model support
- 🧩 Tool calling
- 🗂️ File management
- 🔐 Role-based access control

---

# 🌐 Deployment

The application can be deployed to cloud platforms that support Python/Flask applications.

Possible deployment options include:

- Render
- Railway
- PythonAnywhere
- AWS
- Google Cloud
- Microsoft Azure
- DigitalOcean

Before deployment, make sure:

- API keys are stored securely.
- Debug mode is disabled.
- Environment variables are configured.
- Production dependencies are installed.
- HTTPS is enabled.

---

# 🤝 Contributing

Contributions are welcome!

To contribute:

### 1. Fork the repository

Click the **Fork** button on GitHub.

### 2. Clone your fork

```bash
git clone https://github.com/YOUR_USERNAME/gemini-tool-agent.git
```

### 3. Create a branch

```bash
git checkout -b feature/new-feature
```

### 4. Make your changes

Update the project according to your feature or fix.

### 5. Commit your changes

```bash
git add .
git commit -m "Add new feature"
```

### 6. Push your branch

```bash
git push origin feature/new-feature
```

### 7. Create a Pull Request

Open GitHub and create a Pull Request.

---

# 📄 License

This project is currently intended for educational and development purposes.

If you plan to distribute the project publicly, add an appropriate open-source license such as:

- MIT License
- Apache License 2.0
- GNU GPL

---

# 👨‍💻 Author

**Rakesh Bangra**

Computer Science & Engineering Student

Interested in:

- Artificial Intelligence
- Machine Learning
- Software Development
- Web Development
- Hackathons
- Developer Communities

---

# ⭐ Support

If you like this project:

⭐ Star the repository

🍴 Fork the repository

🐛 Report issues

💡 Suggest new features

🤝 Contribute to the project

---

<p align="center">

<b>Built with ❤️ using Python, Flask & AI</b>

</p>
