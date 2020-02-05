import random
"""Find a random number in a password num times"""

num = 3
password = "thisisaveryweakpassword"

"""complicated example"""
choices = []
for x in range(num):
    choice = random.choice(password)
    choices.append(choice)
print("The complicated example", choices)

"""The pythonic way"""
key_keyphase = random.sample(password, num)
print("The pythonic example",key_keyphase)