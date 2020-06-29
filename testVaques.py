import unittest
from camio import Camio
from vaca import Vaca
from raca import Raca

class TestVaques(unittest.TestCase):

    def test_entraTreuVaques(self):
        c=Camio(300)
        v = Vaca("bonfiassia", 200, Raca("Normanda", 1))
        c.entra(v)
        c.treu(v)
        self.assertTrue(c.nVaques==0)
        c.entra(v)
        self.assertTrue(c.nVaques==1)

    def test_noEsPermetenMesVaquesSiSuperaPes(self):
        c=Camio(200)
        v = Vaca("Bonfiassia", 100, Raca("Normanda", 1))
        c.entra(v)
        v = Vaca("Maria", 100, Raca("Normanda", 1))
        c.entra(v)
        v = Vaca("Joana", 1, Raca("Normanda", 1))
        c.entra(v)
        self.assertTrue(c.nVaques == 2, "Error incorrecte en pes maxim camió")
        


if __name__ == '__main__':
    unittest.main()