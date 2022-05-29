# Write a Python program to reverse a string.
String = "1234abcd"
def reverse(String):
    str2 =" "
    for i in String:
        str2 = i + str2
    return str2
result = reverse(String)
print(result)

