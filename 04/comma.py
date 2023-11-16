def comma(spam):
    for i in spam:
        if spam.index(i) != len(spam)-1:
            print(i, end=',')
        else:
            print('and', i)

spam = list(input('enter the values seperated by spaces:').split())


comma(spam)
# spam = ['apples', 'bananas', 'tofu', 'cats']

# comma(spam)

# empty=[]

# comma(empty)

