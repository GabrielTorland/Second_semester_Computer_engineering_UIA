import csv


def main():
    customers = {}
    products = {}
    orders_product = {}
    rows = 0
    customers_price = {}
    with open('customers.csv', newline='') as csv_file:
        for word in csv.reader(csv_file):
            if rows == 0:
                rows += 1
                continue
            customers[(word[0])] = {}
            customers[(word[0])]['name'] = word[1]
            customers[(word[0])]['address'] = word[2]
            print("Customer: ", end='')
            print(customers[(word[0])]['name'], end=', ')
            print(customers[(word[0])]['address'])
            rows += 1
        rows = 0
    with open('products.csv', newline='') as csv_file2:
        for word in csv.reader(csv_file2):
            if rows == 0:
                rows += 1
                continue
            products[word[0]] = {}
            products[(word[0])]['product'] = (word[1])
            products[(word[0])]['price'] = (word[2])
            print("Product: ", end='')
            print(products[word[0]]['product'], end=', ')
            print(products[word[0]]['price'])
            rows += 1
        rows = 0
    with open('orders.csv', newline='') as csv_file3:
        for word in csv.reader(csv_file3):
            if rows == 0:
                orders_product[word[2]] = word[3]
                rows += 1
                continue
            elif word[2] in orders_product.keys():
                orders_product[word[2]] += int(word[3])
            else:
                orders_product[word[2]] = int(word[3])
            if word[1] in customers_price.keys():
                customers_price[word[1]] += int(word[3]) * int(products[word[2]]['price'])
            else:
                customers_price[word[1]] = int(word[3]) * int(products[word[2]]['price'])
        for order in products.keys():
            print(products[order]['product'], end=" amount: ")
            print(orders_product[order])
            print(products[order]['product'], end=" gross income: ")
            print(orders_product[order] * int(products[order]['price']))
        for customer in customers.keys():
            print(customers[customer]['name'], end=" money spent: ")
            print(customers_price[customer])


if __name__ == "__main__":
    main()
