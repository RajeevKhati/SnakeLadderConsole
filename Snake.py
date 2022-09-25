class Snake:
    def __init__(self, pair):
        self.start = pair.start
        self.end = pair.end
    
    def __str__(self) -> str:
        return f"Snake start:{self.start}, end:{self.end}"