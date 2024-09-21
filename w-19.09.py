# start

# num: int =int (input(" number"))

last_positive = None
last_negative = None
positive_count: int = 0
negative_count: int = 0
zero_count: int = 0
sevan_count: int = 0
mona: int = 0
while mona < 10:
    num: int = int(input(" number"))
    mona += 1
    if num == -9999:
        break
    if 1000 <= num or num <= -1000:
        continue
    if num > 0:
        positive_count += 1
        last_positive = num
    if num < 0:
        negative_count += 1
        last_negative = num
    if num == 0:
        zero_count += 1
    if num % 7 == 0:
        sevan_count += 1

else:
    print(f"positive{positive_count} ")
    print(F"negative{negative_count} ")
    print(f" zero {zero_count}")
    print(f"sevan{sevan_count}")
    print(f"last_positive {last_positive}")
    print(f"last_negative {last_negative}")

# stop
