# In the 5 by 5 matrix below, the minimal path sum
# from the top left to the bottom right,
# by only moving to the right and down,
# is indicated in bold red and is equal to 2427.
#
# 131 673 234 103 18
# 201 96 342 965 150
# 630 803 746 422 111
# 537 699 497 121 956
# 805 732 524 37 331
#
# Find the minimal path sum from the top left to the bottom right
# by only moving right and down in matrix.txt
# (right click and "Save Link/Target As..."),
# a 31K text file containing an 80 by 80 matrix.

import numpy as np


class BinaryTree:
    def __init__(self, pos: tuple = None, cost: int = None):
        self.position = pos
        self.cost = cost
        self.right_child = None
        self.down_child = None
        self.parent = None
    
    def get_right_child(self):
        return self.right_child

    def get_down_child(self):
        return self.down_child

    def get_parent(self):
        return self.parent
    
    def set_parent(self, tree):
        self.parent = tree

    def get_pos(self):
        return self.position

    def set_pos(self, pos):
        self.position = pos

    def get_cost(self):
        return self.cost

    def set_cost(self, cost):
        self.cost = cost
    
    def insert_right(self, pos, cost):
        if self.right_child == None:
            self.right_child = BinaryTree(pos, cost)
            self.right_child.parent = self
        else:
            t = BinaryTree(pos, cost)
            t.right_child = self.right_child
            if self.down_child != None:
                t.down_child = self.down_child
                t.down_child.parent = t
            self.right_child = t
            t.parent = self
            t.right_child.parent = t

    def insert_down(self, pos, cost):
        if self.down_child == None:
            self.down_child = BinaryTree(pos, cost)
            self.down_child.parent = self
        else:
            t = BinaryTree(pos, cost)
            t.down_child = self.down_child
            if self.right_child != None:
                t.right_child = self.right_child
                t.right_child.parent = t
            self.down_child = t
            t.parent = self
            t.down_child.parent = t
    
    def remove_right_child(self):
        self.right_child = None
    
    def remove_down_child(self):
        self.down_child = None
            
        
    def node_to_string(self):
        return "Pos: " + str(self.position) + " Cost: " + str(self.cost)

    def to_string(self, came_from=None):
        if came_from == None:
            res = " + " + self.node_to_string() + "\n"
        elif came_from == "Up":
            res = " v " + self.node_to_string() + "\n"
        elif came_from == "Left":
            res = " > " + self.node_to_string() + "\n"
        if self.down_child != None:
            res += self.down_child.to_string(came_from="Up")
        if self.right_child != None:
            res += self.right_child.to_string(came_from="Left")
        return res
        

def read_matrix(filename):
    return np.loadtxt(filename, dtype=int, delimiter=',')


def min_path_dp_recursive(matrix):
    """
    Find the minimal path sum from the top left to the bottom right
    by only moving right and down in the matrix
    """
    dynamic_programing_matrix = matrix.copy()
    ln = len(dynamic_programing_matrix)
    lm = len(dynamic_programing_matrix[0])
    for i in range(ln):
        for j in range(lm):
            if i > 0 and j > 0:
                dynamic_programing_matrix[i][j] += min(
                        dynamic_programing_matrix[i][j-1],
                        dynamic_programing_matrix[i-1][j]
                    )
            elif i > 0:
                dynamic_programing_matrix[i][j] += dynamic_programing_matrix[i-1][j]
            elif j > 0:
                dynamic_programing_matrix[i][j] += dynamic_programing_matrix[i][j-1]
    return dynamic_programing_matrix[-1][-1]


def main():
    example_matrix = np.array(
        [
            [131, 673, 234, 103,  18],
            [201,  96, 342, 965, 150],
            [630, 803, 746, 422, 111],
            [537, 699, 497, 121, 956],
            [805, 732, 524,  37, 331]
        ]
    )
    
    min_path_sum = min_path_dp_recursive(example_matrix)
    print("Example min_path_sum", min_path_sum)
    matrix = read_matrix('p081_matrix.txt')
    min_path_sum = min_path_dp_recursive(matrix)
    print("p081_matrix min_path_sum", min_path_sum)

main()
