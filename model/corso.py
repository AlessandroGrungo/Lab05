from dataclasses import dataclass

@dataclass()
class Corso:
    codins: str = ''
    crediti: int = 0
    nome: str = ''
    pd: int = 0
    studenti: set = None
    def __str__(self):
        return f"{self.nome} ({self.codins}), {self.crediti} CFU"

    def __eq__(self, other):
        return self.codins == other.codins

    def __hash__(self):
        return hash(self.codins)