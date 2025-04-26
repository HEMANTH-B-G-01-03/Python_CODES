import time

time_t = time.strftime('%H:%M:%S')
print(time_t)

hr=int(time.strftime('%H'))
print(hr)

if(hr>0 and hr < 12 ):
    print("Good Morning")

elif(hr>=12 and hr <17 ):
    print("good afernoon ")
elif(hr>=17 and hr<=24):
    print("good Night")
else:
    print("no time")


def greet(name):
    print(f"Hello, {name}!")

def add(a, b):
    return a + b

if __name__ == "__main__":
    # This block will run only if the script is executed directly
    greet("Hemanth")
    result = add(5, 3)
    print(f"The sum is: {result}")


