# x = 2
# print(type(x))
# print(x)

# x = "Hello World!"
# print(type(x))
# print(x)


# x = 20
# print(type(x))
# print(x)

# x = 20.5
# print(type(x))
# print(x)

# x = 1j
# print(type(x))
# print(x)
           
# x = {"apple", "banana", "cherry"}
# print(type(x))
# print(x)

# x = ("apple", "banana", "cherry")
# print(type(x))
# print(x)

# x = range(2, 6)
# print(type(x))
# print(x)

# x = {"name" : "Luke", "age" : "30"}
# print(type(x))
# print(x)

# x = frozenset({"apple", "banana", "cherry"})
# print(type(x))
# print(x)

nums = [2,7,11,15]
target = 26
print(len(nums))
for index in range(len(nums)):
    print("First For loop  current value : " + str(nums[index]))
    print("First Forloop current index : " + str(index))
    for j in range(index + 1, len(nums)):
        print("2nd for loop current value : " + str(nums[j]))
        print("2nd for loop current index : " + str(j))

        leftValue = nums[index]
        rightValue = nums[j]
        print("leftValue is : " + str(leftValue) + " rightValue is : " + str(rightValue))
        
        if leftValue + rightValue == target:
            print(index)
            print(j)
            c = "a"
        




