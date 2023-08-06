# Define the stock and the prices of a small shop.

# Define a function compute_bill that accepts list of items.
# Check whether the shop has each item in stock, and then calculate the total price of the shopping list.

# Finally, modify the stock of the shop to reflect the items bought.


stock = {
    "apple": 1,
    "banana": 15,
    "chocolate": 101
}
prices = {
    "apple": 0.39,
    "banana": 0.15,
    "chocolate": 1.50
}

print("There's a discount on chocolate!")
prices["chocolate"] = 1.40


total_price = 0
shopping_list = ["apple", "apple", "chocolate", "banana"]


for item in shopping_list:
    print("Processing:", item)
    item_stock = stock[item]
    if item_stock > 0:
        stock[item] = item_stock - 1
    else:
        print(item, "out of stock.")
        continue
    item_price = prices[item]
    print(item, "costs", item_price)
    total_price = total_price + item_price


print("\nTotal price:", total_price)
