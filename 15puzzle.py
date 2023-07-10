from collections import deque

def create_2d_array(rows, cols, val=None):
    ret = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(val)
        ret.append(row)
    return ret

def flatten_board(board):
    ret = []
    for row in board:
        for val in row:
            ret.append(val)
    return ret

def copy_2d_array(from_arr, to_arr):
    assert len(from_arr) == len(to_arr)
    assert len(from_arr[0]) == len(to_arr[0])
    rows = len(from_arr)
    cols = len(from_arr[0])
    for i in range(rows):
        for j in range(cols):
            to_arr[i][j] = from_arr[i][j]

def is_solvable(board):
    count = 0
    f_board = flatten_board(board)
    for i, val1 in enumerate(f_board):
        for val2 in f_board[i + 1:]:
            if val1 > val2:
                count += 1
    print(count)
    return count % 2 == 0 

class Board:
    def __init__(self, vals) -> None:
        self.rows = len(vals)
        self.cols = len(vals[0])
        self.board = create_2d_array(self.rows, self.cols)
        self.dist = create_2d_array(self.rows, self.cols)
        copy_2d_array(vals, self.board)
        self.hole_pos = self.find_zero()
        self.set_dist()
        assert self.hole_pos is not None
    
    def pos_to_ij(self, val):
        return val // self.cols, val % self.cols
    
    def set_dist(self):
        for i, row in enumerate(self.board):
            for j, val in enumerate(row):
                i2, j2 = self.pos_to_ij(val)
                assert 0 <= i2 < self.rows
                assert 0 <= j2 < self.cols
                idiff = abs(i2 - i)
                jdiff = abs(j2 - j)
                self.dist[i][j] = idiff + jdiff
    
    def calculate_dist(self):
        da_sum = 0
        for row in self.dist:
            for val in row:
                da_sum += val
        return da_sum

    
    def get_tuple_representation(self):
        tuple_holder = []
        for row in self.board:
            tuple_holder.append(tuple(row))
        return tuple(tuple_holder)

    def get_possible_moves(self):
        ret = []
        hi, hj = self.hole_pos
        possible_positions = [
            (hi+1, hj),
            (hi-1, hj),
            (hi, hj+1),
            (hi, hj-1)
        ]
        for i,j in possible_positions:
            if 0 <= i < self.rows and 0 <= j < self.cols:
                ret.append((i,j))
        return ret
    
    def find_zero(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.board[i][j] == self.rows * self.cols - 1:
                    return i, j
        raise Exception("hole not found")
    
    def swap(self, pos1i, pos1j, pos2i, pos2j):
        if (pos1i, pos1j) == self.hole_pos:
            self.hole_pos = pos2i, pos2j
        else:
            self.hole_pos = pos1i, pos1j
        self.board[pos1i][pos1j], self.board[pos2i][pos2j] = self.board[pos2i][pos2j], self.board[pos1i][pos1j]
    

def bfs(start):
    if not is_solvable(start):
        return "no solutions"
    q = deque()
    seen = set()
    q.append(start)
    depth = 0
    while len(q) > 0:
        for _ in range(len(q)):
            tuple_board = q.popleft()
            seen.add(tuple_board)
            board = Board(tuple_board)
            if board.calculate_dist() == 0:
                return depth
            for move in board.get_possible_moves():
                board = Board(tuple_board)
                swapi, swapj = move
                holei, holej = board.hole_pos
                board.swap(swapi, swapj, holei, holej)
                tupl = board.get_tuple_representation()
                if tupl not in seen:
                    q.append(tupl)
        depth += 1
        if depth % 3 == 0:
            print(depth)
    return "no solutions"

# b = ((2,0,1,3),(4,5,6,7), (8,9,10,11), (12,13,14,15))
b = (2,0,1)
# print(bfs(b))