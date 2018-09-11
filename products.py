products=[]
with open('products.csv', 'r') as f:
#with open('products.csv', 'r', encoding = 'utf-8') as f:
	for line in f:
		name, price, unit, total = line.strip().split(',')
#		print(s)
		products.append([name, price, unit, total])
	print(products)







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
#sum = 0
#for p in products:
#	print(p[0],'的價格是',p[1],'買了', p[2], '個,付',p[3],'元')
#	sum += p[3] #計算總付出成本
#print('您共支付', sum, '元')

# 'abc' + '123' = 'abc123' (字串合併)
# 'abc' * 3 = 'abcabcabc'
with open('products.csv', 'w') as f:
#with open('products.csv', 'w', encoding = 'utf-8') as f:
#	f.write('商品名稱, 商品價格, 商品數量, 總支出\n')
	for p in products:
		f.write(p[0] + ',' + str(p[1]) + ',' + str(p[2])+ ','+ str(p[3])+ '\n')