def trim(s):
	i=0
	x=-1
	y=0
	status = 0
	while i < len(s):
		if s[i] != ' ':
			status = 1
			y = 0 # 遇到非空格，重新计算末尾空格数
		elif s[i] == ' ' and status == 0:
			x = i
		elif s[i] == ' ' and status == 1:
			y+=1 #存储字符串末尾的空格数
		i+=1
	return s[x+1:len(s) - y]
	# 测试:
if trim('hello  ') != 'hello':
    print('测试失败1!',trim('hello  '))
elif trim('  hello') != 'hello':
    print('测试失败2!',trim('  hello'))
elif trim('  hello  ') != 'hello':
    print('测试失败3!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败4!')
elif trim('') != '':
    print('测试失败5!')
elif trim('    ') != '':
    print('测试失败6!')
else:
    print('测试成功!')