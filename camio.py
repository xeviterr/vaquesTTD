from vaca import Vaca

class Camio:

    def __init__(self):
        super().__init__()
        self.vaques = []

    def entra(self, vaca:Vaca):
        self.vaques.append(vaca)

    def treu(self, vaca:Vaca):
        self.vaques.remove(vaca)

    def __get_nvaques(self):
        return self.vaques.__len__()

    nVaques = property(__get_nvaques)