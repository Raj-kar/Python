# generators can hold the last value. and from the last value, it's starts iterating
def gen_counter(val):
    count = 1
    while count <= val:
        yield count  # yield mean execution hold here, when we next time call, it's from here
        count += 1
    print()


counter = gen_counter(5)
for i in counter:
    print(i, end=" ")  # 1 2 3 4 5

counter = gen_counter(5)
print(next(counter))  # 1
for i in counter:  # we already iterate one time, so next time loop will run from 2
    print(i, end=" ")  # 2 3 4 5

for i in counter:
    print(i, end=" ")  # No output, because we already iterate over counter.
