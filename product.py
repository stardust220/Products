#加入是否檔案在不在
import os # operating system
products = []
def read_file(filename):#讀取檔案 #檔名建議寫在parameter
    if os.path.isfile(filename):
        print('yes, the file exists')
        with open(filename,'r',encoding ='utf-8') as f:
            for line in f:
                if '商品,價格' in line:
                    continue
                name, price = line.strip().split(',')  #Split切割後的結果是清單
                products.append([name,price])
        print (products)
    else:
        print('cannot find the file')
    return products
#讓使用者輸入
def user_input(products):
    while True:
        name = input ("Please input the prodcut name? ")
        if name == 'q':
            break
        price = input ("please input the price? ")
        price = int(price) #轉換價錢為數字型態
        products.append([name,price])
    print(products)
    return products

def print_products(products):
    for p in products:
        print(p[0], 'price is', p[1])

def  write_file(filename,products):
    with open(filename, 'w', encoding ='utf-8') as f: #寫入模式,並且明確告知我要用utf編碼寫入
        f.write('商品,價格\n') #加上第一行的欄位
        for p in products:
            f.write(p[0] + ',' + str(p[1]) + '\n') #轉換價錢為文字型態才能與字串合併


products = read_file('products.csv')
products = user_input(products)
print_products(products)
write_file('products.csv',products)

