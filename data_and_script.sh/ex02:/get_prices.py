import os

def get_prices(file_name):
    products = []
    prices = []
    
    if not os.path.exists(file_name):
        print(f"Sorry, the specified file does not exist")
        return

    with open(file_name, "r") as file:
        for line in file:
            prod, price = line.strip().split(',')
            prices.append(float(price))
            products.append(prod)

    return products, prices


file_name = input("Insert the file name: ")

if not os.path.exists(file_name):
    print("Sorry, the specified file does not exist")

else:
    products, prices = get_prices(file_name)
    
    print(products[:3])
    print(prices[:3])

    for i in range(len(products)):
        print(f"{products[i]} {prices[i]}")
