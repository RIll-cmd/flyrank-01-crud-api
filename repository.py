class Repository:
    def initialize(self):
        self.tasks = [{"id": i, "title": title, "done": False} for i, title in enumerate(["Learn APIs", "Read a book", "Take a walk"], 1)]
        self.next_id = 4
    def list(self): return self.tasks.copy()
    def get(self, task_id): return next((t for t in self.tasks if t["id"] == task_id), None)
    def create(self, title):
        task = {"id": self.next_id, "title": title, "done": False}; self.next_id += 1; self.tasks.append(task); return task
    def update(self, task_id, changes):
        task = self.get(task_id)
        if task: task.update(changes)
        return task
    def delete(self, task_id):
        task = self.get(task_id)
        if task: self.tasks.remove(task)
        return bool(task)
