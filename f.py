num = int(input("enter the number "))
fact=1
for i in range(1,num+1):
    fact*=i
print(f"the factorial of the {num} is ", fact)



num1 = int(input ("enter the 2nd number "))

def factorial(num1):
    if (num1==0 or num1==1):
        return 1
    else:
        return num1 * factorial(num1-1)
    
print(factorial(9))

# sets is bellow duplicate value will be inored or no be added 

s = { 1,2, 3 ,4 ,  2 , 1 ,7}
print(s)