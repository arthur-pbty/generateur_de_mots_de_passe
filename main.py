import string
import random

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

password = generate_password(int(input("Quelles taille pour votre mot de passe voulez vous ? ")))
print(f"Votre mot de passe : {password}")
