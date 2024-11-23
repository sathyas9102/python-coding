# 1 -------------wap to check given no is even or odd .If it is even print square number else print cube of the number..----
from struct import pack_into

# num=int(input('Enter the No : '))
# if num%2==0:
#     print(num**2)
# else:
#     print(num**3)

# 2--wap to check given single char is captial letter o not .If it is captial letter convert to lower case else convert into uppercase.---

# ch=input('Enter the Character : ')
# if 'A' <=ch <='Z':
#     print(chr(ord(ch)+32))
# else:
#     print(chr(ord(ch)-32))
#                                    or
# ch=input('Enter the Character : ')
# if ch.isupper():
#     print(chr(ord(ch) + 32))
# else:
#     print(chr(ord(ch)-32))

# 3--------wap to check whether given number is multple of 2 if it is multple of 2 make them it square else make it cube----

# num=int(input('Enter the No : '))
# if num%2==0:
#     print(num**2)
# else:
#     print(num**3)


# 4----wap to display if the entered age is greater than or equal to 18 print your are eligible to vote else not eligible

# Age=int(input('Enter the age : '))
# if Age>0:
#     if 0<=Age<18:
#         print('Your Not Eligible to vote..')
#     else:
#          print('your are eligible to vote...')
# else:
#     print('invalid age..')

# 5-- wap to display hiii if the userr entered no is positive else print bye  and zero is netural

# num=int(input('enter the no : '))
# if num==0:
#     print('netural')
# elif num>1:
#     print('Hii')
# else:
#     print('bye')

# 6--wap to print the given character string first letter ascii value is even o odd (without type casting)---
# ch=input('enter the string : ')
# s=ord(ch[0])
# print(s)
# if s%2==0:
#     print('even..')
# else:
#     print('odd')

# 7--wap to check given character is a special character o not

# ch=input('enter the character : ')
# if ch.isalnum():
#     print('No special character')
# else:
#     print('special character')

# 8--wap to convert the middle letter into upper if it is lower else print first letter of the word.
# ch=input('Enter the character : ')
# s=len(ch)//2
# if ch[s].islower():
#     print(ch[s].upper())
# else:
#     print(ch[0])

# 9--wap to check if the given number is zero--
# num=int(input('Enter the No : '))
# if num==0:
#     print('The Given Number is Zero ')
# else:
#     print('The Given Number is Not Zero')

# 10--wap to check whether the first number is divisible by the second number--
# num1=int(input('Enter the Number 1 : '))
# num2=int(input('Enter the Number 2 : '))
# if num1%num2 ==0:
#     print('It is Divisible')
# else:
#     print('It is not Divisible')


# 11--wap to check if a character entered by the user is  start with vowel
# ch=input('Enter the character : ')
# if ch[0] in 'aeiouAEIOU':
#     print('It is Vowel')
# else:
#     print('It is Not Vowel')

# 12--wap to convert first letter of the word into upper if it's starting with lower and vowel--
#
# ch=input('Enter the character : ')
# if ch[0] in 'aeiouAEIOU':
#     if ch[0].islower():
#         print(ch[0].upper())
#     else:
#         print(ch[0].lower())
# else:
#     print('Invalid character ')

# 13--wap to check if a number entered by the user is multiple of 5--

# num=int(input('Enter the number :'))
# if num%5==0:
#     print('Number is Divisible ')
# else:
#     print('Number is Not Divisibe')

# 14--wap to check the given number is divisible by  2 and 3--

# num=int(input('Enter the number : '))
# if num%2==0 and num%3==0:
#     print('Number Divisible by both 2 and 3')
# else:
#     print('Number is Not Divisible by both 2 and 3')

# 15--wap to check whether the given string is palindrome--(palindrome means if you read from reverse also the name should be same)--

# ch=input('Enter the character : ')
# if ch==ch[::-1]:
#     print('It Is Palindrome')
# else:
#     print('It Is Not Palindrome')


# 16--wap to check whether the given number is palindrome or not--
# num=int(input('Enter the Number : '))
# s=str(num)
# if num==s[::-1]:
#     print('It is palindrome Number')
# else:
#     print('It is not palindrome number ')

# 17--wap ask the user to enter the number and prints whether it is within the range of 1 to 100--
# num=int(input('Enter the number : '))
# if 1 <=num<=100:
#     print('Number within the range')
# else:
#     print('Number is not within the range')

# 18--wap asks the user to enter three sides of a triangle and prints whether it is an equilateral triangle--

# a=int(input('Enter the Number 1: '))
# b=int(input('Enter the Number 2: '))
# c=int(input('Enter the Number 3: '))
#
# if a==b==c:
#     print('it is equal')
# else:
#     print('not equal')

# 19--wap to check whether middle of a list in a single digit or not--
# a=[1,22,3333,44444,5,555555,666666,777777]
# b=len(a)//2
# if a[b]<=9:
#     print('it is single digit')
# else:
#     print('it is not a single digit')

# 20--wap to check whether given string is ending with vowel or consonant if it is ending with vowel print reverse of the word elsee print as it is--
# ch=input('Enter the character : ')
# if ch[-1] in 'AEIOUaeiou':
#     print(ch[::-1])
# else:
#     print(ch)

# 21--wap to check whethe userr given year is leapyear or not
# num=int(input('Enter the year : '))
# if num%4==0 or num%400 ==0 and num%100 !=0:
#     print(f'{num} is leap year')
# else:
#     print(f'{num} is not a leap year')

# 22--wap to check whether students belongs to pyspider or qspider or jspider based on the batch code

# ch=input('enter the batch code : ')
# if ch[:2:1]=='py':
#     print(f'{ch} is belongs to pyspiders')
# elif ch[:2:1]=='qs':
#     print(f'{ch} is belongs to qspiders')
# elif ch[:2:1]=='js':
#     print(f'{ch} is belongs to jspiders')
# else:
#     print(f'{ch} is invalid batch code')

# 23--WAP to check given no is positive o not if positive print happy else print sad

# num=int(input('enter the no : '))
# if num>0:
#     print('happy')
# elif num==0:
#     print('netural')
# else:
#     print('sad')

# 24--wap to add the 'hello' to a list if the list is having even length else add 'bye'

# lst=[1,2,3,'sathya',7777,'anitha','divya']
# s=len(lst)
# print(s)
# if s%2==0:
#     lst.append('hello')
#     print(lst)
# else:
#     lst.append('bye')
#     print(lst)


# 25--wap to check given no is palindrome or not if it is palindrome add the string into a set--
# num=int(input('enter the no : '))
# s={11,22}
# a=str(num)
#
# if num==a[::-1]:
#     s.add(int(a))
#     print(s)
# else:
#     print('hello')

# 26--wap to check given character is special or not--
# ch=input('Enter the character : ')
# if ch.isalnum():
#     print('No special character ')
# else:
#     print('Special character')

# 27--wap to check whether given string having character b at even index if it is present at even index print first half of the string in reverse else second half in the reverse order--
# ch=input('Enter the string : ')
# if ch.find('b')%2==0:
#     print(ch[:len(ch)//2:] [::-1])
# else:
#     print(ch[len(ch)//2 : :] [::-1])