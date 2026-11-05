# Task API

Python and FastAPI provide CRUD endpoints and interactive documentation at `/docs`.

```sh
pip install -r requirements.txt
uvicorn app:app --reload
```

Open http://localhost:8000/docs. If another assignment is already using port 8000, run `uvicorn app:app --port 8004` and open http://localhost:8004/docs instead.

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

Verified against the W2 PDF on 2026-11-05. The complete HTTP transcript is in [verification.txt](verification.txt). A real `curl -i` example from the test server:

```sh
curl -i -X POST http://localhost:8004/tasks -H "Content-Type: application/json" -d '{"title":"Buy milk"}'
```

```http
HTTP/1.1 201 Created
date: Thu, 05 Nov 2026 06:43:09 GMT
server: uvicorn
content-length: 40
content-type: application/json

{"id":4,"title":"Buy milk","done":false}
```

The same CRUD cycle was executed using Swagger's actual Try it out/Execute controls: POST 201, list GET 200, PUT 200, DELETE 204 with no body, then GET 404. The updated Swagger screenshot records the results. After creating another task and restarting the server process, GET returned exactly the three examples and the added task returned 404, confirming in-memory storage.
