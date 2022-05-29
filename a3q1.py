#  Write a Python function to sum all the numbers in a list.
list = [8,2,3,0,7]
def sumlist(list):
    sum = 0
    for i in list:
        sum = sum + i
    return sum
result=sumlist(list)
print(result)
