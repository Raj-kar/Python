email = "raj@google.com"

p1 = email.index('@')
p2 = email.index('.')

print(email[p1+1:p2],end="")
