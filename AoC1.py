import lib

list = lib.input_as_ints("input1.txt")

increase = 0
for i in range(len(list)):
    if list[i] > list[i-1]:
        increase += 1
print(increase)

increase_2 = 0
last_value = list[0] + list[1] + list[2]
for i in range(len(list)-2):
    if list[i] + list[i+1] + list[i+2] > last_value:
        increase_2 += 1
    last_value =list[i] + list[i+1] + list[i+2]

print(increase_2)


