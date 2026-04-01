from app import app

def test_home():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200

def test_prediction():
    client = app.test_client()
    response = client.post('/', data={"message": "Free money"})
    assert response.status_code == 200
