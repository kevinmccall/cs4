from itertools import permutations
from collections import Counter
from copy import deepcopy

def generate_board(length):
    return [[] for x in range(length)]

def generate_die_rolls(max_roll):
    return list(range(1, max_roll + 1))

def generate_die_orderings(colors):
    return list(permutations(colors))

def md_list_to_tuple(md_list):
    return tuple(map(tuple, md_list))

def combine_arr(arr1, arr2):
    res = []
    def do_recursion(history, index=0):
        if index >= len(arr1):
            res.append(history)
            return
        for thing in arr2:
            do_recursion(history + [(arr1[index], thing)], index + 1)
            
    do_recursion([])
    return res

def calc_probabilities(board: list[list[str]], die_colors, die_possibilites):
    counts = Counter()
    for c in die_colors:
        counts[c] = 0
    for ordering in generate_die_orderings(die_colors):
        for die_sequence in combine_arr(ordering, die_possibilites):
            b_copy = deepcopy(board)
            for die in die_sequence:
                color, move = die
                update_board(b_copy, color, move)
            counts[md_list_to_tuple(b_copy)] += 1
    return counts

def update_board(board: list[list[str]], color, move):
    for spot_i, spot in enumerate(board):
        for camel_spot, camel in enumerate(spot):
            if camel == color:
                board[spot_i + move].extend(board[spot_i][camel_spot:])
                board[spot_i] = board[spot_i][:camel_spot]
                return



if __name__ == '__main__':
    b = generate_board(15)
    b[0] = ['r', 'g', 'b']
    b[1] = ['y', 'p']
    res = calc_probabilities(b, ['r', 'g', 'b', 'y', 'p'], list(range(1,4)))
    print(f"{res.values()=}")
    print(sum(res.values()))
    print(max(res.values()))