def mean_and_variance(numbers):
    mean = 1/len(numbers) * sum(numbers)
    variance = 1/(len(numbers)-1) * sum((numbers - mean)**2)
    return mean, variance

from numpy import mean, var, arange

nums = arange(0, 10)
print(f"Numbers: {nums}")
print(f"Mean and variance: {mean_and_variance(nums)}")
print(f"With numpy: {mean(nums)}, {var(nums, ddof=1)}")