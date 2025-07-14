c=input("Enter a Character")
def check_letter(c):
    if c.strip().lower() in ['a','e','i','o','u']:
       print("It is a VOWEL")
    else:
        print("It is a CONSONANT")
check_letter(c)