first_name = "ada"
last_name = "lovelace"
print(f"{first_name.title()} {last_name.title()}")

favorite_food = " CaRbOnaRa "
print(favorite_food.strip().lower().title())

dishes = ["carbonara", "pasta pesto", "salad", "pizza"]

print(dishes)
del dishes[0]
print(dishes)
 # Fetching the last item is done using pop
fetched_dish = dishes.pop()  # it removes the lats element of the list
 # it prints the list excluding the last
dishes.insert(0,"carbonara")
print(dishes)
print(f"Fetched {fetched_dish}")  # here we fetch the element


