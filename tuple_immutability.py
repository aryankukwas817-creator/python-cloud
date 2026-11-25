a=[1,2,3,4,5]
a[1]=10
print(a)
numbers=(10,20,30)
# numbers[1] = 90

numbers = numbers[:1] + (99,) + numbers[2:]
print(numbers)