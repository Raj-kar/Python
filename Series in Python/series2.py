# 1+(1/2)+(1/3)+(1/4)...(1/n) -> harmonic series !

num = int(input("Enter a range :: "))
sum = 0

for i in range(1,2):
    for j in range(i, num+1):
        # print(f"{i}/{j}")
        sum += i/j

print(sum)