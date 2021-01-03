# TicTacToeAI
  A Tic Tac Toe AI I created in Python by using the minimax algorithm.
  
  The minimax algorithm is a recursive algorithm that is often used in two-player games such as Connect 4 or Tic Tac Toe. It's main idea is to minimize the chances that a worst case scenario occurs. 
  
  Given a certain board state, it considers two players: a maximizing player and a minizing player. The maximizing player seeks to make a move that gives it the maximum value returned by the algorithm while the minimizing player seeks to make a move that gives it the minimum value. These values are values that are assigned to each ending state of the game (in the case of TicTacToe if someone gets three in a row or there is a tie). In my program, the algorithm returns +1 if X wins, -1 if O wins, and 0 if it's a tie. The algorithm then makes its move based on the theory that its opponent will choose a move that maximizes its chance of winning. 
  
  For example if the user chooses to be 'X,' then during the AI's turn, the algorithm will look at all the possible board states and choose a move that either returns -1 (it wins) or it will choose a move that avoids as many +1 board states as possible(states in which the user wins i.e. the worst case scenario). In this case, the AI is the minimizing player and the user is the maximizing player.

