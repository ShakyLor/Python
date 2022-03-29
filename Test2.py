#importing datetime library
from ast import Try
from datetime import datetime, timedelta

#formatting string
first_name = 'Shakya_Dev'
last_name = 'Saha'

output = f'Hello {first_name} {last_name}'
print(output)

current_date = datetime.now()
one_day = timedelta(days=1)

yesterday_date = current_date - one_day

print(f'Current date is : {str(current_date)}')
print(f'Yesterday was :{str(yesterday_date)}')


birthday = input('Please enter your birthday(dd/mm/yyyy):')
#birthday_date = datetime.strptime(birthday,'%d/%m/%Y')

try:
    birthday_date = datetime.strptime(birthday,'%d/%m/%Y')
except ValueError:
    print('wrong date')
finally:
    print('date reading done')
    print(f'Birthday is :{str(birthday)}')

print(f'For Loop\n----------')
for i in range(0,5):
    print(str(i))

print(f'While Loop\n------------')
i=0
while i < 5:
    print(str(i))
    i=i+1

print(f'Complete')

