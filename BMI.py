l = input('請輸入身高(CM):')
l = float(l)
kg = input('請輸入體重(KG):')
kg = float(kg)
l = l / 100
BMI = kg / l / l
print('BMI:' , BMI)
if BMI < 18.5:
	print('體重過輕')
elif 18.5 <= BMI < 24:
	print('正常範圍')
elif 24 <= BMI < 27:
	print('過重')
elif 27 <= BMI < 30:
	print('輕度肥胖')
elif 30 <= BMI < 35:
    print('中度肥胖')
else:
	print('重度肥胖')