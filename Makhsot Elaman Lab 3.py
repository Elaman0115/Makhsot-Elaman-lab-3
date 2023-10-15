'''
"task 1"
n = int(input())
i = 1
while i <= n:
    if i % 2 == 0:
        print(i)
    i += 1
'''

'''
"task 2"
n = int(input())
i = 1
sum = 1
while i <= n:
    sum *= i
    i += 1
print(sum)
'''


'''"task 3"
"a)"
while True:
    n = int(input())
    if n == 42:
        break
    else:
        print ("you entered",n)
"b)"
i = 0
while i < 1000:
    n = int(input())
    if n==42:
        break
    else:
        i+=1
'''

'''"task 4"
s = str(input())
count = 0
for char in s:
    if char == 's' or char == 'S':
        count += 1
if count == 0:
    print("No S or s")
else:
    print(count)
'''

# "task 5"
# number = input("Enter a number: ")
# sum_of_digits = 0
# for digit in number:
#     sum_of_digits += int(digit)
# print("Sum of digits:", sum_of_digits)
#

'''"task 6"
n = int(input())
fst,snd = 0,1
i = 0
while i <= n:
    print(fst,end=' ')
    fbc = fst + snd
    fst = snd
    snd = fbc
    i += 1
'''

'''"task 7"
s = str(input())
print(s[::-1])
'''

"task 8"
# sum_of_odd_numbers = 0
# while True:
#     number = input("Enter a number (or 'done' to exit): ")
#     if number.lower() == "done":
#         break
#     number = int(number)
#     if number % 2 == 0:
#         continue
#     sum_of_odd_numbers += number
# print("Sum of odd numbers:", sum_of_odd_numbers)

"task 9"
# import random
# secret_number = random.randint(1, 100)
# while True:
#     guess = int(input("Guess the number (between 1 and 100): "))
#
#     if guess == secret_number:
#         print("Congratulations! You guessed the number:", secret_number)
#         break
#     elif guess < secret_number:
#         print("Too small! Try again.")
#     else:
#         print("Too large! Try again.")
#

'''"task 10"
s = str(input())
s = s.replace(" ","").lower()
if s == s[::-1]:
    print("Palindrome")
else:
    print("No palindrome")
'''

"task 11"
# n = int(input())
# i = 1
# while i <= n:
#
#     if i%2==0:
#         print()
"task 12"
# n = int(input("Введите число N: "))
# current_number = 2
# print(f"Простые числа от 1 до {n}: ")
# while current_number <= n:
#     is_prime = True
#     divisor = 2
#     while divisor * divisor <= current_number:
#         if current_number % divisor == 0:
#             is_prime = False
#             break
#         divisor += 1
#     if is_prime:
#         print(current_number)
#     current_number += 1
"task 13"
# n = input()
# print(n[::-1])

"task 14"
# def is_prime(num):
#     if num < 2:
#         return False
#     for i in range(2, int(num**0.5) + 1):
#         if num % i == 0:
#             return False
#     return True
# user_input = int(input("Введите число: "))
# while True:
#     if is_prime(user_input):
#         print(f"{user_input} - простое число")
#         break
#     else:
#         print(f"{user_input} не является простым числом.")
#         user_input += 1
#         continue

"task 15"
# text = input("Введите текст для шифрования: ")
# shift = int(input("Введите сдвиг: "))
# encrypted_text = ""
# for char in text:
#     if char.isalpha():
#         shifted_char = chr((ord(char) - 65 + shift) % 26 + 65) if char.isupper() else chr((ord(char) - 97 + shift) % 26 + 97)
#         encrypted_text += shifted_char
#     else:
#         encrypted_text += char
# print("Зашифрованный текст:", encrypted_text)
#



