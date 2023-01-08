class Boss:
    def __init__(self, id_: int, name: str, company: str):
        self.id = id_
        self.name = name
        self.company = company
        self._workers = []

    def get_workers(self):
        return self._workers

    def set_workers(self, worker):
        self._workers.append(worker)

class Worker:
    def __init__(self, id_: int, name: str, company: str, boss: Boss):
        self.id = id_
        self.name = name
        self.company = company
        self.boss = boss
        self.add_worker()

    def add_worker(self):
        self.boss.set_workers(self)


boss1 = Boss(1, 'John', 'Tesla')
worker1 = Worker(1, 'Alex', 'Tesla', boss1)
print(worker1.boss.get_workers())