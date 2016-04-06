def multiplicativeInverse(a, mod):
		if a%mod ==0:
			return 0,1
		x,y = multiplicativeInverse(mod, a%mod)
		temp = x
		x = y
		y = temp - (a/mod)*y
		return x,y


fp = open("N_common","r")
N_str = fp.read()
fp.close()
N = int(N_str)

a,b = multiplicativeInverse(5,N)
if a<0:
	a=a+N
print a


fp = open("blind_key","wb")
fp.write(str(a))
fp.close()

