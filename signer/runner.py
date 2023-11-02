#!/usr/bin/env python
from Crypto.Cipher import AES
from signer import Signer

sgn = Signer()

# You can NOT use the [__sign] or [__verify] function in [signer.py].
# Your solution should work for any value of [key] and therefore should not be a
# hardcoded solution.

# Your solution HERE.

# The final and the only print statement in the program should print out
# "Congratulations, you did it!" after a successful execution.
# There should be no other print statements in the program and you cannot
# hardcode this string to be printed.

# Using a null byte string to Extract aes(aes(b'000...1')) {15 zeros and 1 one} aes->encrypt with key
encCrack = ('\0'*15).encode('utf-8').hex()
ok, primary_Sign = sgn.execute('sign',encCrack)
primary_Sign = primary_Sign[:32] # Extracting the signature only
primary_Sign = bytes.fromhex(primary_Sign)

# Consider String containing 'InterIIT-2023' to get signature
data = 'InterIIT-2023'
data = data + "_"*(16-len(data)%16) # Padding the string to make it 16 bytes
data = data.encode('utf-8')
data = data.hex()
data = bytes.fromhex(data)
Cracked_string = ('\0'*15 +'\1' + '\0'*16).encode('utf-8') + data # modifying string a litlle bit so that a signature could be obtained
# using fact that A xor 0 = A


# Making an arbitary cracked data which will have the same signature as data
# Cracked data is from the intermediate process of sign function of the orginal data (Cracked_string)
# Hence it would have the same signature as orginal data but without 'InterIIT-2023'
CrackedData = Signer.xor(primary_Sign,data)
CrackedData = CrackedData.hex()
ok, get_Sign = sgn.execute('sign',CrackedData)
get_Sign = get_Sign[:32]    # Extracting the signature of cracked data
get_Sign = bytes.fromhex(get_Sign)

# Signature of CrackedData same as Cracked_string
Signed_Data = (get_Sign + Cracked_string).hex()
code,result = sgn.execute('verify',Signed_Data)
print(result)

