# ==============================================
# Project Name : iShop Calculator
# Author       : Ahmed Waled
# Date         : 21-10-2025
# Description  : Calculate the number of items and their prices
# ==============================================

items = []
prices = []

print("** Welcome to iShop Calculator **")

number_items = int(input("How many items are there in your basket today? "))

if number_items > 0:
    print("\nLet's get to counting them...\n")
    for i in range(number_items):
        name_item = input(f"Please tell me the name of item {i + 1}: ")
        items.append(name_item)

        item_price = float(input(f"What is the price of {name_item}? "))
        prices.append(item_price)

    all_items = input("\nWould you like to see your entire basket items? (Yes/No): ").capitalize()

    if all_items == "Yes":
        print(f"\nYour basket items are: {items}")

        total_price = input("Would you like to see how much it'll cost? (Yes/No): ").capitalize()
        if total_price == "Yes":
            print(f"\nBuying these items will cost: {sum(prices)}")
        else:
            print("\nOkay, exiting program.")
    else:
        print("\nOkay, exiting program.")
else:
    print("No items entered. Exiting program.")
