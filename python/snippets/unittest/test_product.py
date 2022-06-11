import unittest
from product import Product


class TestProduct(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Ejecucion antes de todas las pruebas
        # Ej: conexion BD (1 sola)
        pass

    @classmethod
    def tearDownClass(cls):
        # Ejecucion despues de todas las pruebas
        # Ej: restablecer/reiniciar objetos del setUpClass
        pass

    def setUp(self) -> None:
        # Ejecucion antes de cada prueba
        self.name = 'apple'
        self.price = 2.50
        self.fruit = Product(self.name, self.price)

    def tearDown(self) -> None:
        # Ejecucion despues de cada prueba
        pass

    def test_product_name(self):
        self.assertEqual(self.fruit.name, self.name)

    def test_product_price(self):
        self.assertEqual(self.fruit.price, self.price)

if __name__ == '__main__':
    unittest.main()
