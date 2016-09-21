#! env/bin/python
""" 
Given 2 integers m and n such that m < n,
find the numbers between m and n which are divisible by both 3 and 5. 
 """
 
m = int(raw_input('Enter m: '))
n = int(raw_input('Enter n: '))

 
if(m < n):
    #print('thx')
    for i in range(m,n+1):
        if(i%3 == 0 and i%5 == 0):
            print(i)
else:
    print("Please enter correct input, m must be less than n")

 