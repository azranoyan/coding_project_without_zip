import sys

product_names = []
product_prices = []

filter
products_file = open(input("insert the file name: "))
for line in products_file: 
    "[name,price]"
    product = line.split(',')

    product_names.append(product[0])
    product_prices.append(float(product[1]))

products_file.close()

cheap_products = []
expensive_products = []

for i in range(0, len(product_prices)):
    price = product_prices[i]
    name = product_names[i]

    if price < 100:
        cheap_products.append(name + "," + str(price) + "\n")
    else:
        expensive_products.append(name + "," + str(price) + "\n")

result_cheap_products_file = open("data/cheap_products.csv", "w")
result_expensive_products_file = open("data/expensive_products.csv", "w")

result_cheap_products_file.writelines(cheap_products)
result_expensive_products_file.writelines(expensive_products)

result_cheap_products_file.close()
result_expensive_products_file.close()

print("Files created!")