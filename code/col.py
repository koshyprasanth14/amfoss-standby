def collatz(number):
        
        if number%2==0:
            x = number//2
            print(x)
            return x
        else:
            x = 3*number +1
            print(x)
            return x
    


z = int(input('Enter a number :'+ '\n'))

try:
    while z != 1:
        z= collatz(z)
except ValueError:
        print('invalid input')