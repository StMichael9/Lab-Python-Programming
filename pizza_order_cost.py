pizza_size = input("What size pizza do you want? (small or large): ")
pizza_toppings = int(input("How many toppings do you want? "))
delivery_distance = int(input("How many miles away is the delivery? "))


if pizza_size == "small": 
    base_price = 8
elif pizza_size == "large":
    base_price = 12
toppings = 1

if delivery_distance <= 5: 
    delivery_fee = 2 
elif delivery_distance >= 5:
    delivery_fee = 2 + (delivery_distance - 5)

toppings_cost = pizza_toppings * toppings
 
total_cost = base_price + toppings_cost + delivery_fee

print(f"The cost is {total_cost}")
