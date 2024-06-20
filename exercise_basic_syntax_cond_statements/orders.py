n_orders = int(input())
total_price = 0

for i in range(1, n_orders + 1):
    price_per_capsule = float(input())
    days = int(input())
    capsules_needed_per_day = int(input())

    coffee_price = price_per_capsule * days * capsules_needed_per_day

    if 0.01 <= price_per_capsule <= 100 and 1 <= days <= 31 and 1 <= capsules_needed_per_day <= 2000:
        print(f"The price for the coffee is: ${coffee_price:.2f}")
        total_price += coffee_price

else:
    print(f'Total: ${total_price:.2f}')