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


fp = open("blind_key","r")
blind_key_str = fp.read()
fp.close()
blind_key = int(blind_key_str)


fp = open("N_common","r")
N_str = fp.read()
fp.close()
N = int(N_str)

fp = open("encrypted_msg","r")

message_str = fp.read()
fp.close()

encryptedMsg=int(message_str)


decryptedMsg = (encryptedMsg*blind_key)%N
#decryptedMsg = "".join( chr(i) for i in decryptedMsg_list )
fp = open("real_fake","wb")
fp.write(str(decryptedMsg))
fp.close()

print decryptedMsg
