f = open("input1.txt")
lines = f.readlines()

numbers = list(map(int, lines))

j = 0
number = []

for i in range(len(numbers)):
    if(i+2 == len(numbers)):
        break
    
    number.insert(j,numbers[i])
    number[j] += numbers[i+1]
    number[j] += numbers[i+2]

    j += 1


decrease = 0
increase = 0


for i in range(len(number)):

    if(i == len(number)-1):
        break

    if(number[i+1] < number[i]):
        decrease += 1

    if(number[i+1] > number[i]):
        increase +=1



print(increase)


