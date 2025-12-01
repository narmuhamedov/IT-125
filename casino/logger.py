class Logger:
    def __init__(self, filename):
        self.filename = filename
    
    def write(self, text:str):
        with open(self.filename, "a", encoding="utf-8") as f:
            f.write(text + '\n')