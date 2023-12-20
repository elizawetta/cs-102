import unittest

from src.lab4 import age_groups


class SudokuTestCase(unittest.TestCase):
    def test_1(self):
        ages = [50]
        peoples = [('Кошельков Захар Брониславович', 105),
                   ('Дьячков Нисон Иринеевич', 88),
                   ('Иванов Варлам Якунович', 88),
                   ('Старостин Ростислав Ермолаевич', 50),
                   ('Ярилова Розалия Трофимовна', 29),
                   ('Соколов Андрей Сергеевич', 15),
                   ('Егоров Алан Петрович', 7)]
        age = age_groups.Groups(peoples, ages)
        lst = [('Кошельков Захар Брониславович', 105),
               ('Дьячков Нисон Иринеевич', 88),
               ('Иванов Варлам Якунович', 88)]
        self.assertEqual(age.create_groups()[1], lst)

    def test_2(self):
        ages = [2, 4, 6, 8]
        peoples = [('Кошельков Захар Брониславович', 105),
                   ('Дьячков Нисон Иринеевич', 88),
                   ('Иванов Варлам Якунович', 88),
                   ('Старостин Ростислав Ермолаевич', 50),
                   ('Ярилова Розалия Трофимовна', 29),
                   ('Соколов Андрей Сергеевич', 15),
                   ('Егоров Алан Петрович', 7)]
        age = age_groups.Groups(peoples, ages)
        self.assertEqual(age.create_groups()[0], [])
        self.assertEqual(age.create_groups()[1], [])
        self.assertEqual(age.create_groups()[2], [])

