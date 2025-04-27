def double(x):
    print(x*x*x)

double(5)

# the above is same as 

double = lambda x : x*x*x
print(double(2))



# bellow is Map Reduce and filter 

def cube(x):
    return x*x*x

l = [1,2,3,4,5]
newl = []
for item in l:
    newl.append(cube(item))


# the above op i same as bellow

newl = list(map(cube,l))
print(newl)


# filtering 

#filter(predicate , iterable)

def filter_func(a):
    return a > 4

newnewl = list(filter(filter_func , l))

print(newnewl)  # now i will be getting all elements reater than 4



# reduce is bellow  , we must alwasys inmport reduce 


from functools import reduce
num = [1,2,3,4,5]

sum = reduce(lambda x,y:x+y , num)

# just printing the sum 
print(sum)