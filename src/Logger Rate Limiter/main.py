class Logger:
    def __init__(self):
        self.messages = {}

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if self.messages.get(message) is not None and self.messages[message] > timestamp - 10: return False
        self.messages[message] = timestamp
        return True
