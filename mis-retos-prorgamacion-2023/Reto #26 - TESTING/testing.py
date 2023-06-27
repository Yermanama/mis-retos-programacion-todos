import os
import sys
import unittest

ruta = os.path.join('C:', os.sep, 'Users', 'marti', 'OneDrive', 'Escritorio', 'Programación', 'mis-retos-programacion', 'mis-retos-prorgamacion-2023', 'Reto #12 - VIERNES 13')
sys.path.insert(0, ruta)

from yermanama_viernes import es_viernes_13


class TestViernes13(unittest.TestCase):

    def test_viernes_13_existente(self):
        self.assertTrue(es_viernes_13(2023, 1))
        self.assertTrue(es_viernes_13(2022, 5))

    def test_viernes_13_no_existente(self):
        self.assertFalse(es_viernes_13(2023,2))
        self.assertFalse(es_viernes_13(2022, 6))
    
    def test_mes_no_valido(self):
        with self.assertRaises(ValueError):
            es_viernes_13(2023, 13)

if __name__ == "__main__":
    unittest.main()