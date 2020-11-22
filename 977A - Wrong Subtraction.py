n_k = input().split()
n,k = int(n_k[0]),int(n_k[1])
for _ in range(k):
	if n % 10 == 0:
		n = n // 10
	else:
		n -= 1
print(int(n))
