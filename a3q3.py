# Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
string = 'The quick Brow Fox'
def upplow(string):
    upp = 0
    low = 0
    for i in string.split(" "):
        for j in i:
            if j.isupper():
                upp+=1
            else:
                low+=1
    print("no. of upper case:",upp)
    print("no. of lower case:",low)
upplow(string)