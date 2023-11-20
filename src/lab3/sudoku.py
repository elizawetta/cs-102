import pathlib
import typing as tp
from copy import deepcopy
import random

T = tp.TypeVar("T")


def read_sudoku(path: tp.Union[str, pathlib.Path]) -> tp.List[tp.List[str]]:
    """ Прочитать Судоку из указанного файла """
    path = pathlib.Path(path)
    with path.open() as f:
        puzzle = f.read()
    return create_grid(puzzle)


def create_grid(puzzle: str) -> tp.List[tp.List[str]]:
    digits = [c for c in puzzle if c in "123456789."]
    grid = group(digits, 9)
    return grid


def display(grid: tp.List[tp.List[str]]) -> None:
    """Вывод Судоку """
    width = 2
    line = "+".join(["-" * (width * 3)] * 3)
    for row in range(9):
        print(
            "".join(
                grid[row][col].center(width) + ("|" if str(col) in "25" else "") for col in range(9)
            )
        )
        if str(row) in "25":
            print(line)
    print()


def group(values: tp.List[T], n: int) -> tp.List[tp.List[T]]:
    """
    Сгруппировать значения values в список, состоящий из списков по n элементов
    """
    lst = []
    for i in range(len(values)):
        if i % n == 0:
            lst.append([values[i]])
        else:
            lst[-1].append(values[i])
    return lst

def get_row(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает все значения для номера строки, указанной в pos"""
    return grid[pos[0]]



def get_col(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает все значения для номера столбца, указанного в pos"""
    return [i[pos[1]] for i in grid]


def get_block(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.List[str]:
    """Возвращает все значения из квадрата, в который попадает позиция pos"""
    row = pos[0] // 3 * 3
    col = pos[1] // 3 * 3
    lst = []
    for i in range(row, row + 3):
        for j in range(col, col + 3):
            lst.append(grid[i][j])
    return lst


def find_empty_positions(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.Tuple[int, int]]:
    """Найти первую свободную позицию в пазле"""
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == '.':
                return i, j
    return -1, -1


def find_possible_values(grid: tp.List[tp.List[str]], pos: tp.Tuple[int, int]) -> tp.Set[str]:
    """Вернуть множество возможных значения для указанной позиции"""
    row_values = get_row(grid, pos)
    col_values = get_col(grid, pos)
    block_values = get_block(grid, pos)
    return set('123456789.') - set(row_values+col_values+block_values)


def solve(grid: tp.List[tp.List[str]]) -> tp.Optional[tp.List[tp.List[str]]]:
    """ Решение пазла, заданного в grid """
    empty_pos = find_empty_positions(grid)
    if empty_pos == (-1, -1):
        return grid
    values = find_possible_values(grid, empty_pos)
    for i in values:
        grid1 = deepcopy(grid)
        grid1[empty_pos[0]][empty_pos[1]] = i
        slv = solve(grid1)
        if slv and find_empty_positions(slv) == (-1, -1):
            return slv
    return None




def check_solution(solution: tp.List[tp.List[str]]) -> bool:
    """ Если решение solution верно, то вернуть True, в противном случае False """
    for i in solution:
        if '.' in i:
            return False
        if len(set(i)) != len(i):
            return False

    for i in range(len(solution), 3):
        s = get_col(solution, (0, i))
        if len(set(s)) != len(s):
            return False

    for i in range(len(solution)):
        s = get_block(solution, (0, i))
        if len(set(s)) != len(s):
            return False

    return True

def transposing(grid):
    """ Transposing the whole grid """
    return list(map(list, zip(*grid)))

def swap_row(grid):
    area = random.choice([0, 3, 6])
    a, b = random.choice([[0, 1], [0, 2], [1, 2]])
    grid[area + a], grid[area + b] = grid[area + b], grid[area + a]
    return grid

def swap_rows(grid):
    a, b = random.choice([[0, 3], [0, 6], [3, 6]])
    for i in range(3):
        grid[a+i], grid[b+i] = grid[b+i], grid[a+i]
    return grid


def generate_sudoku(N: int) -> tp.List[tp.List[str]]:
    """Генерация судоку заполненного на N элементов
    >>> grid = generate_sudoku(40)
    >>> sum(1 for row in grid for e in row if e == '.')
    41
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    >>> grid = generate_sudoku(1000)
    >>> sum(1 for row in grid for e in row if e == '.')
    0
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    >>> grid = generate_sudoku(0)
    >>> sum(1 for row in grid for e in row if e == '.')
    81
    >>> solution = solve(grid)
    >>> check_solution(solution)
    True
    """
    grid = [list('123456789')]
    for i in range(2):
        grid.append(grid[-1][6:]+grid[-1][:6])
    for i in range(2):
        grid.append(grid[-3][1:]+grid[-3][:1])
        grid.append(grid[-3][1:]+grid[-3][:1])
        grid.append(grid[-3][1:]+grid[-3][:1])
    functions = [swap_row, swap_rows, transposing]
    for i in range(10):
        f = random.choice(functions)
        grid = f(grid)
    n = max(81-N, 0)
    while n != 0:
        a, b = random.choice(range(9)), random.choice(range(9))
        if grid[a][b] != '.':
            grid[a][b] = '.'
            n -= 1
    return grid


