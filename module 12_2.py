from unittest import TestCase

import unit1
import unittest


class TournamentTest(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.u = unit1.Runner('Усейн', 10)
        self.a = unit1.Runner('Андрей', 9)
        self.n = unit1.Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        for key, value in enumerate(cls.all_results.items(), 1):
            print(f'{key},{value}')

    def test_run(self):
        tour = unit1.Tournament(90, self.u, self.n)
        results = tour.start()
        self.all_results = results
        self.assertTrue(results[max(results.keys())] == 'Ник')

    def test_run1(self):
        tour = unit1.Tournament(90, self.a, self.n)
        results1 = tour.start()
        self.all_results = results1
        self.assertTrue(results1[max(results1.keys())] == 'Ник')

    def test_run2(self):
        tour = unit1.Tournament(90, self.u, self.a, self.n)
        results2 = tour.start()
        self.all_results = results2
        self.assertTrue(results2[max(results2.keys())] == 'Ник')


if __name__ == '__main__':
    unittest.main()
