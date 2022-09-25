class Ladder:
    def __init__(self, pair):
        self.start = pair.start
        self.end = pair.end

    def __str__(self) -> str:
        return f"Ladder start:{self.start}, end:{self.end}"