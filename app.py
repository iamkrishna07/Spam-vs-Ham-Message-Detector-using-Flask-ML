from flask import Flask, render_template, request, redirect, url_for, session
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.model_selection import train_test_split

app = Flask(__name__)
app.secret_key = "spam_detector_secret_key"

# =====================
# LOAD DATA
# =====================
# LOAD DATA
dataset = pd.read_csv('email_cleaned.csv')

dataset = dataset.dropna()

# CHANGE COLUMN NAMES IF NEEDED
X = dataset['text']        # message column
y = dataset['label']      # ham/spam or 0/1

# =====================
# FEATURE EXTRACTION
# =====================
vectorizer = TfidfVectorizer(stop_words='english')
X_vec = vectorizer.fit_transform(X)

# =====================
# TRAIN MODEL
# =====================
X_train, X_test, y_train, y_test = train_test_split(
    X_vec, y, test_size=0.2, random_state=42
)

model = LinearSVC()
model.fit(X_train, y_train)

# =====================
# ROUTE
# =====================
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        message = request.form['message']

        message_vec = vectorizer.transform([message])
        prediction = model.predict(message_vec)[0]

        if prediction == 1:
            result = 'SPAM'
            css_class = 'spam'
        else:
            result = 'HAM'
            css_class = 'ham'

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
