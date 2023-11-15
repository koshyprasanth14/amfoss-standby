def isValidChessBoard(board):

    blacks = 0
    whites = 0

    wking = 0
    bking = 0

    wpawn = 0 
    bpawn = 0


    positions_possible = ['1a','1b','1c','1d','1e','1f','1g','1h',
                          '2a','2b','2c','2d','2e','2f','2g','2h',
                          '3a','3b','3c','3d','3e','3f','3g','3h',
                          '4a','4b','4c','4d','4e','4f','4g','4h',
                          '5a','5b','5c','5d','5e','5f','5g','5h',
                          '6a','6b','6c','6d','6e','6f','6g','6h',
                          '7a','7b','7c','7d','7e','7f','7g','7h',
                          '8a','8b','8c','8d','8e','8f','8g','8h']
    
    for position, piece in board.items():

        if position not in positions_possible:
            return False
        
        if piece[0]=='b':
            blacks+=1
        elif piece[1]=='w':
            whites+=1

        if blacks>16 or whites>16:
            return False
        
        if piece == 'bking':
            bking +=1
        if piece == 'wking':
            wking +=1

        if wking>1 or bking>1:
            return False
        
        if piece == 'wpawn':
            wpawn+=1

        if piece == 'bpawn':
            bpawn+=1
            
        if wpawn>1 or bpawn>1:
            return False

    return True       


hmm =  {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}

v = isValidChessBoard(hmm)

print(v)