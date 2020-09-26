# (1*1) + (2*2) + (3*3) + (4*4) .... (n*n)

num = int(input("Enter a range :: "))
sum = 0

for i in range(1,num+1):
    # print(f"{i}*{i}")
    sum += i*i

print(sum)