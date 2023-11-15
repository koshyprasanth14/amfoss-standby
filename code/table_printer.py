def table(tabledata):

    longest_char = 0

    for x in tabledata:
        for y in x:
            if len(y)>longest_char:
                longest_char = len(y)
                break
    
    for x in range(len(tabledata)):
        for y in range(len(tabledata)):

            print(' '* (longest_char-len(tabledata[x][y])+2), tabledata[x][y], end = '')
        
        print()





tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

table(tableData)