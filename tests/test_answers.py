def test_create_answer(client):
    question_data = {"text": "Тестовый вопрос"}
    question_response = client.post("/questions/", json=question_data)
    question_id = question_response.json()["id"]
    answer_data = {
        "text": "Тестовый ответ",
        "user_id": "550e88d4a734e941c60ada6"
        }
    response = client.post(
        f"/questions/{question_id}/answers/",
        json=answer_data
    )
    assert response.status_code == 200
    data = response.json()
    assert data["text"] == "Тестовый ответ"
    assert data["user_id"] == "550e88d4a734e941c60ada6"
    assert data["question_id"] == question_id
    assert "id" in data
    assert "created_at" in data


def test_create_answer_nonexisting_question(client):
    answer_data = {
        "text": "Тестовый ответ",
        "user_id": "550e88d4a734e941c60ada6"
    }
    response = client.post("/questions/999999/answers/", json=answer_data)
    assert response.status_code == 404


def test_get_answers(client):
    question_data = {"text": "Тестовый вопрос"}
    question_response = client.post("/questions/", json=question_data)
    question_id = question_response.json()["id"]
    answer_data = {
        "text": "Тестовый ответ",
        "user_id": "550e88d4a734e941c60ada6"
        }
    response = client.post(
        f"/questions/{question_id}/answers/",
        json=answer_data
    )
    answer_id = response.json()["id"]
    response = client.get(f"/questions/{question_id}/answers/{answer_id}/")
    assert response.status_code == 200
    data = response.json()
    assert data["text"] == "Тестовый ответ"
    assert data["user_id"] == "550e88d4a734e941c60ada6"
    assert data["question_id"] == question_id


def test_get_nonexisting_answer(client):
    response = client.get("/questions/999999/answers/")
    assert response.status_code == 404


def test_delete_answer(client):
    question_data = {"text": "Тестовый вопрос"}
    question_response = client.post("/questions/", json=question_data)
    question_id = question_response.json()["id"]
    answer_data = {
        "text": "Тестовый ответ",
        "user_id": "550e88d4a734e941c60ada6"
        }
    response = client.post(
        f"/questions/{question_id}/answers/",
        json=answer_data
    )
    answer_id = response.json()["id"]
    delete_response = client.delete(
        f"/questions/{question_id}/answers/{answer_id}/"
    )
    assert delete_response.status_code == 200
    get_response = client.get(f"/questions/{question_id}/answers/{answer_id}/")
    assert get_response.status_code == 404
