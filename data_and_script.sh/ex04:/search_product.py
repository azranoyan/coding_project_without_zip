def get_prices(fname):
    products = []
    prices = []
   
   
    with open(fname, "r") as file:
        for line in file:
            prod, price = line.strip().split(',')
            products.append(prod)
            prices.append(float(price))


    return products, prices


fname = "data/IT_products.csv"
p = input("What product do you need? ")
products, prices = get_prices(fname)




for prod in products:
    if (prod == p):
        print(f"Product {p} found at index {products.index(prod)}, the price is ${prices[products.index(prod)]}")
        exit()

else:
    print("Sorry, we do not sell that product")