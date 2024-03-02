# Given a string, find the first non-repeated character using a dictionary.
# Solution:
def find_first_unique(string):
    count_dict = {}
    for char in string:
        if char in count_dict:
            count_dict[char] += 1
        else:
            count_dict[char] = 1
    for char in string:
        if count_dict[char] == 1:
            return char
    return None

x ='pple'
print(find_first_unique(x))

# Write a function to merge two dictionaries. If there are common keys, append the values in a list.
def merge_dicts(d1, d2):
    merged = {**d1}
    for key, value in d2.items():
        if key in merged:
            if isinstance(merged[key], list):
                merged[key].append(value)
            else:
                merged[key] = [merged[key], value]
        else:
            merged[key] = value
    return merged



fruits = {"Apple":10,"Oranges":15, "Grapes":12}


def print_fruit(fruits):
 for fruit in fruits.keys():
     print(fruit)

def print_fruit_qty(fruits):
     for fruit in fruits.values():
         print(fruit)

fruits = {"Apple":10,"Oranges":15, "Grapes":12}
def print_fruit_qty_price(fruits):
    for fruit in fruits.values():
        fruit_price = fruit*5
        print(fruit_price)

fruit_world = {
    "Apple": {"qty": 10, "price": 2},  # Assuming the price is 2 per Apple
    "Oranges": {"qty": 15, "price": 1.5},  # Assuming the price is 1.5 per Orange
    "Grapes": {"qty": 12, "price": 3}  # Assuming the price is 3 per Grape
}

def print_total_inventory(fruit_world):
    total_inventory = 0
    for fruit,details in fruit_world.items():
        total_price = details["qty"] * details["price"]
        print(f"Total price = {total_price}")
        total_inventory+=total_price
    print(total_inventory)





print_fruit(fruits)

print_fruit_qty(fruits)

print_fruit_qty_price(fruits)

print_total_inventory(fruit_world)