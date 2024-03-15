#1
name = input('Nhap ten cua ban: ')
print('Ten cua ban la: ')
for n in name:
    print(n)

#2 #3a
print('Cac so le tu 1 den 10 la: ')
sum = 0
for x in range(1, 11):
    if x % 2 == 1:
        sum += x
        print(x)

print('Tong cac so le tu 1 den 10 la: ', sum)

#3b
sum = 0
for x in range(1, 7):
        sum += x
        print(x)

print('Tong cac so tu 1 den 6 la: ', sum)

#4a
dict = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4
}
print('Cac key co o trong dict la: ')
for d in dict.keys():
    print(d)

#4b
print('Cac value co o trong dict la: ')
for d in dict.values():
    print(d)

#4c
print('Cac key - value co o trong dict la: ')
for k, v in dict.items():
    print(k, v)

#5
courses = [131, 141, 142, 212]
names = ['Maths', 'Physics', 'Chem', 'Bio']
data = tuple(zip(courses, names))
print(data)

#6
s = 'jabbawocky'
consonant = "euoaiEUOAI"
SumOfCons = 0
for x in consonant:
    SumOfCons += s.count(x)
    s = s.replace(x, '_')
print(f'Tong so nguyen am: {SumOfCons}')
print(f'Chuoi sau khi cat nguyen am: {s}')

#7
x = -2
y = 3
while True:
    a = int(input("Nhap a: "))
    if (a < x) | (a > y):
        print("Nhap sai, vui long nhap lai!!!")
    else:
        try:
            print(10 / a)
            break
        except ZeroDivisionError:
            print("Khong the chia cho 0!!!")

#8
ages = [23, 10, 80]
names = ['Hoa', 'Lam', 'Nam']
data = list(zip(ages, names))
sorted_data = sorted(data, key=lambda x: x[0])
print(sorted_data)

#9
input_file = open("firstname.txt")
first_name = input_file.read()
input_file.close()
print(first_name)