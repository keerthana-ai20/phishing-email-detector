# 🛡️ Phishing Email Detection System

## 🚀 Overview

This project is a machine learning-based web application that detects whether an email is **phishing** or **safe** using textual content and URL-based features.

It combines **Natural Language Processing (NLP)** with **feature engineering** and deploys the model using a Flask web interface.

---

## 🎯 Key Features

* ✅ Classifies emails as **Phishing** or **Safe**
* ✅ Trained on real and synthetic email datasets
* ✅ Extracts and analyzes:

  * URLs in email content
  * Suspicious keywords (e.g., *verify, urgent, login*)
  * IP-based links
  * Email length and structure
* ✅ Uses **TF-IDF + custom features**
* ✅ Displays:

  * Model Accuracy
  * Confusion Matrix
  * Classification Report
* ✅ Web interface for real-time predictions

---

## 🧠 Technologies Used

* Python
* Scikit-learn
* Flask
* Pandas & NumPy
* Matplotlib & Seaborn

---

## 📁 Project Structure

```
phishing-detector/
│── phishing_app.py        # Main Flask app + ML model
│── emails.csv            # Dataset (cleaned)
├── static/               # Stores confusion matrix image
└── templates/
    └── index.html        # Web interface
```

---

## ⚙️ Installation

Clone the repository:

```
git clone https://github.com/your-username/phishing-email-detector.git
cd phishing-email-detector
```

Install dependencies:

```
pip install flask pandas scikit-learn numpy matplotlib seaborn
```

---

## ▶️ How to Run

```
python phishing_app.py
```

Open in browser:

```
http://127.0.0.1:5000/
```

---

## 🧪 Example Usage

### 🔴 Phishing Input:

```
Verify your account immediately at http://fake-bank.com
```

### 🟢 Safe Input:

```
Meeting scheduled at 10 AM tomorrow
```

### ✅ Output:

* ⚠️ Phishing Email
* ✅ Safe Email

---

## 📊 Model Details

* Algorithm: Random Forest Classifier
* Text Processing: TF-IDF (unigrams + bigrams)
* Additional Features:

  * URL count
  * Suspicious keyword detection
  * IP address presence
  * Special characters & digits
  * Uppercase ratio

---

## 🎯 Expected Outcome

The model successfully classifies emails as phishing or safe with high accuracy based on textual content and URL features.

---

## ⚠️ Limitations

* Accuracy depends on dataset quality
* May struggle with highly sophisticated phishing emails
* Requires continuous dataset updates for improvement

---

## 🚀 Future Improvements

* 🤖 Deep learning (BERT-based model)
* 📧 Integration with real email systems
* 🌐 Deploy as a live web application
* 🎨 Improved UI/UX dashboard
* 📂 File upload support (.txt / .eml emails)

---

## 👨‍💻 Author
KeerthanaChandran
