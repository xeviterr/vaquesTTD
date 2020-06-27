import unittest
from camio import Camio
from vaca import Vaca
from raca import Raca

class TestVaques(unittest.TestCase):

    def test_entraTreuVaques(self):
        c=Camio()
        v = Vaca("bonfiassia", 200, Raca("Normanda", 1))
        c.entra(v)
        c.treu(v)
        self.assertTrue(c.nVaques==0)
        c.entra(v)
        self.assertTrue(c.nVaques==1)

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()