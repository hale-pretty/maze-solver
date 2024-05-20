class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y
        
    def __repr__(self) -> str:
        return f"Point: ${self.x} ${self.y}"