nums = list()
for x in range(0, 10):
    nums.append(float(input('Digite um numero inteiro: ')))
for x in range(9, -1, -1):
    print(nums[x], end='')