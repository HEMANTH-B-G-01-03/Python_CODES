#methods in the dicory 
emp = { 122:21 ,
       111: 12
       } 
emp2 = {
    222: 67,
    221: 27
}
emp.update(emp2)
print(emp)

# emp.clear()

emp.popitem()
print(emp)



# exception handling usin try and catch 

a = input("enter the number")
print(f"Multiplicationtable of {a} is ")

try: 
    for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a)*i }")

except Exception as e:
    print(" this is not a integer number ")
finally: 
    print(" i will be executed always ")




# if elsse in sinlge like an ternary operator

a = 10 
b = 1

print(a) if a>b  else print(b)
