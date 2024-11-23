# 1--wap to check whether given number is poistive or negative or netueral--
# num=int(input('Enter the no : '))
# if num==0:
#     print('Netural')
# elif num>0:
#     print('Positive')
# else:
#     print('Negative')

# 2--wap to check whether students is belongs to 1-qspiders or 2-jspiders or 3-pyspiders or 4-prospiders based on batch code--
# batchcode=input('Enter the batch code : ')
# if batchcode[:2:].lower()=='py':
#     print('pyspider')
# elif batchcode[:2:].lower()=='qs':
#     print('qspider')
# elif batchcode[:2:].lower()=='js':
#     print('jspider')
# elif batchcode[:2:].lower()=='pr':
#     print('prospider')
# else:
#     print('invalid batch code')

# 3--wap to check given charaacter is upper or lower or number --
# ch=input('Enter the Character : ')
# if ch.isupper():
#     print('upper')
# elif ch.islower():
#     print('Lower')
# elif ch.isdigit():
#     print('Digit')
# elif ch.isalnum():
#     print('special character')
# else:
#     print('Invalid character')

# 4--wap to check no divisible by 3 and 5 print(Fizzbuzz) and no divisibe by 5 ony print(fizz) no divisible by 3 only print(buzz)no not divisible by 3 and 5 print not divisible by both 3 and 5--
# num=int(input('Enter the no : '))
# if num%3==0 and num%5==0:
#     print('FizzBuzz')
# elif num%3==0:
#     print('Fuzz')
# elif num%5==0:
#     print('Buzz')
# elif num%3 !=0 and num%5 !=0:
#     print('not divisible by both 3 and 5')
# else:
#     print('invalid no ')

# 5--wap to welcome the tourist based on the city he entered--
# ch=input('Enter  the state : ').upper()
# city= {'TN': {1:'chennai',2: 'madurai', 3:'salem'},
# 'AP':{'tirupathi','vizag','nellore'},
# 'KA':{'bangalore','mysore','coorgi'}}
#
# if ch in  'TN':
#     print('தமிழகத்திற்கு வரவேற்கிறோம😊😊..')
# elif ch in 'AP':
#     print('ఆంధ్ర ప్రదేశ్ కు స్వాగతం 😊😊 ')
# elif ch in 'KA':
#     print('ಕರ್ನಾಟಕಕ್ಕೆ ಸ್ವಾಗತ 😊😊')
# else:
#     print('invalid city')

# 6--find the largest of three numbers--
# no1=int(input('enter no 1 :'))
# no2=int(input('enter no 2 :'))
# no3=int(input('enter no 3 :'))
#
# if no1>=no2 and no1>=no3:
#     print(f'{no1} is greater')
# elif no2>=no1 and no2>=no3:
#     print(f'{no2} is greater')
# else:
#     print(f'{no3} is greater ')

# 7--grade a student based on marks if mark is 50-70 =>c and 70-80 =>b and 80-90=>a and 90-100=>a+
# mark=int(input('Enter the mark : '))
# if 50<=mark<=70:
#     print('Grade C')
# elif 70<=mark<=80:
#     print('Grade B')
# elif 80<=mark<=90:
#     print('Grade A')
# elif 90<=mark<=100:
#     print('Grade A+')
# else:
#     print('Invalid Grade')

# 8--categorize the agr group <10 child and <18 adult and <30 man >30 old
# age=int(input('Enter the age : '))
# if age<10:
#     print('Child')
# elif age<=18:
#     print('Adult')
# elif age<30:
#     print('Man')
# else:
#     print('old')

# 9--determine the day od the week 1-mon 2-tues 3-wed 4-thur 5-fri-6-sat-7-sun--
# week=int(input('Enter the week : '))
# if week==1:
#     print('Monday')
# elif week==2:
#     print('Tuesday')
# elif week==3:
#     print('Wednesday')
# elif week==4:
#     print('Thursday')
# elif week==5:
#     print('Friday')
# elif week==6:
#     print('Saturday')
# elif week==7:
#     print('Sunday')
# else:
#     print('No Week Day')

# 10--wap to check whether given no is single digit or double or three--
# num=int(input('Enter the number : '))
# if num>=-9 and num<=9:
#     print('Single Digit')
# elif num>=-99 and num<=99:
#     print('Double Digit')
# elif num>=-999 and num<=999:
#     print('Three Digit')
# else:
#     print('Invalid')