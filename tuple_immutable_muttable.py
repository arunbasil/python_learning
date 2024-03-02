# Question: Tuple is immutable but in some cases the items can be appeneded in tuple in there is list present in it


tuple_example = (1,2,3,["Arun"],4,5)

tuple_example[3].append("Ann")


print(tuple_example)