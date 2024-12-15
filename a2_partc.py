# Main Author: Ayush Patel, Archi Kakadiya
# Main Reviewer: Mohdeep Singh

from a1_partc import Queue
from a1_partd import overflow

WINNING_SCORE = 1000000
LOSING_SCORE = -1000000
WINNING_THRESHOLD = 999999
LOSING_THRESHOLD = -999999
PLAYER_ONE = 1
PLAYER_TWO = -1
ALPHA = float('-inf')
BETA = float('inf')

# This function duplicates and returns the board. You may find this useful
def copy_board(board):
        current_board = []
        height = len(board)
        for i in range(height):
            current_board.append(board[i].copy())
        return current_board


# this function is your evaluation function for the board
def evaluate_board (board, player):
    playerScore = 0
    opponentScore = 0

    for row in board:
        for cell in row:
            if (player == PLAYER_ONE and cell > 0) or (player == PLAYER_TWO and cell < 0):
                playerScore += abs(cell)
            else:
                opponentScore += abs(cell)

    if playerScore > 0 and opponentScore == 0:
        return WINNING_SCORE
    elif playerScore == 0 and opponentScore > 0:
        return LOSING_SCORE
    return playerScore - opponentScore

class GameTree:
    class Node:
        def __init__(self, board, depth, player, tree_height = 4):
            self.board = copy_board(board)
            self.depth = depth
            self.player = player
            self.height = tree_height
            self.children = []
            self.score = None
            self.parent = None
            self.previous_move = None
        
        def set_score(self, score):
            self.score = score

        def get_children(self):
            return self.children
        
        def get_parent(self):
            return self.parent
        
        def is_game_won(self):
            score = evaluate_board(self.board, self.player)
            return score > WINNING_THRESHOLD or score < LOSING_THRESHOLD
        
        def add_child(self, node):
            self.children.append(node)
            node.parent = self

        def is_max_height(self):
            return self.depth >= self.height - 1

    def __init__(self, board, player, tree_height = 4):
        self.player = player
        self.board = copy_board(board)
        # you will need to implement the creation of the game tree here.  After this function completes,
        # a full game tree will be created.
        # hint: as with many tree structures, you will need to define a self.root that points to the root
        # of the game tree.  To create the tree itself, a recursive function will likely be the easiest as you will
        # need to apply the minimax algorithm to its creation.
        self.root = self.Node(self.board, 0, self.player, tree_height)
        self.height = tree_height
        self.build_tree(self.root)

    def build_tree(self, node : Node):
        if node.is_max_height() or node.is_game_won():
            score = evaluate_board(node.board, node.player) * node.player
            node.set_score(score)
        else:
            moves = get_possible_moves(node.board, node.player)

            for move in moves:
                board = copy_board(node.board)
                board[move[0]][move[1]] += node.player
                queue = Queue()

                overflow(board, queue)

                new_node = self.Node(board, node.depth + 1, -node.player, self.height - 1)
                new_node.previous_move = move
                node.add_child(new_node)
                self.build_tree(new_node)

    
    def minimax(self, node, player, alpha = ALPHA, beta = BETA):
        best_score = alpha if player else beta
        best_child_move = None

        if node.is_max_height() or node.is_game_won():
            return node, node.score

        if player:
            for child in node.get_children():
                _, child_score = self.minimax(child, not player, alpha, beta)
                if(child_score > best_score):
                    best_score = max(best_score, child_score)
                    best_child_move = child
                alpha = max(alpha, child_score)
                if beta <= alpha:
                    break
            return best_child_move, best_score
        else:
            for child in node.get_children():
                _, child_score = self.minimax(child, not player, alpha, beta)
                if(child_score < best_score):
                    best_score = min(best_score, child_score)
                    best_child_move = child
                beta = min(beta, child_score)
                if beta <= alpha:
                    break
            return best_child_move, best_score
    

    def get_move(self):
        best_node,_ = self.minimax(self.root, self.player == PLAYER_ONE)
        return best_node.previous_move if best_node else None
    
    def clear_tree(self):
        def clear_node(node):
            for child in node.get_children():
                clear_node(child)
            node.children = None
        clear_node(self.root)
        self.root = None


"""
Returns the possible moves for the 'player' from the current 'board' state in the form of an array
"""
def get_possible_moves(board, player):
    # Define moves array
    moves = []

    # Get number of rows and columns in the board
    nRows = len(board)
    nCols = len(board[0])

    # For each row in the board
    for row in range(nRows):
        # For each column in a particular row in the board
        for col in range(nCols):
            # If the sign of the value is of the player for whom we want to get moves
            if (player == PLAYER_ONE and board[row][col] >= 0) or (player == PLAYER_TWO and board[row][col] <= 0):
                # Add the coordinates to the moves array
                moves.append((row, col))

    #return the moves array
    return moves



