
# sum of all the numbers from a given list of numbers

nums = [2, -7, 8, 9, 4]  #2, 2+(-7), 2+(-7)+8, 2+(-7)+8+9, 2+(-7)+8+9+4
summation = 0 # 2, -5, 3,  12, 16

# for each number in nums ; sum = sum + number

for x in nums:
    summation = summation+x
    print(summation)

# 1st iteration: summation = 0 + 2 = 2
# 2nd iteration : summation = 2 + -7 = -5
# 3rd iteration : summation = -5 + 8 = 3

print("The summation is: ", summation)


