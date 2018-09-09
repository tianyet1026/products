products=[]

while True:
	name = input('請輸入商品名稱:(輸完請按"q"離開)')
	if name == 'q':
		break
	price = input('請輸入商品價格:')
	price = int(price)
	unit = input('你買了多少?')
	unit = int(unit)
	total = price * unit
	products.append([name, price, unit, total])
print(products)	
sum = 0
for p in products:
	print(p[0],'的價格是',p[1],'買了', p[2], '個,付',p[3],'元')
	sum += p[3] #計算總付出成本
print('您共支付', sum, '元')