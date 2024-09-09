def check_palindrome(num):
    return str(num) == str(num)[::-1]

pal = 0
for j in range(100, 1000):
    for k in range(100, 1000):
        num = j * k
        if check_palindrome(num):
            pal = num
print(pal)
