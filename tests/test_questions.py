def test_create_question(client):
    question_data = {"text": "Какая высота Эвереста?"}
    response = client.post("/questions/", json=question_data)
    assert response.status_code == 200, (
        f"Ожидаемый статус 200, но получили {response.status_code}. "
        f"Тело ответа: {response.text}"
    )
    data = response.json()
    assert data["text"] == "Какая высота Эвереста?"
    assert "id" in data
    assert "created_at" in data
