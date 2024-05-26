import itertools

def get_prices():
    products = []
    prices = []
    with open("data/IT_products.csv", "r") as file:
        for line in file:
            parts = line.split(',')
            prices.append(float(parts[1]))
            products.append(parts[0])

    return products, prices


products, prices = get_prices()

products_prices_pair = zip(products, prices)

my_dict = dict(products_prices_pair)
first_two = dict(itertools.islice(my_dict.items(), 2))
red = list(my_dict.items())[:2]
print(red)

p = input("What producct do you need? ")
try:
    x = products.index(p)
    y= prices[x]
    print("The price is $"+ str(y))

except:
    print("Sorry, we do not sell that product")
