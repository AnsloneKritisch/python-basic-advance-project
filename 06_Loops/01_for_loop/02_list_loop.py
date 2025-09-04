marks = [ 99 , 100 , 101 , 102 , 103 ]


# find the sum of list 
sum = 0 
for mark in marks:
    sum += mark

print(sum)


# find the maximum number in the list
max = 0

for mark in marks:
    if mark > max:
        max = mark

print(max)