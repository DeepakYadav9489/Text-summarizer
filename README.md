# AI-Powered Text Summarizer

An AI-powered web application that generates concise and meaningful summaries from lengthy text using a fine-tuned pre-trained Transformer model from Hugging Face.

## About the Project

The Text Summarizer is a Natural Language Processing (NLP) application designed to reduce lengthy text into shorter summaries while preserving the main information.

The application uses a pre-trained Transformer model from Hugging Face. The model was fine-tuned and trained for the text summarization task.

Users can enter lengthy text through a simple web interface and receive an automatically generated summary.

## Features

- Accepts lengthy text as input.
- Generates short and meaningful summaries.
- Uses a fine-tuned Transformer model.
- Provides a simple and user-friendly interface.
- Integrates the trained model with a FastAPI backend.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Hugging Face Transformers | Pre-trained Transformer model |
| Deep Learning | Model training and fine-tuning |
| NLP | Text processing and summarization |
| FastAPI | Backend development |
| HTML | Webpage structure |
| CSS | Frontend styling |
| JavaScript | Frontend functionality |

## Installation and Setup

### 1. Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Navigate to the Project Directory

```bash
cd TEXTSUMMARIZERAPP
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

For Windows:

```bash
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

If you do not have a requirements file, install the main packages:

```bash
python -m pip install fastapi uvicorn transformers torch sentencepiece jinja2
```

### 6. Run the Application

```bash
python -m uvicorn app:app --reload
```

### 7. Open in Browser

Visit:

```text
http://127.0.0.1:8000
```

## How It Works

1. The user enters lengthy text into the application.
2. The frontend sends the input text to the FastAPI backend.
3. The backend processes the input and passes it to the fine-tuned Transformer model.
4. The model generates a summary based on the provided text.
5. The generated summary is returned and displayed on the frontend.

## Model Development

- Used a pre-trained Transformer model from Hugging Face.
- Performed fine-tuning for the text summarization task.
- Trained the model using a dialogue summarization dataset.
- Integrated the trained model into the FastAPI application.

## Learning Outcomes

Through this project, I gained practical experience in:

- Natural Language Processing (NLP).
- Working with pre-trained Transformer models.
- Deep Learning and model fine-tuning.
- Text preprocessing and summarization.
- Building APIs using FastAPI.
- Integrating AI models with frontend applications.

## Future Improvements

- Support for larger input documents.
- Improve summary quality and generation speed.
- Add PDF and document upload functionality.
- Improve the user interface.

---

If you find this project useful, feel free to explore the repository and share your feedback.
