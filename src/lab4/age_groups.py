import sys


class Groups:
    def __init__(self, peoples: list, ages: list):
        self.peoples = peoples
        self.ages = ages

    def create_groups(self):
        groups = [[] for i in range(len(self.ages) + 1)]
        for i in self.peoples:
            for j in range(len(self.ages)):
                if i[1] <= self.ages[j]:
                    groups[j].append(i)
                    break
            else:
                groups[-1].append(i)
        return groups

    def get_names(self, group):
        ans = []
        for i in group:
            ans.append(i[0] + f" ({i[1]})")
        return ', '.join(ans)

    def print_groups(self):
        groups = self.create_groups()
        if groups[-1]:
            print(str(self.ages[-1]+1)+'+:', self.get_names(groups[-1]))
        n = len(self.ages)
        for i in range(n-1, -1, -1):
            if groups[i] and i != 0:
                print(str(self.ages[i-1]+1)+'-'+str(self.ages[i])+':', self.get_names(groups[i]))
            elif groups[i]:
                print('0-'+str(self.ages[i])+':', self.get_names(groups[i]))



ages = list(map(int, sys.argv[1:]))
lst = []
while True:
    s = input()
    if s.lower() == "end":
        break
    s = s.split(',')
    lst.append((s[0], int(s[1])))
age = Groups(lst, ages)
age.print_groups()
