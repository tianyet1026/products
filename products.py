#讀取檔案
def read_file(filename):
	#with open('products.csv', 'r', encoding = 'utf-8') as f:
	products=[]
	with open(filename, 'r') as f:
		for line in f:
			if '商品名稱, 商品價格' in line:
				continue
			name, price, unit, total = line.strip().split(',')
	#		print(s)
			products.append([name, price, unit, total])
	print(products)
	return products
#讓使用者輸入
def user_input(products):
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
	return products	

#印出購買紀錄
#sum = 0
def print_products(products):
	for p in products:
		print(p[0],'的價格是',p[1],'買了', p[2], '個,付',p[3],'元')
#	sum += p[3] #計算總付出成本
#print('您共支付', sum, '元')

# 'abc' + '123' = 'abc123' (字串合併)
# 'abc' * 3 = 'abcabcabc'
#寫入檔案
def write_file(filename, products):
	with open(filename, 'w') as f:
	#with open('products.csv', 'w', encoding = 'utf-8') as f:
		f.write('商品名稱, 商品價格, 商品數量, 總支出\n') #寫入標題
		for p in products:
			f.write(p[0] + ',' + str(p[1]) + ',' + str(p[2])+ ','+ str(p[3])+ '\n')


def main():
	filename = 'products.csv'
	import os #開啟作業系統模組
	if os.path.isfile(filename): #用os模組功能檢查檔案是否在本資料夾(要跨資料夾需完整路徑)
		print('找到檔案了')
		products = read_file('products.csv')
		products = user_input(products)
		print_products(products)
		write_file('products.csv', products)
	else:
			print('目前檔案不存在...')
main()