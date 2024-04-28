'''
4/27/2024

encryption test
'''
from cryptography.fernet import Fernet

key = Fernet.generate_key()  # Creates a encryption key
fernet = Fernet(key)  # This is the class that encrypts and decrypts messages

test_string = "Test 1 - Armen Jump"
encoded_string = test_string.encode()  # encodes with the default utf-8
encrypted_string = fernet.encrypt(encoded_string)  # encrypts the encoded string
decrypted_string = fernet.decrypt(encrypted_string)  # decrypts the string back into the encoded version
decoded_string = decrypted_string.decode()  # decodes the string back into letters?

for action_list in [
    ['key: ', key],
    ["original: ", test_string],
    ["encoded: ", encoded_string],
    ['encrypted: ', encrypted_string],
    ['decrypted: ', decrypted_string],
    ['decoded: ', decoded_string]
]:
    print(action_list[0], action_list[1])

# writing to a file
key_file = open('testkey.ky', 'w')
key_file.write(key.decode())
key_file.close()

key_file = open('testkey.ky', 'r')
print(key_file.read())
key_file.close()


'''
Sources: 
https://www.geeksforgeeks.org/how-to-encrypt-and-decrypt-strings-in-python/
How to use it
'''

'''
Notes
The encoded version of the string has a b'' on it. is it bit?
https://www.geeksforgeeks.org/effect-of-b-character-in-front-of-a-string-literal-in-python/
it's a byte string

The key is an encoded string and must be converted by decoding it. Because you can't write bytes to a file?
'''