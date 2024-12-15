#    Main Author(s): Mohdeep Singh, Ayush Patel
#    Main Reviewer(s): Archi Mukeshbhai Kakadiya

from a1_partc import Queue
from a1_partd import overflow

# Constants
WINNING_SCORE = 1000000
LOSING_SCORE = -1000000
WINNING_THRESHOLD = 999999
LOSING_THRESHOLD = -999999
PLAYER_ONE = 1
PLAYER_TWO = -1
ALPHA = float('-inf')
BETA = float('inf')

# Creates a copy of the board
def copy_board(board):
    current_board = []
    height = len(board)
    for i in range(height):
        current_board.append(board[i].copy())
    return current_board

def evaluate_board(board, player):
    """
    Evaluates the board state to calculate a score for a given player.
    
    Parameters:
    - board (list): The current state of the game board.
    - player (int): The player for whom the score is calculated (PLAYER_ONE or PLAYER_TWO).
    
    Returns:
    - int: The score representing the advantage or disadvantage for the player.
    """
    player_score = 0
    opponent_score = 0

    for row in board:
        for cell in row:
            if (player == PLAYER_ONE and cell > 0) or (player == PLAYER_TWO and cell < 0):
                player_score += abs(cell)
            else:
                opponent_score += abs(cell)

    if player_score > 0 and opponent_score == 0:
        return WINNING_SCORE
    elif player_score == 0 and opponent_score > 0:
        return LOSING_SCORE
    return player_score - opponent_score

# Get all valid moves for the current player
def get_possible_moves(board, player):
    moves = []
    nRows = len(board)
    nCols = len(board[0])
    for row in range(nRows):
        for col in range(nCols):
            if (player == PLAYER_ONE and board[row][col] >= 0) or (player == PLAYER_TWO and board[row][col] <= 0):
                moves.append((row, col))
    return moves

class GameTree:
    class Node:
        def __init__(self, board, depth, player, tree_height=4):
            """
            Initializes a node within the game tree.
            
            Parameters:
            - board (list): The game board at this node's state.
            - depth (int): The depth of this node in the tree.
            - player (int): The player whose move is represented at this node.
            - tree_height (int): The maximum height of the tree (default is 4).
            """
            self.board = copy_board(board)
            self.depth = depth
            self.player = player
            self.tree_height = tree_height
            self.parent = None
            self.children = []
            self.score = None
            self.previous_move = None

        def is_game_won(self):
            """
            Determines if the current node represents a winning state.
            
            Returns:
            - bool: True if the game is won, False otherwise.
            """
            score = evaluate_board(self.board, self.player)
            return score > WINNING_THRESHOLD or score < LOSING_THRESHOLD

        # Check if the maximum depth is reached
        def is_max_height(self):
            return self.depth >= self.tree_height - 1

        # Add a child node
        def add_child(self, node):
            self.children.append(node)
            node.parent = self

        # Set the score for this node
        def set_score(self, score):
            self.score = score

        # Get the list of child nodes
        def get_children(self):
            return self.children

        # Get the parent node
        def get_parent(self):
            return self.parent

    def __init__(self, board, player, tree_height=4):
        """
        Initializes the game tree with a root node and builds the tree.
        
        Parameters:
        - board (list): The initial state of the game board.
        - player (int): The player who starts the game (PLAYER_ONE or PLAYER_TWO).
        - tree_height (int): The maximum height of the tree (default is 4).
        """
        self.board = copy_board(board)
        self.player = player
        self.tree_height = tree_height
        self.root = self.Node(self.board, 0, self.player, tree_height)
        self.create_tree(self.root)

    def create_tree(self, node):
        """
        Recursively creates the game tree by expanding child nodes.
        
        Parameters:
        - node (GameTree.Node): The current node to expand.
        """
        if node.is_max_height() or node.is_game_won():
            score = evaluate_board(node.board, node.player) * node.player
            node.set_score(score)
        else:
            possible_moves = get_possible_moves(node.board, node.player)
            for move in possible_moves:
                board = copy_board(node.board)
                board[move[0]][move[1]] += node.player
                queue = Queue()
                overflow(board, queue)

                new_node = self.Node(board, node.depth + 1, -node.player, self.tree_height - 1)
                new_node.previous_move = move
                node.add_child(new_node)
                self.create_tree(new_node)

    def minimax(self, node, player, alpha = ALPHA, beta = BETA):
        """
        Implements the Minimax algorithm with alpha-beta pruning to evaluate the best move 
        for the current player based on the game tree.

        Parameters:
        - node (Node): The current node of the game tree being evaluated.
        - player (bool): Indicates whether it's the maximizing player's turn (True) 
                        or the minimizing player's turn (False).
        - alpha (float): The best score achievable by the maximizing player so far.
        - beta (float): The best score achievable by the minimizing player so far.

        Returns:
        - tuple:
            - Node: The child node corresponding to the best move.
            - int: The score of the best move.
        """
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
        """
        Determines the best move for the current player using the minimax algorithm.
        
        Returns:
        - tuple: The (row, column) of the best move, or None if no valid move exists.
        """
        best_node, _ = self.minimax(self.root, self.player == PLAYER_ONE)
        return best_node.previous_move if best_node else None

    def clear_tree(self):
        """
        Clears the game tree to free up memory by removing all child nodes.
        """
        def clear_node(node):
            for child in node.get_children():
                clear_node(child)
            node.children = None
        clear_node(self.root)
        self.root = None