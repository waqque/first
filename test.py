import unittest


class TestExample(unittest.TestCase):

    def setUp(self):
        """Подготовка данных перед каждым тестом."""
        pass

    def tearDown(self):
        """Очистка данных после каждого теста."""
        pass

    def test_sample(self):
        """Пример базового теста."""
        self.assertEqual(1 + 1, 2)

    def test_another_sample(self):
        """Еще один пример теста."""
        self.assertTrue(True)


if __name__ == "__main__":
    unittest.main()
