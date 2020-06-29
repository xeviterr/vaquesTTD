from raca import Raca

class Vaca:

    def __init__(self, nom, pes, raca: Raca):
        super().__init__()
        self.nom = nom
        self.pes = pes
        self.raca = raca

    def getLlet(self):
        return self.pes * self.raca.litresPerKg