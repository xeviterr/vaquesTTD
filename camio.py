from vaca import Vaca

class Camio:

    def __init__(self, pesMaxim=1000):
        super().__init__()
        self.vaques = []
        self.pesMaxim = pesMaxim
        self.totalPes = 0

    def entra(self, vaca:Vaca)->bool:
        if (self.totalPes + vaca.pes <= self.pesMaxim):
            self.vaques.append(vaca)
            self.totalPes += vaca.pes
            return True
        else:
            return False

    def treu(self, vaca:Vaca):
        self.vaques.remove(vaca)
        self.totalPes -= vaca.pes

    def __get_nvaques(self):
        return self.vaques.__len__()

    nVaques = property(__get_nvaques)