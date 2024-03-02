duplicate_list =['a','b','c','d','a','b']

# Analysis:
# Can use set but it doesnt maintain order
# Option 1:
# Use Empty list and append if not in empty list:

def remove_duplicates_maintain_order(lst):
    list =[]
    for element in lst:
        if element not in list:
            list.append(element)
    return list

print(remove_duplicates_maintain_order(duplicate_list))


# Option 2: This is better, use a dictionary as it is one line:
# Convert to Dict and get only the from keys (this will remove duplicates) then get thw key

def remove_duplicates_maintain_order_dict(lst):
    return list(dict().fromkeys(lst).keys())

print(remove_duplicates_maintain_order_dict(duplicate_list))
