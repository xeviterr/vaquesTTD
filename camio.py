from vaca import Vaca

class Camio:

    def __init__(self, pes=1000):
        super().__init__()
        self.vaques = []
        self.totalPes = 0

    def entra(self, vaca:Vaca):
        self.vaques.append(vaca)
        self.totalPes += vaca.pes

    def treu(self, vaca:Vaca):
        self.vaques.remove(vaca)
        self.totalPes -= vaca.pes

    def __get_nvaques(self):
        return self.vaques.__len__()

    nVaques = property(__get_nvaques)