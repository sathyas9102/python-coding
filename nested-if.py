# 1--wap to check whether given no is even or odd befoe that check whether given no is positive or negative
import numbers
# num=int(input('Enter the no :'))
# if num>=0:
#     print(f'{num} is positive')
#     if num%2==0:
#         print(f' {num} even')
#     else:
#         print(f'{num} odd')
# else:
#     print(f'{num} is negative')

# 2--wap to find second heighest number among three

# num1=int(input('Enter the number 1 :'))
# num2=int(input('Enter the number 2 :'))
# num3=int(input('Enter the number 3 :'))
# if num1>num2 and num1>num3:
#     print(f'{num1} is greater')
#     if num2>num3:
#         print(f'{num2} is second heightest')
#     else:
#         print(f'{num3}  is third heighest')
# elif num2>num1 and num2>num3:
#     print(f'{num2} is heighest')
#     if num1>num3:
#         print(f'{num1} is second heighest')
#     else:
#         print(f'{num3} is third heightest')
# elif num3>num1 and num3>num2:
#     print(f'{num3} is heightest')
#     if num1>num2:
#         print(f'{num1} is second heightest')
#     else:
#         print(f'{num2} is third heightest')
# else:
#   print('invald')

#
# # 3--wap to check the bus book ticket
# # input => stating point endpoint gender adult/child
# # price=> male adult-5 male child-2 female-0
# # station => dic={'vadapalani':1,;arumbakkam' : 2,'koyebedu' : 3 ,'anna nagar' : 4 ,'gunidy' : 5,'tambaram':6}


# dic={'vadapalani':1,'arumbakkam' : 2,'koyebedu' : 3 ,'anna nagar' : 4 ,'gunidy' : 5,'tambaram':6}
# import datetime
# x = datetime.datetime.now()
# start=input('Enter the starting point : ').lower()
# end=input('Enter the ending point : ').lower()
# gender=input('enter the gender : ').lower()
# age=int(input('enter the age : '))
# if gender=='male':
#     if age>=18:
#         price=(dic[end]-dic[start] )*5
#
#         print('-'*30)
#         print(f'{start} : stating point')
#         print(f'{end} : ending point')
#         print(f'Date : {x}')
#         print(f' price : {price} :    gender : {gender}    age :  {age}')
#
#     else:
#         price=(dic[end] - dic[start] )*2
#         print('-' * 10)
#         print(f'{start} : stating point')
#         print(f'{end} : ending point')
#         print(f'Date : {x}')
#         print(f' price : {price} :    gender : {gender}   age :  {age}')
# elif gender=='female':
#     if age >= 18:
#         price = (dic[end] - dic[start]) * 0
#         print('-' * 30)
#         print(f'{start} : stating point')
#         print(f'{end} : ending point')
#         print(f'Date : {x}')
#         print(f' price : {price} :    gender : {gender}    age :  {age}')
#
#     else:
#         price = (dic[end] - dic[start]) * 0
#         print('-' * 30)
#         print(f'{start} : stating point')
#         print(f'{end} : ending point')
#         print(f'Date : {x}')
#         print(f' price : {price} :   gender : {gender}    age :  {age}')
#
# else:
#     if age >= 18:
#         price = (dic[end] - dic[start]) * 4
#         print('-' * 30)
#         print(f'{start} : stating point')
#         print(f'{end} : ending point')
#         print(f'Date : {x}')
#         print(f' price : {price} :   gender : {gender}   age :  {age}')
#
#     else:
#         price = (dic[end] - dic[start]) * 1
#         print('-' * 30)
#         print(f'{start} : stating point')
#         print(f'{end} : ending point')
#         print(f'Date : {x}')
#         print(f' price : {price} :   gender : {gender}    age :  {age}')

#4--wap to manage hotel booking
# 1-single bed room -->per day 500 rupees
# 2-double bed room --> per day 100 rupees


# import datetime
# x=datetime.datetime.now()
# name=input('Enter the Name :  ')
# count=int(input('Hoe many members : '))
# days=int(input('enter the days : '))
# bed=input('Enter the single/double bed room : ').lower()
# if bed=='single':
#     price=days*500
#     print('-'*50)
#     print(f'{name}')
#     print(f'{count} members')
#     print(f'{days} days')
#     print(f'{bed} bed room')
#     print(f'{x}')
#     print(f'price : {price} ')
#     print('-' * 50)
# else:
#     price = days * 1000
#     print('-' * 50)
#     print(f'{name}')
#     print(f'{count} members')
#     print(f'{days} days')
#     print(f'{bed} bed room')
#     print(f'{x}')
#     print('-' * 50)


