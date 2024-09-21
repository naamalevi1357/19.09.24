# start

num: int = int(input(" number : "))
for i in range(1, num + 1, 2):
    for i in range(1, i):
        print(i, end=" ")
    print()

for i in range(num - 1, 1, -2):
    for i in range(1, i):
        print(i, end=" ")
    print()

# stop
