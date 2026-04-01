from flask import Flask, render_template, request, redirect, url_for, session
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC

app = Flask(__name__)
app.secret_key = "spam_detector_secret_key"

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

    # fallback (for testing)
    vectorizer = TfidfVectorizer()
    model = LinearSVC()

    # dummy training (so app doesn't crash)
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
                result = 'SPAM'
                css_class = 'spam'
            else:
                result = 'HAM'
                css_class = 'ham'
        else:
            result = "No message entered"
            css_class = ""

        session['message'] = message
        session['result'] = result
        session['css_class'] = css_class

        return redirect(url_for('home'))

    message = session.pop('message', '')
    result = session.pop('result', None)
    css_class = session.pop('css_class', '')

    return render_template(
        'index.html',
        message=message,
        result=result,
        css_class=css_class
    )


# =====================
# RUN APP
# =====================
if __name__ == '__main__':
    app.run(debug=True)