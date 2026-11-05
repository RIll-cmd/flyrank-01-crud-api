from fastapi.testclient import TestClient
from app import app

def test_swagger_exposes_task_request_bodies():
    with TestClient(app) as client:
        spec=client.get('/openapi.json').json()
        create=spec['paths']['/tasks']['post']['requestBody']
        update=spec['paths']['/tasks/{task_id}']['put']['requestBody']
        assert create['required'] and update['required']
        assert 'title' in create['content']['application/json']['schema']['properties']
        assert 'done' in update['content']['application/json']['schema']['properties']
