import re

form = re.compile(r'^(0[1-9]|[1-2][0-9]|3[01])/(0[1-9]|1[0-2])/(0000|(\d{4}))$')

lisht = ['01-01-2001', '31/12/2022', '15/07/1985', '05/05/0000', '20/08/9999']

valid_list = []

for x in lisht:
    if form.match(x):
        valid_list.append(x)


for x in valid_list:
    if x[3]==1:
        
        if x[4]==1:
            month = 'nov'
            day = int(x[3]+x[4])
            year = int(x[6]+x[7]+x[8]+x[9])
            if day>30:
                valid_list.remove(x)
        
    else:

        if x[4]==2:
            month = 'feb'
            day = int(x[3]+x[4])
            
            year = int(x[6]+x[7]+x[8]+x[9])
            
            if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
                if day>29:
                    valid_list.remove(x)
            else:
                if day>28:
                    valid_list.remove(x)
        
        
        elif x[4]==4:
            month = 'apr'
            day = int(x[3]+x[4])
            year = int(x[6]+x[7]+x[8]+x[9])
            if day>30:
                valid_list.remove(x)

        elif x[4]==6:
            month = 'jun'
            day = int(x[3]+x[4])
            year = int(x[6]+x[7]+x[8]+x[9])
            if day>30:
                valid_list.remove(x)
        
        elif x[4]==9:
            month = 'sep'
            day = int(x[3]+x[4])
            year = int(x[6]+x[7]+x[8]+x[9])
            if day>30:
                valid_list.remove(x)

print(valid_list)