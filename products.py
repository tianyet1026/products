products=[]

while True:
	name = input('請輸入商品名稱:(輸完請按"q"離開)')
	if name == 'q':
		break
	price = input('請輸入商品價格:')
	products.append([name, price])
print(products)	