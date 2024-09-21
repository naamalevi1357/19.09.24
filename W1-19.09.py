# start
best_record: float = 0
result_name: str = ""
record_men: float = 6.23
mona: float = 0
result_high: float = 0
sum_result: float = 0
max_record = None
for i in range(7):
    result_high: float = float(input("result_high :"))
    if result_high < 5.80:
        continue
    if result_high >= 5.80:
        mona += 1
        sum_result += result_high
        if best_record < result_high:
            best_record = result_high
        if result_high > record_men:
            max_record = result_high
            result_name: str = str(input("name "))
print(f" result_good  : {mona}   ")
print(f"average {sum_result / result_high} ")
print(f" high most result {best_record}")
if max_record:
    print(f" name sportsman {result_name}  and  {max_record}")
else:
    print("None")

# stop
