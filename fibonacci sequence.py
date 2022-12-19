fib = int(input('\nenter the no. of terms to be displayed:'))
a=0
b=1
print(a)
print(b)

for x in range(2,fib):
        c = a+b
        a = b
        b = c

        print(c)
print('\nthe above is a fibonacci sequence')

        
