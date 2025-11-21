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


def test_create_question_empty_text(client):
    question_data = {"text": ""}
    response = client.post("/questions/", json=question_data)
    assert response.status_code == 422, (
        f"Ожидаемый статус 422, но получили {response.status_code}. "
        f"Тело ответа: {response.text}"
    )


def test_get_question(client):
    question_data = {"text": "Какая высота Эвереста?"}
    create_response = client.post("/questions/", json=question_data)
    question_id = create_response.json()["id"]
    response = client.get(f"/questions/{question_id}")
    assert response.status_code == 200, (
        f"Ожидаемый статус 200, но получили {response.status_code}"
    )
    data = response.json()
    assert data["id"] == question_id
    assert data["text"] == "Какая высота Эвереста?"


def test_get_different_question_text(client):
    question_data = {"text": "Другой текст вопроса"}
    create_response = client.post("/questions/", json=question_data)
    question_id = create_response.json()["id"]
    response = client.get(f"/questions/{question_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["text"] == "Другой текст вопроса", (
        f"Ожидали 'Другой текст вопроса', но получили '{data['text']}'"
    )


def test_get_all_questions(client):
    question1_data = {"text": "Первый вопрос"}
    question2_data = {"text": "Второй вопрос"}
    client.post("/questions/", json=question1_data)
    client.post("/questions/", json=question2_data)
    response = client.get("/questions/")
    assert response.status_code == 200
    questions = response.json()
    assert len(questions) >= 2
    assert any(q["text"] == "Первый вопрос" for q in questions)
    assert any(q["text"] == "Второй вопрос" for q in questions)
