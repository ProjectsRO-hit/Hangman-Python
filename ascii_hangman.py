def hangman_graphic(lives):
    stages = [
        # Stage 6: Full hangman (game over)
        '''
          -----
          |   |
          O   |
         /|\\  |
         / \\  |
              |
        --------
        ''',
        # Stage 5: Missing one leg
        '''
          -----
          |   |
          O   |
         /|\\  |
         /    |
              |
        --------
        ''',
        # Stage 4: Missing both legs
        '''
          -----
          |   |
          O   |
         /|\\  |
              |
              |
        --------
        ''',
        # Stage 3: Missing one arm
        '''
          -----
          |   |
          O   |
         /|   |
              |
              |
        --------
        ''',
        # Stage 2: Only torso and head
        '''
          -----
          |   |
          O   |
          |   |
              |
              |
        --------
        ''',
        # Stage 1: Only head
        '''
          -----
          |   |
          O   |
              |
              |
              |
        --------
        ''',
        # Stage 0: Empty gallows
        '''
          -----
          |   |
              |
              |
              |
              |
        --------
        '''
    ]
    return stages[lives]
