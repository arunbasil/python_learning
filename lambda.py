# Example 4: Lambda function with filter().
# FILTER,MAP It takes two required parameters: a function (lambda) and an iterable (list) in the below case
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
odd_nums = list(filter(lambda x: x % 2 != 0, nums))
print(odd_nums)

# Example 5: Lambda function with map().

nums = [1, 2, 3, 4, 5]
squared_nums = list(map(lambda x: x ** 2, nums))
print(squared_nums)  # Output: [1, 4, 9, 16, 25]


# Filter applies ONLY to specific items in the Iterables whereas map applies to ALL items in the Iterable

# REDUCE
# from functools import reduce
#
# nums = [1, 2, 3, 4, 5]
# product = reduce((lambda x, y: x * y), nums)
# print(product)  # Output: 120


from functools import reduce

transactions = [
    {'amount': 100},
    {'amount': 200},
    {'amount': 50},
]

# total_amount = reduce(lambda total, transaction: total + transaction['amount'], transactions,0)
# print(total_amount)  # Output: 350

tl_amt = sum(map(lambda trns:trns['amount'],transactions))
print(tl_amt)














