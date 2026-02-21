# 🚀 NASA Astronomy Picture of the Day – Streamlit App

This is a simple web app built with Streamlit that fetches and displays NASA’s Astronomy Picture of the Day (APOD) using
the NASA API.

The app displays:

- 🌌 Title of the image
- 🖼 High-resolution image
- 📖 Explanation

---

## 🛰 API Used

This project uses NASA's official APOD API:

https://api.nasa.gov/planetary/apod

You can generate a free API key from:
https://api.nasa.gov/

---

## 📂 Project Structure

space-web-app/
│
├── main.py  
├── get_data.py  
├── .env  
├── requirements.txt  
└── README.md

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/keshavnandwal2003/nasa-astronomy-picture-of-the-day
cd nasa-astronomy-picture-of-the-day
```

### 2️⃣ Create a Virtual Environment (Recommended)

```bash
python -m venv .venv
```

Activate the environment:

Windows:

```bash
.venv\Scripts\activate
```

Mac/Linux:

```bash
source .venv/bin/activate
```

### 3️⃣ Install Dependencies

```bash
pip install streamlit requests python-dotenv
```

Or if using requirements.txt:

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file in the project root directory:

```
API_KEY=your_nasa_api_key_here
```

⚠️ Do NOT commit your `.env` file to GitHub.

Add this line to your `.gitignore` file:

```
.env
```

---

## ▶️ Run the App

```bash
streamlit run main.py
```

The app will open automatically in your browser.

---

## 🧠 How It Works

### main.py

```python
import streamlit as st
from get_data import get_data

data = get_data()
if data:
    st.title(data["title"])
    st.image(data["hdurl"])
    st.write(data["explanation"])
else:
    st.error("Failed to fetch data.")
```

### get_data.py

```python
import requests
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("API_KEY")
url = f"https://api.nasa.gov/planetary/apod?api_key={api_key}"


def get_data():
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

```

---

## 🛠 Dependencies

- streamlit
- requests
- python-dotenv

---

## 🌟 Features

- Uses environment variables for API security
- Clean modular code structure
- Beginner-friendly
- Easy to deploy

---

## 📜 License

This project is for educational purposes.