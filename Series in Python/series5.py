# display sum of the series [9 + 99 + 999 + 9999 ....] = 111105

num = int(input("Enter a number :: "))
sum = 0

for i in range(1,num+1):
    print("9"*i, end=" ")
    sum += int("9" * i)

print(f"\n {sum}")