# with open('films.txt') as f:
#     f = list(f.readlines())
# with open('films.txt', 'w') as w:
#     for i in range(len(f)):
#         w.write(str(i+1)+','+f[i])
# with open('users.txt', 'w') as w:
#     import random
#     for i in range(100):
#         n = random.randrange(6, 15)
#         us = []
#         for j in range(n):
#             us.append(random.randrange(1, 51))
#         print(*us, sep=',', file=w)
from collections import Counter


class User:
    def __init__(self, films):
        self.films = list(map(int, films.split(',')))
        self.count = len(self.films)

    def add_film(self, film):
        self.films.append(film)
        self.count += 1



class Reco:
    def __init__(self, films_path, users_path):
        with open(films_path) as file:
            self.films = {int(i[0]): i[1] for i in map(lambda x: x.strip().split(','), file.readlines())}
        with open(users_path) as file:
            self.users = list(map(lambda x: list(map(int, x.split(','))), file.readlines()))
        self.count_films = Counter(sum(self.users, []))

    def get_films(self, user: User):
        all_films = []
        for i in self.users:
            lst = [j for j in i if j not in user.films]
            if len(i) - len(lst) >= user.count//2:
                all_films += lst
        return set(all_films)

    def get_one_film(self, user: User):
        lst = self.get_films(user)
        max_raiting = (-1, -1)
        for i in lst:
            if self.count_films[i] > max_raiting[0]:
                max_raiting = (self.count_films[i], i)
        return self.films[max_raiting[1]]


films_path = 'films.txt'
users_path = 'users.txt'
films_id = input()
user = User(films_id)
reco = Reco(films_path, users_path)
print(reco.get_one_film(user))
