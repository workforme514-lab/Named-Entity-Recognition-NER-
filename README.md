# 🔎 Named Entity Recognition (NER)

A simple Named Entity Recognition (NER) application built using **Python, spaCy, FastAPI, and Streamlit**. This project identifies named entities such as people, organizations, locations, dates, and other information from English text.

## ✨ Features

* 🔍 Extract named entities from text.
* 👤 Identify people, organizations, locations, dates, and more.
* ⚡ FastAPI backend for processing text.
* 🖥️ Interactive Streamlit web interface.
* 📊 Display extracted entities in a structured table.
* 📥 Download entity results as a CSV file.
* 📖 Interactive API documentation with Swagger UI.

## 🛠️ Technologies Used

* Python
* spaCy
* FastAPI
* Streamlit
* Pandas
* Requests
* Uvicorn

## 📁 Project Structure

```text
Named Entity Recognition (NER)/
│
├── main.py
├── streamlit_app.py
├── requirements.txt
├── README.md
└── .gitignore
```

## ⚙️ Installation and Setup

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY.git
cd "Named Entity Recognition (NER)"
```

Replace the repository URL with your actual GitHub repository URL.

### 2. Create a Virtual Environment

```bash
python -m venv venv
```

Activate the virtual environment on Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Run the FastAPI Backend

Open a terminal in the project directory and run:

```bash
python -m uvicorn main:app --reload
```

The backend will run at:

* API: http://127.0.0.1:8000
* Swagger documentation: http://127.0.0.1:8000/docs
* Health check: http://127.0.0.1:8000/health

### 5. Run the Streamlit Frontend

Open a second terminal, activate the virtual environment, and run:

```bash
python -m streamlit run streamlit_app.py
```

The Streamlit application will open in your browser.

## 🚀 How to Use

1. Open the Streamlit application.
2. Enter or paste English text into the text area.
3. Click the **Extract Entities** button.
4. View the extracted entities and their labels.
5. Download the results as a CSV file.

## 🔌 API Endpoints

| Method | Endpoint   | Description                      |
| ------ | ---------- | -------------------------------- |
| GET    | `/`        | Check if the API is running      |
| GET    | `/health`  | Check API health                 |
| POST   | `/predict` | Extract named entities from text |

### Example API Request

Send a `POST` request to:

```text
http://127.0.0.1:8000/predict
```

Request body (JSON):

```json
{
  "text": "Ali works at Google in Karachi. He met Sara on Monday."
}
```

### Example Output

The API returns the input text, total number of detected entities, and a list of entities with their labels and character positions.

Possible entities include:

| Entity  | Label  |
| ------- | ------ |
| Ali     | PERSON |
| Google  | ORG    |
| Karachi | GPE    |
| Sara    | PERSON |
| Monday  | DATE   |

*Actual results depend on the text and the spaCy model.*

## 🔄 Project Workflow

```text
User Input
    ↓
Streamlit Interface
    ↓
FastAPI Backend
    ↓
spaCy NLP Model
    ↓
Named Entity Extraction
    ↓
Display Results
    ↓
Download CSV
```

## 📌 Model Information

This project uses spaCy's `en_core_web_sm` English language model to identify named entities.

The model can recognize categories such as:

* **PERSON:** Names of people
* **ORG:** Companies and organizations
* **GPE:** Countries, cities, and other geopolitical entities
* **DATE:** Dates and periods
* **MONEY:** Monetary values
* **EVENT:** Named events

Recognition accuracy depends on the input text and the model's capabilities.

## 🔮 Future Improvements

* Add support for additional languages.
* Improve entity recognition accuracy.
* Add custom entity categories.
* Include automated tests.
* Deploy the application online.

## 👨‍💻 Author

**Your Name**

GitHub: [Your GitHub Profile](https://github.com/YOUR-USERNAME)

## 📄 License

This project is created for educational and learning purposes. Add a license file if you want to specify how others may use, modify, and distribute the project.
