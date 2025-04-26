#some of the string 

name = "HEMANTH"
# string slicing
print(name[0:5])


# practuicle use of if else 
import  time  
time_t = time.strftime('%H:%M:%S')
print(time_t)


name1 = "samsung"
for c in name1:
    print(c)



for i in range(10):
    print("i am number ", i)

j = 15
while(j>0):
    print(" i am the value decreasing", j)
    j-=1



arr = [1,2,3,4,5,6]
print(arr[2])

# pyhton supports both the postive and negetive indexs 

if 6 in arr:
    print("yes is present")
else: 
    print(" no is not present")



even = []

for x in range(100):
    if(x%2 == 0):
        even.append(x)

print(even)



countries = ("India" , "Russia" ,"Netherland", "COntinental")
print(countries.count(1))