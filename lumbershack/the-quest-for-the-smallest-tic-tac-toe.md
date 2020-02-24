## The Quest For The Smallest Tic-Tac-Toe

As the first blog post here, I feel I should warn that I'm not the best at writing. Today, we have a problem. Tic-Tac-Toe.

### The Problem:

At this point, you're probably wondering, what the hell is wrong with tic-tac-toe. Nothing really, except for the fact that our original programs took up almost two hundred fucking lines. Now I'm not one to really one to care about size, but for the intention of keeping a small file size, and for a later project, I challengd my friend. In order to win, the rules where simple, whoever made a fully functional tic-tac-toe game, in the least lines, and the loser paid for shipping on our amazon order.

### The Race For The Smallest:

Each of us, with our tic-tac-toes, mine at ~180 lines, and his at an advantageous ~120, we set out to slim down our projects.

After only a few minutes of looking for obvious space wasters, I was down to 94 lines. But, like he always does, my friend catches up quickly.
This is the code I had at this point.

  
<code>#Non spagghetti Code.
  
    import sys #import sys so we can close our program

    board = ['#','#','#','#','#','#','#','#','#',] #Define the board as a list that we can change and inspect for wins

    currentPlayer = 'X' #Sets the current player incase they enter an invalid option


    def printBoard(): #Create a function to print the board in sections, instead of in a line

      print(board[0:3])

      print(board[3:6])

      print(board[6:9])

    def play(player): #Create a function we can call when we want a player to have a turn

      currentPlayer = player
  
      turn = input('Player enter position from 1 through 9:') #Grab players input as an integer beetween 1 and 9
  
        if turn < 10:
    
          turn -= 1 #Make the integer 1 less, so we can change the item in our list   
      
          if board[turn] =='#': #Check if the space is blank, so you dont overwrite other moves
      
            board[turn] = player #Set the current space selected to the players symbol
        
        else:
    
          print('Invalid option') #If the space chosen is anything else we print invalid option and play the turn again
      
          play(currentPlayer)
      

    def wins(): #Define each and every single possible win, for each player

      if currentPlayer == 'X':
  
        if board[0:3]  == ['X','X','X'] or board[3:6]  == ['X','X','X'] or board[6:9] == ['X','X','X']: #Horizontal wins for x
    
          print('X Wins')
      
          sys.exit()
      
        if board[0] == 'X' and board[3] == 'X' and board[6] == 'X': #Vertical wins for X
    
          print('X Wins')
      
          sys.exit()
      
        if board[1] == 'X' and board[4] == 'X' and board[7] == 'X':
    
          print('X Wins')
      
          sys.exit()
      
        if board[2] == 'X' and board[5] == 'X' and board[8] == 'X':
    
          print('X Wins')
      
          sys.exit()
      
        if board[0] == 'X' and board[4] == 'X' and board[8] == 'X': #Diagonal wins for X
    
          print('X Wins')
      
          sys.exit()
      
        if board[2] == 'X' and board[4] == 'X' and board[6] == 'X':
    
          print('X Wins')
      
          sys.exit()
      
      if currentPlayer == 'O':
  
        if board[0:3] == ['O','O','O'] or board[3:6] == ['O','O','O'] or board[6:9] == ['O','O','O']: #Horizontal wins for O
    
          print('O Wins')
      
          sys.exit()
      
        if board[0] == 'O' and board[3] == 'O' and board[6] == 'O': #Vertical wins for O
    
          print('O Wins')
      
          sys.exit()
      
        if board[1] == 'O' and board[4] == 'O' and board[7] == 'O':
    
          print('O Wins')
      
          sys.exit()
      
        if board[2] == 'O' and board[5] == 'O' and board[8] == 'O':
    
          print('O Wins')
      
          sys.exit()
      
        if board[0] == 'O' and board[4] == 'O' and board[8] == 'O': #Diagonal wins for O
    
          print('O Wins')
      
          sys.exit()
      
        if board[2] == 'O' and board[4] == 'O' and board[6] == 'O':
    
          print('O Wins')
      
          sys.exit()
      

    def playCycle(): #Create a cycle of 9 plays, 5 by x, 4 by 0. We only run wins every turn because there was a weird bug in the code somewhere

      printBoard() #Standard cycle should look like this #Prints the current state of the board
  
      play('X') #Start a turn with the current player, in this case X
  
      wins() #Check for a win on the board #Theoreticaly, you only need to check after the 5th turn
  
      printBoard()
  
      play('O')
  
      wins()
  
      printBoard()
  
      play('X')
  
      wins()
  
      printBoard()
  
      play('O')

      wins()
  
      printBoard()
  
      play('X')
  
      wins()
  
      printBoard()
  
      play('O')
  
      wins()
  
      printBoard()
  
      play('X')
  
      wins()
  
      printBoard()
  
      play('O')
  
      wins()
  
      printBoard()
  
      play('X')
  
      currentPlayer = '' #Last turn, set current player to '' and then
  
      print(currentPlayer) # print it to create a blank line
  
      printBoard() #print the final state of the board, which at this point would be a cats game
  
      wins() #Im paranoid, so might as well check for a win one last time.
  

    playCycle() #Run the game!</code>


