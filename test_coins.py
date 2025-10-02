import unittest

from functions_coins import find_coins_greedy, find_min_coins

class TestCoinAlgorithms(unittest.TestCase):

    def test_greedy_basic(self):
        self.assertEqual(find_coins_greedy(113), {50: 2, 10: 1, 2: 1, 1: 1})

    def test_dp_basic(self):
        self.assertEqual(find_min_coins(113), {50: 2, 10: 1, 2: 1, 1: 1})

    def test_greedy_zero(self):
        self.assertEqual(find_coins_greedy(0), {})

    def test_dp_zero(self):
        self.assertEqual(find_min_coins(0), {})

    def test_greedy_small(self):
        self.assertEqual(find_coins_greedy(3), {2: 1, 1: 1})

    def test_dp_small(self):
        self.assertEqual(find_min_coins(3), {2: 1, 1: 1})

    def test_greedy_large(self):
        # Тестує жадібний алгоритм на великій сумі (1000).
        # Перевіряє, що сума монет у результаті точно дорівнює 1000.
        # Не перевіряє оптимальність, лише коректність підсумку.

        result = find_coins_greedy(1000)
        total = sum(k * v for k, v in result.items())
        self.assertEqual(total, 1000)

    def test_dp_large(self):
        # Тестує алгоритм динамічного програмування на великій сумі (1000).
        # Перевіряє, що сума монет у результаті точно дорівнює 1000.

        result = find_min_coins(1000)
        total = sum(k * v for k, v in result.items())
        self.assertEqual(total, 1000)

    def test_greedy_vs_dp_equivalence(self):
        # Перевіряє, що жадібний алгоритм і алгоритм динамічного програмування
        # дають однаковий результат для всіх сум від 1 до 199.
        # Якщо обидва алгоритми дають однаковий результат, можна використовувати жадібний — він швидший.

        for amount in range(1, 200):
            self.assertEqual(find_coins_greedy(amount), find_min_coins(amount))

if __name__ == '__main__':
    unittest.main()