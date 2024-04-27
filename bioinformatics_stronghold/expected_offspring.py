
def expct_offspring(nums):
    probabilities = [1, 1, 1, 0.75, 0.5, 0]
    expected_offspring = []
    for i in range(len(nums)):
        expected_offspring.append((nums[i]*2) * probabilities[i])
    return sum(expected_offspring)


nums = [19430, 16455, 16342, 18654, 19616, 18754]
exp_offs = expct_offspring(nums)
print(exp_offs)
