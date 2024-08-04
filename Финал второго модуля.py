wan_numbers = int(input())
chisla = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
password = (str())
a = 0
b = wan_numbers
for i in range(1, 20):
    for j in range(2, 20):
        a = i + j
        b = wan_numbers % a
        if b == 0 and i < j :
            b = (str(i))
            a = (str(j))
            a = (str(b + a))
            password = (str(password + a))
print(password)
