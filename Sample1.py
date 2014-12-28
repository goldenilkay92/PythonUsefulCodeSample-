__author__ = 'gokhan'


# print <Output>

print 'Sample'

# line input

argument = raw_input('Hello');
print  'Hi, %s.' % argument


# arrayUsage you can declare all types.

arrayExample = ["1", "2", "3", 1, '2', 0.5];

# for loop example

for item in arrayExample:
    print item

# And or with values in a list
t, f = 1, 0
x, y = 88, 99

a = (t and x) or y
print a

# Search in array example
# Result will be index of current element

arrayExample2 = [1, 2, 4, "2", 0, '1', bool];

print arrayExample2.index("2");


