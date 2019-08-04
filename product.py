#讀取檔案
products = []
with open('products.csv','r',encoding ='utf-8') as f:
    for line in f:
        if '商品,價格' in line:
            continue
        name, price = line.strip().split(',')  #Split切割後的結果是清單
        products.append([name,price])
print (products)

#讓使用者輸入
while True:
        name = input ("Please input the prodcut name? ")
        if name == 'q':
            break
        price = input ("please input the price? ")
        price = int(price) #轉換價錢為數字型態
        products.append([name,price])
print(products)

for p in products:
    print(p[0], 'price is', p[1])


with open('products.csv', 'w', encoding ='utf-8') as f: #寫入模式,並且明確告知我要用utf編碼寫入
    f.write('商品,價格\n') #加上第一行的欄位
    for p in products:
        f.write(p[0] + ',' + str(p[1]) + '\n') #轉換價錢為文字型態才能與字串合併
