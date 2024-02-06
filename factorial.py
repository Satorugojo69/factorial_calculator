fh = open('output.txt','w')

def fact(n):
    if n == 1:
        return 1
    else:
        return fact(n - 1) * n

number = int(input("Enter the number you want factorial : "))
a = fact(number)
fh.write("The number is : " + str(number) + '\n')
fh.write("Factorial of number is :" + str(a) + "\n")
