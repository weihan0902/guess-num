# 產生一個隨機整數1~100(不要印出來)
# 讓使用者重複輸入數字去猜
# 猜對的話 印出"終於猜對了"
# 猜錯的話 要告訴他 比答案大/小

import random

r = random.randint(1,100)
count = 0 # 不能寫在while迴圈裡面，不然會一直歸零
while True:
	count +=1 # count = count + 1
	num = input('請猜數字: ')
	num = int(num) # 型別轉換
	if num == r: # 17~20都是在if架構裡面，如果要寫在裡面要重複寫3次
		print('你猜中了')
		print('這是你猜的第', count, '次')
		break
	elif num > r:
		print('比答案大')
	elif num < r:
		print('比答案小')
	print('這是你猜的第', count, '次')
