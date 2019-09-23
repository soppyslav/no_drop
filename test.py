from Crypto.Cipher import AES
with open('engwordlist.txt') as f:
   for line in f:
      line = line.ljust(16,'#')
      key = line
      iv = 'aabbccddeeff00998877665544332211'
      ciphertext = '764aa26b55a4da654df6b19e4bce00f4ed05e09346fb0e762583cb7da2ac93a2'
      aes = AES.new(key, AES.MODE_CBC, iv)
      encd = aes.encrypt(line)
      print(encd)
