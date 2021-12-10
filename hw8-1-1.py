# Author: SMR (AMDG) 12/10/21
def conv_celsius(fahrenheit):
    celsius = round((((fahrenheit) - 32) * 5/9), 2)
    return celsius
print(conv_celsius(40) == 4.44)
print(conv_celsius(94) == 34.44)
print(conv_celsius(37) == 2.78)