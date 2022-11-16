from Crypto.Random.random import getrandbits
import base64
import operator

t = int(input("How many test?  "))
n = int(input("How many bits?  "))
while t > 0:
    print("str" + str(t) + ": " + base64.b64encode(str(getrandbits(n)).encode()).decode())
    t -= 1

message = input("Lets encrypt this: ")
m_len = len(message.encode())

m_bits = m_len * 8
one_time_key_i = getrandbits(m_bits)
message_i = int.from_bytes(message.encode(),"big")
print("key: " + base64.b64encode(str(one_time_key_i).encode()).decode())
#print("message: " + base64.b64encode(str(message_i).encode()).decode())

ciphertext_i = message_i ^ one_time_key_i
print("ciphertext: " + base64.b64encode(str(ciphertext_i).encode()).decode())

deciphertext_i = ciphertext_i ^ one_time_key_i
print("deciphertext: " + deciphertext_i.to_bytes(m_len,"big").decode())
