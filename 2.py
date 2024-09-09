term1 = 1
term2 = 2
num = 0
sum = 2 
while num < 4000000:
    num = term1 + term2
    term1 = term2
    term2 = num
    if num % 2 == 0:
        sum += num
print(sum)
