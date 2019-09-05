'''Program Description:
User enters a message, then the code looks for every letter of the message in alphabet.
Using a user-entered key, the letters change and the message becomes encrypted/decrypted.'''

#store all alphabetic letters in a string(in the correct order
alphabet='abcdefghijklmnopqrstuvwxyz'

#get user's message
message=input('Please enter a message')

'''get the key from the user. 'key' is an integer based on which letters change.
for example:if message entered is 'b', and the key entered is 2, the encrypted message
is going to be 'b'+2='d' '''
key=int(input('Please enter a key'))

#the cenrypted message
secret=""
for i in range(len(message)):
    
    #find letters in the alphabet string
    new_position=alphabet.find(message[i])
    
    #if not found, store the same character in 'secret'
    if new_position==-1:
        secret+=message[i]
        
    #if found, store the encrypted letter in 'secret'
    else:
        secret+=alphabet[(new_position+key)%26]

#if key is a positive number, the message is encrypted, otherwise, it is decrypted   
if key>=0:
    print('The encrypted message is:',secret)
else:
    print('The decrypted message is:',secret)
