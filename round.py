#Given a variable, x, that stores
#the value of any decimal number,
#write Python code that prints out
#the nearest whole number to x.

#You can assume x is not negative.

# x = 3.14159 -> 3 (not 3.0)
# x = 27.63 -> 28 (not 28.0)

x = 27.63

x_str = str(x)
dot = x_str.find('.')

if x_str[dot+1] >= '5':
    x = x + 1
    x_str = str(x)
    dot = x_str.find('.')
    x = x_str[0:dot]
else:
    x = x_str[0:dot]

print x
