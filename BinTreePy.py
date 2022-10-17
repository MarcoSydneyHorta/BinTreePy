def Level(nodes):
    import math
    return int(math.log(int(nodes)+1,2))

nod = input('Enter the number of nodes(n) of a tree, whose size is 2**n - 1 (1 or 3 or 7 or 15 or 31 or 63 ...) : ')
print (f'This binary tree is height {Level(nod)} ')
