from vaca import Vaca
from typing import List

class Camio:

    def __init__(self, pesMaxim=1000):
        super().__init__()
        self.vaques:List[Vaca] = []
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

    @property
    def nVaques(self):
        return self.vaques.__len__()

    @property
    def lletPotencialDeTotesLesVaques(self):
        totalLlet=0
        for vaca in self.vaques:
            totalLlet+=vaca.pes*vaca.raca.litresPerKg
        return totalLlet