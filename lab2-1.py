#author: DMH 1/10/22

def double_stuff(lst):
    for i,v in enumerate(lst):
        lst[i] = 2 * v 
    return lst

list1 = [6,2,9,'waffles',1.4]
print(double_stuff(list1))

print(double_stuff([1, 2, 3, 4]) == [2, 4, 6, 8])

