while True:
		print('Введите 1 для расчета массы на земле/луне')
		print('Введите 2 для расчета высоты прыжка на земле/луне')
		vibor = int(input('>>>')) 		
		if vibor ==1:
			 print('введите 1 для расчета массы на луне')
			 print('Введите 2 для расчета массы на земле')
			 planets = int(input('>>> '))
			 if planets == 1:
			 	mass_earth = float(input('Введите массу на земле '))
			 	print(mass_earth / (9.8 / 6),' килограмм')
			 elif planets == 2:
			 	mass_moon = float(input('Введите массу на луне '))
			 	print(mass_moon * (9.8/6))
		elif vibor == 2:
			print('введите 1 для расчета высоты прыжка на луне')
			print('Введите 2 для расчета высоты прыжка на земле')
			planets = int(input('>>> '))
			if planets == 1:
				jump_earth = float(input('Введите высоту прыжка на земле'))
				print(jump_eath / (9.8/6))
			elif planets ==2:
				jump_moon = float(input('Введите высоту прыжка на луне'))
				print(jump_moon * (9.8/6))

			

