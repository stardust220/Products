Account = []

while True:
        name = input ("Please input the prodcut name? ")
        if name == 'q':
            break
        price = input ("please input the price? ")
        #products = []
        #products.append (name)
        #products.append (price)
        Account.append([name,price])
print(Account)