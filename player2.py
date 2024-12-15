from a2_partb import GameTree

class PlayerTwo:

    def __init__(self, name = "P2 Bot"):
        self.name = name

    def get_name(self):
        return self.name

    def get_play(self, board, depth = 4):
        tree = GameTree(board, -1, depth)
        (row,col) = tree.get_move()
        return (row,col)