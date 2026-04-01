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

SPAM 
│ 
├── app.py                     # Main Flask app 
├── email_cleaned.csv          # Dataset 
├── requirements.txt           # Dependencies 
├── test_app.py                # Test file 
│ 
├── templates/  
         └── index.html        # UI (optional)
|
│ └── .github/ 
          └── workflows/ 
                  └── test.yml # CI/CD pipeline
```
---
 ## ⚙️ Installation & Setup
* 1️⃣ Clone Repository
git clone https://github.com/iamkrishna07/Spam-vs-Ham-Message-Detector-using-Flask-ML.git
cd Spam-vs-Ham-Message-Detector-using-Flask-ML
 * 2️⃣ Install Dependencies
pip install -r requirements.txt
 * 3️⃣ Run Application
python app.py

👉 Open in browser:
http://127.0.0.1:5000/
---
  ##🧪 Testing

Run tests using:

pytest
🔄 CI/CD Pipeline (GitHub Actions)

This project uses GitHub Actions for automatic testing.

What happens on every push?
📥 Code is pulled from repository
📦 Dependencies are installed
🧪 Tests are executed
✅ Result is shown (Pass/Fail)

👉 Workflow file:

.github/workflows/test.yml
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
