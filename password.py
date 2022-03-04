password = 'a123456'
i = 3
i = int(i)

while i > 0:
	i = i-1
	answer = input('請輸入密碼')
	if answer != password:
		print('密碼錯誤, 還有', i,'次機會')
	elif answer == password:
		print('登入成功!')
		break


