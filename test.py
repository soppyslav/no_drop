from Crypto.Cipher import AES
with open('engwordlist.txt') as f:
   for line in f:
      key = line
      iv = 'aabbccddeeff00998877665544332211'
      
