class ConsultantMemory:

    def __init__(self):
        self.memory = {}

    def save(self, key, value):
        self.memory[key] = value

    def get(self, key):
        return self.memory.get(key, "")

    def get_many(self, *keys):
        return {
            key: self.memory.get(key, "")
            for key in keys
        }

    def exists(self, key):
        return key in self.memory

    def clear(self):
        self.memory.clear()

    def show(self):
        return self.memory