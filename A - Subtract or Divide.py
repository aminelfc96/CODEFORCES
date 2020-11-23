import time
t = int(input())

for _ in range(t):
	n = int(input())
	m = 0
	while True:
			if 1 < n and n > 3 :
				if n % 2 == 0 and n != 2:
					
					m += 1
					n = n // (n // 2)
					
				elif n % 3 == 0 and n != 3:
					
					m += 1
					n = n // (n // 3)
					
				else:
					
					m += 1
					n -= 1
					
			elif n == 2 or n == 3:
				
				m += 1
				n -= 1
							
			else:
				break
	
	print(m)
