# take n as input from the user
# sum all the numbers from 1 to n
# sum all even numbers from 1 to n
# sum all odd numbers from 1 to n

#range where to start and where to end
n = int(input("Enter n: "))
summation = 0
for x in range(1,n+1):
    if x%2 ==0:
        summation = summation + x

print(summation)


