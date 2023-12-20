import unittest

from src.lab4 import film_reco


class RecoTestCase(unittest.TestCase):
    def test_reco(self):
        films = {1: 'Мстители: Финал', 2: 'Хатико', 3: 'Дюна', 4: 'Унесенные призраками'}
        users = [[2, 1, 3], [1, 4, 3], [2, 2, 2, 2, 2, 3]]
        user = film_reco.User([2, 4])
        reco = film_reco.Reco(films, users)
        self.assertEqual(reco.get_one_film(user), 'Дюна')

    def test_user(self):
        user = film_reco.User([2, 4])
        user.add_film(5)
        self.assertEqual(user.films, [2, 4, 5])

    def test_reco2(self):
        films = {1: 'Мстители: Финал', 2: 'Хатико', 3: 'Дюна', 4: 'Унесенные призраками'}
        users = [[2, 1, 3], [1, 4, 3], [2, 2, 2, 2, 2, 3]]
        user = film_reco.User([2, 4])
        reco = film_reco.Reco(films, users)
        self.assertEqual(reco.get_films(user), {1, 3})



