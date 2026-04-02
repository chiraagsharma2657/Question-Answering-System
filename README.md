# Question Answering System

A Flask-based web application that answers questions from a given text passage or uploaded PDF document using Natural Language Processing (NLP). The system uses a fine-tuned BERT model and a custom inference pipeline to extract accurate answers directly from the provided text.

## Features

- **PDF Upload** - Upload a PDF file and automatically extract its text content
- **Two QA Models** - Choose between a fine-tuned BERT model and a custom inference pipeline
- **Web Interface** - Simple and interactive UI for entering passages and asking questions
- **REST API** - JSON-based API endpoints for programmatic access

## Tech Stack

- **Backend:** Python, Flask
- **NLP Model:** BERT (bert-large-uncased-whole-word-masking-finetuned-squad)
- **PDF Processing:** PyPDF2
- **Frontend:** HTML, CSS, JavaScript

## Step-by-Step Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/chiraagsharma2657/Question-Answering-System.git
cd Question-Answering-System
```

### Step 2: Create a Virtual Environment (Recommended)

```bash
python -m venv venv
```

Activate the virtual environment:

- **Windows:**
  ```bash
  venv\Scripts\activate
  ```
- **macOS/Linux:**
  ```bash
  source venv/bin/activate
  ```

### Step 3: Install Flask

```bash
pip install flask
```

### Step 4: Install Required Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- `pytorch-transformers` - For running the BERT model
- `Flask` - Web framework
- `Flask-Cors` - Cross-origin request handling

### Step 5: Download and Set Up the BERT Model

- Download the pre-trained BERT model (`bert-large-uncased-whole-word-masking-finetuned-squad`)
- Unzip the model files
- Place them inside a `model` folder in the project root directory

### Step 6: Create the Uploads Folder

Create a folder named `uploads` in the project root to store uploaded PDF files:

```bash
mkdir uploads
```

### Step 7: Run the Application

```bash
python app.py
```

The application will start on `http://127.0.0.1:5000`.

### Step 8: Open in Browser

Open your browser and go to `http://127.0.0.1:5000` to start using the application.

## How to Use

1. **Enter a passage** manually in the text box or **upload a PDF** file
2. **Type your question** about the passage
3. **Select a model** (BERT or custom inference) to get the answer
4. The system will extract and display the most relevant answer from the given text

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Home page |
| `/upload` | POST | Upload a PDF file |
| `/model1` | POST | Get answer using BERT model |
| `/model2` | POST | Get answer using custom model |
| `/predict` | POST | JSON API for BERT model |
| `/predict2` | POST | JSON API for custom model |

## Project Structure

```
Question-Answering-System/
├── app.py                 # Main Flask application
├── bert.py                # BERT model wrapper
├── utils.py               # Utility functions
├── requirements.txt       # Python dependencies
├── Code/                  # Custom inference pipeline
├── static/                # CSS, JavaScript, images
├── templates/             # HTML templates
├── model/                 # BERT model files (to be added)
└── uploads/               # Uploaded PDF files (to be created)
```
