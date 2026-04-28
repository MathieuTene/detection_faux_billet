<div align="center">
  <h1 align="center">📊 Fake Banknote Detection</h1>
  <p align="center">
    <strong>An end-to-end Machine Learning pipeline to identify counterfeit currency.</strong>
  </p>

  <p align="center">
    <a href="https://github.com/MathieuTene/detection_faux_billet/issues"><img src="https://img.shields.io/github/issues/MathieuTene/detection_faux_billet?style=for-the-badge&color=orange" alt="Issues"></a>
    <a href="https://github.com/MathieuTene/detection_faux_billet/network/members"><img src="https://img.shields.io/github/forks/MathieuTene/detection_faux_billet?style=for-the-badge&color=blue" alt="Forks"></a>
  </p>

  <p align="center">
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python" />
    <img src="https://img.shields.io/badge/scikit_learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white" alt="scikit-learn" />
    <img src="https://img.shields.io/badge/pandas-150458?style=for-the-badge&logo=pandas&logoColor=white" alt="pandas" />
    <img src="https://img.shields.io/badge/Dash-008DE4?style=for-the-badge&logo=dash&logoColor=white" alt="Dash" />
  </p>
</div>

<br />

## 📖 About the Project

This project leverages statistical analysis and machine learning to distinguish between genuine and counterfeit banknotes based on geometric dimensions (length, height, margins, etc.).

It covers the entire data science lifecycle: from Exploratory Data Analysis (EDA) and model training to deployment via an interactive **Dash Plotly** web application.

## ✨ Key Features & Methodology

- 🔍 **Exploratory Data Analysis (EDA):** Comprehensive data cleaning and visualization using `Pandas`, `Matplotlib`, and `Seaborn`.
- 🧠 **Machine Learning:** Implementation of classification algorithms using `Scikit-learn` and `Statsmodels` to achieve high detection accuracy.
- 📦 **Model Export:** Serialization of the trained model using `Joblib` for production use.
- 🌐 **Web Dashboard:** An interactive interface built with `Dash` to allow users to input banknote dimensions and receive real-time predictions.

## 🚀 Getting Started

### Installation & Execution

1. **Clone the repository**
   ```bash
   git clone https://github.com/MathieuTene/detection_faux_billet.git
   cd detection_faux_billet
   ```
2. **Install Dependencies**
   It is recommended to use a virtual environment.
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the Dashboard**
   ```bash
   python app.py
   ```
   *Navigate to `http://127.0.0.1:8050/` in your browser.*

## 📈 Repository Stats
<p align="center">
  <img src="https://github-readme-stats.vercel.app/api/pin/?username=MathieuTene&repo=detection_faux_billet&theme=tokyonight" alt="Repository Card" />
</p>
