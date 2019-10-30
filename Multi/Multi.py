#by Erika Fermin 10/30/19
nums = [1, 2, 3, 4, 5]
output = []
nonDiv = []
skip = False
k = 1

for i in range(0, len(nums)):
    for j in range(0, len(nums)):
        k = k*nums[j]
    k = k/nums[i]
    output.append(k)
    k = 1
print(output)

print("what if you can't use division?")

for i in range(0, len(nums)):
    for j in range(0, len(nums)):
        if nums[i] == nums[j]:
            continue

        k = k*nums[j]
    nonDiv.append(k)
    k = 1
print(nonDiv)

