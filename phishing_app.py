import pandas as pd
import numpy as np
import re
import os
import matplotlib.pyplot as plt
import seaborn as sns

from flask import Flask, request, render_template
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.pipeline import FeatureUnion
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# -----------------------------
# 🔍 Custom Feature Extractor
# -----------------------------
class URLFeatures(BaseEstimator, TransformerMixin):
    def fit(self, x, y=None):
        return self

    def transform(self, texts):
        features = []

        for text in texts:
            url_count = len(re.findall(r'http[s]?://', text))
            suspicious_words = len(re.findall(r'urgent|verify|bank|password|click|login|confirm', text.lower()))
            has_ip = int(bool(re.search(r'\d+\.\d+\.\d+\.\d+', text)))
            length = len(text)

            special_chars = len(re.findall(r'[!@#$%^&*]', text))
            digit_count = len(re.findall(r'\d', text))
            uppercase_ratio = sum(1 for c in text if c.isupper()) / (len(text) + 1)

            features.append([
                url_count,
                suspicious_words,
                has_ip,
                length,
                special_chars,
                digit_count,
                uppercase_ratio
            ])

        return np.array(features)

# -----------------------------
# 🧠 Train Model
# -----------------------------
def train_model():
    df = pd.read_csv("emails.csv")
    df['label'] = df['label'].map({'safe': 0, 'phishing': 1})

    # 🔥 Improved TF-IDF
    tfidf = TfidfVectorizer(
        stop_words='english',
        max_features=10000,
        ngram_range=(1, 2),
        min_df=2,
        max_df=0.9
    )

    features = FeatureUnion([
        ("tfidf", tfidf),
        ("url_features", URLFeatures())
    ])

    X_train, X_test, y_train, y_test = train_test_split(
        df['text'], df['label'], test_size=0.2, random_state=42
    )

    X_train_features = features.fit_transform(X_train)
    X_test_features = features.transform(X_test)

    # 🔥 Tuned RandomForest
    model = RandomForestClassifier(
        n_estimators=300,
        max_depth=20,
        min_samples_split=5,
        min_samples_leaf=2,
        max_features='sqrt',
        class_weight='balanced',
        random_state=42,
        n_jobs=-1
    )

    model.fit(X_train_features, y_train)

    y_pred = model.predict(X_test_features)

    accuracy = accuracy_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)
    report = classification_report(y_test, y_pred)

    # 📊 Save confusion matrix
    if not os.path.exists("static"):
        os.makedirs("static")

    plt.figure()
    sns.heatmap(cm, annot=True, fmt='d')
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.title("Confusion Matrix")
    plt.savefig("static/confusion_matrix.png")
    plt.close()

    return model, features, accuracy, report

model, features, accuracy, report = train_model()

# -----------------------------
# 🌐 Flask App
# -----------------------------
app = Flask(__name__)

@app.route('/')
def home():
    return render_template(
        'index.html',
        accuracy=round(accuracy * 100, 2),
        report=report
    )

@app.route('/predict', methods=['POST'])
def predict():
    email_text = request.form['email']

    transformed = features.transform([email_text])
    prediction = model.predict(transformed)[0]

    result = "⚠️ Phishing Email" if prediction == 1 else "✅ Safe Email"

    return render_template(
        'index.html',
        prediction=result,
        accuracy=round(accuracy * 100, 2),
        report=report
    )

if __name__ == '__main__':
    app.run(debug=True)