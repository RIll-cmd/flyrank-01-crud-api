from fastapi.testclient import TestClient
from app import app

def test_unknown_task_is_not_reported_as_success():
    with TestClient(app) as client:
        for response in (client.get('/tasks/999'),client.put('/tasks/999',json={'done':True}),client.delete('/tasks/999')):
            assert response.status_code == 404
            assert 'not found' in response.json()['error']
