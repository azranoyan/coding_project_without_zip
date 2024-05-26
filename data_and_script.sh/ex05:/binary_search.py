def get_prices(fname):
    products = []
    prices = []

    with open(fname, "r") as file:
        for line in file:
            parts = line.split(',')
            products.append(parts[0])
            prices.append(float(parts[1]))

    return products, prices



def choose_half(l, x, i, j):
    k = (i + j)//2
    z = l[k]

    if (x == z):
        return k, k
    elif (x < z):
        return i, k
    else:
        return k+1, j
    


def binary_search(list, p):
    i = 0
    j = len(list)-1
    i, j = choose_half(l, p, i, j)
    count = 1
    while (j > i):
        i, j = choose_half(l, p, i, j)
        count = count+1 


    return j, count

fname = "data/sorted_products.csv"
l, prices = get_prices(fname)
p = input("What product do you need? ")


j, count = binary_search(l, p)

if p == l[j]:
    print("Product", p, "found after", count, "comparisons", ", the price is $" + str(prices[j]))
else:
    print("Sorry, we do not sell that product")