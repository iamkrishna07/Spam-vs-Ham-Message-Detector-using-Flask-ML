from flask import Flask, request
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC

app = Flask(__name__)

# =====================
# LOAD DATA (SAFE)
# =====================
try:
    dataset = pd.read_csv('email_cleaned.csv')
    dataset = dataset.dropna()

    X = dataset['text']
    y = dataset['label']

    vectorizer = TfidfVectorizer(stop_words='english')
    X_vec = vectorizer.fit_transform(X)

    model = LinearSVC()
    model.fit(X_vec, y)

except Exception as e:
    print("Error loading dataset:", e)

    # fallback model (for testing)
    vectorizer = TfidfVectorizer()
    model = LinearSVC()
    model.fit(["test message"], [0])

# =====================
# ROUTE
# =====================
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        message = request.form.get('message', '')

        if message:
            message_vec = vectorizer.transform([message])
            prediction = model.predict(message_vec)[0]

            if str(prediction) == '1':
                return "SPAM"
            else:
                return "HAM"

    # ✅ IMPORTANT: simple response (no template error)
    return "App is running"

# =====================
# RUN APP
# =====================
if __name__ == '__main__':
    app.run(debug=True)
