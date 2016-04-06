def modular_pow(base, exponent, mod):

	if exponent==0:
		return 1
	res=1
	while exponent > 0:
		if exponent & 1:
			res=(res*base)%mod
		exponent = exponent>>1
		base = (base*base)%mod
	return res


fp = open("Public_key","r")
public_key_str = fp.read()
fp.close()
public_key = int(public_key_str)


fp = open("N_common","r")
N_str = fp.read()
fp.close()
N = int(N_str)

fp = open("real_fake","r")

encryptedMsg=int(fp.read())

fp.close()

decryptedMsg = modular_pow(encryptedMsg,public_key,N)

print decryptedMsg
