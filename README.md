# Spam vs Ham Message Detector using Flask & ML

A Machine Learning web application that classifies text messages as **Spam** or **Ham (Not Spam)** using **TF-IDF** and **Linear SVM**, built with Flask.

---

## 🚀 Features

* Spam vs Ham message detection
* Simple and clean web interface
* Real-time prediction
* Machine learning based classification
* Easy to run locally

---

## 🧠 Tech Stack

* Python
* Flask
* Scikit-learn
* Pandas
* HTML / CSS
* Machine Learning (TF-IDF + LinearSVC)

---

## 📁 Project Structure

```
spam-ham-detector
│
├── app.py
├── email_cleaned.csv
│
├── templates
│     └── index.html
│
└── static (optional)
```

---

## 📊 Machine Learning Model

* Feature Extraction: TF-IDF Vectorizer
* Algorithm: Linear Support Vector Classifier (LinearSVC)
* Train/Test Split: 80/20
* Text preprocessing using stop words removal

---

## 🖥️ Example

**Input**

```
Congratulations! You won a free lottery ticket
```

**Output**

```
SPAM
```
