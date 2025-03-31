class Session:
    def __init__(self):
        self.data = {}

    def set(self, key, value):
        """Store a value in the session."""
        self.data[key] = value

    def get(self, key, default=None):
        """Retrieve a value from the session."""
        return self.data.get(key, default)
    
    def clear(self):
        self.data.clear()
