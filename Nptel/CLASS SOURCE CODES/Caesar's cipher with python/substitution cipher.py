import string


def encrypt(secret, sub):
    secret_items = {}
    items = secret

    for letter in range(len(items)):
        secret_items[items[letter]] = items[letter - sub]
    return secret_items


def subCipher(msg, sub=1):
    result = ""
    secret_letters = encrypt(string.ascii_letters, sub)
    secret_numbers = encrypt(string.digits, sub)
    secret_punctuation = encrypt(string.punctuation, sub)
    secret_whitespaces = encrypt(string.whitespace, sub)

    for i in msg:
        if i in secret_letters:
            result += secret_letters[i]
        elif i in secret_numbers:
            result += secret_numbers[i]
        elif i in secret_punctuation:
            result += secret_punctuation[i]
        elif i in secret_whitespaces:
            result += secret_whitespaces[i]
        else:
            result += i

    print(result)


msg = "The Indian %$%^^!19 Institute %$%^^!19 of %$%^^!19 Technology Ropar (IIT ROPAR) #! %$%^^!1992819271"

subCipher("HEY THERE")
# GDX
#     SGDQD