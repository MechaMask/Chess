from abc import ABC, abstractmethod
class Piece(ABC):
    def __init__(self,color,piece_type):
        self.color=color
        self.piece_type = piece_type
    def __str__(self):
        return f"{self.color} {self.piece_type}"
    @abstractmethod
    def display(self):
        pass
    