from fastapi.testclient import TestClient
from app import app

def test_invalid_task_payloads_return_400():
    with TestClient(app) as client:
        for payload in ({}, {'title':'  '}, {'title':123}, {'title':'ok','done':'yes'}, {'unexpected':1}):
            assert client.post('/tasks',json=payload).status_code == 400
        assert client.put('/tasks/1',json={}).status_code == 400
        assert client.put('/tasks/1',json={'done':'yes'}).status_code == 400
