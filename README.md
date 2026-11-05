# Task API

Python and FastAPI provide CRUD endpoints and interactive documentation at `/docs`.

```sh
pip install -r requirements.txt
uvicorn app:app --reload
```

| Method | Path | Purpose |
|---|---|---|
| GET | /, /health | API information and health |
| GET | /tasks, /tasks/{id} | List or read |
| POST | /tasks | Create with `{"title":"Buy milk"}` |
| PUT | /tasks/{id} | Update `title` and/or `done` |
| DELETE | /tasks/{id} | Delete |

Missing or invalid input returns 400; unknown task IDs return 404.

Storage is in memory and resets on restart. Run `pip install pytest httpx` and `python -m pytest -q` to check the lifecycle. [Swagger screenshot](swagger.png). The original stage-by-stage commit history remains incomplete.

Example local output:

```text
GET /health 200 {"status":"ok"}
POST /tasks 201 {"id":4,"title":"Buy milk","done":false}
```
