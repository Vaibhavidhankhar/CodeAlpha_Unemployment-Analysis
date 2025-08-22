# CodeAlpha Unemployment Analysis Web App

[![Python](https://img.shields.io/badge/Python-3.13-blue?logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.3.2-orange?logo=flask)](https://flask.palletsprojects.com/)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-black?logo=github)](https://github.com/Vaibhavidhankhar/CodeAlpha_Unemployment-Analysis.git)
[![Render](https://img.shields.io/badge/Render-Live%20App-brightgreen?logo=render)](https://your-render-link-here)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3.0-lightgrey?logo=scikit-learn)](https://scikit-learn.org/)
[![Pandas](https://img.shields.io/badge/Pandas-2.1.1-lightblue?logo=pandas)](https://pandas.pydata.org/)
[![Joblib](https://img.shields.io/badge/Joblib-1.3.2-blueviolet)](https://joblib.readthedocs.io/)
[![HTML5](https://img.shields.io/badge/HTML5-orange?logo=html5)](https://developer.mozilla.org/en-US/docs/Web/HTML)
[![CSS3](https://img.shields.io/badge/CSS3-blue?logo=css3)](https://developer.mozilla.org/en-US/docs/Web/CSS)
[![JavaScript](https://img.shields.io/badge/JavaScript-yellow?logo=javascript)](https://developer.mozilla.org/en-US/docs/Web/JavaScript)

---

## 🔗 Quick Access Buttons

[![Web App](https://img.shields.io/badge/View%20Web%20App-Render-blue?logo=google-chrome)](https://your-render-link-here)  
[![Project Repo](https://img.shields.io/badge/View%20Project-GitHub-black?logo=github)](https://github.com/Vaibhavidhankhar/CodeAlpha_Unemployment-Analysis.git)  
[![Colab Notebook](https://img.shields.io/badge/View%20Colab-Notebook-orange?logo=googlecolab)](https://colab.research.google.com/your-colab-link-here)  
[![Dashboard URL]([https://your-demo-link-here](https://india-unemployment-analysis-dashboard.onrender.com))

---


## 🚀 Project Overview

**CodeAlpha Unemployment Analysis** is a web-based Python project that analyzes unemployment trends in India using real Kaggle datasets. The app allows interactive exploration of unemployment data, provides visual insights, and can help understand the impact of events like COVID-19 on unemployment rates.

This project includes:
- **Data cleaning and preprocessing**
- **Exploratory data analysis (EDA) with interactive graphs**
- **Predictive modeling (Task 2: Regression and SVM models)**
- **A Flask web app dashboard for live interaction**

---

## 📂 Dataset

The data is sourced from Kaggle:

1. [Unemployment in India](https://www.kaggle.com/datasets/gokulrajkmv/unemployment-in-india?select=Unemployment+in+India.csv)  
2. [Unemployment Rate up to Nov 2020](https://www.kaggle.com/datasets/gokulrajkmv/unemployment-in-india?select=Unemployment_Rate_upto_11_2020.csv)  

We merged these datasets and performed analysis to extract trends, seasonal patterns, and COVID-19 impact.

---

## 🧰 Tools & Libraries

- **Python 3.13**
- **Flask** for web deployment
- **pandas, numpy** for data manipulation
- **scikit-learn** for predictive modeling
- **matplotlib, seaborn, plotly** for visualizations
- **joblib** for saving models

---

## 💻 Features

- Interactive dashboard with unemployment trends by **state and zone**
- Graphical visualization of unemployment patterns over time
- Predictive insights using machine learning models
- Clean and responsive web interface

---

## 📁 Project Structure

```
CodeAlpha_Unemployment-Analysis/
├─ UnemploymentAnalysis_WebApp/
│ ├─ app.py # Flask app main file
│ ├─ templates/ # HTML templates
│ ├─ unemployment_data.pkl # Preprocessed data
│ └─ ... # Other supporting files
├─ requirements.txt # Python dependencies
└─ README.md # Project documentation
```

---

## 🚀 How to Run Locally

1. Clone the repo:

```bash
git clone https://github.com/Vaibhavidhankhar/CodeAlpha_Unemployment-Analysis.git
cd CodeAlpha_Unemployment-Analysis/UnemploymentAnalysis_WebApp
```

2. Create a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

3. Install dependencies:

```bash
pip install -r ../requirements.txt
```

4. Run the app:

```bash
python app.py
Open http://127.0.0.1:5000 in your browser.
```
---

## 🔗 Live Deployment
The app can be deployed on platforms like Render, Heroku, or PythonAnywhere. Configure gunicorn as the web server for production.

---

## 📊 Insights
Visualize unemployment trends by state or zone.
Explore the impact of COVID-19 on unemployment rates.
Identify seasonal and regional patterns.

---

## 📜 License
This project is open-source and available under the MIT License.
📫 Contact
Vaibhavi Dhankhar
GitHub: [](https://github.com/Vaibhavidhankhar/CodeAlpha_Unemployment-Analysis.git)
Email: bhavi7677@gmail.com



