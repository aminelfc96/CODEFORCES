k_n_w = input().split()
k,n,w = int(k_n_w[0]),int(k_n_w[1]),int(k_n_w[2])
total = 0
for i in range(1,int(w)+1):
	total += k*i	
print(0) if int(n) > int(total) else print(int(total)-int(n))
	
