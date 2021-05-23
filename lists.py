#list are represented by a square bracket []
#list is implemented in cpython using array datastructure

bicycles = ['a','b','c','d','e']
print(bicycles[0])
for bicycle in bicycles:
    print(bicycle)

#removes the last element
bicycles.pop()     

bicycles.remove('d')

for bicycle in bicycles:
    print(bicycle)

