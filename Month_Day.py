# Author: Crystal Frye


print("Please state the month and day to find the season")
print("")
print("Month:")

input_month = input()

print("Day:")
input_day = int(input())

###USE IN

months = ['January', 'February', 'March','April','May','June','July','August','September','October','November','December']
spring = ['March', 'April', 'May', 'June']
summer = ['June','July','August','September']
autumn = ['September','October','November', 'December']
winter = ['December','January','February','March']

if input_day < 0:
    print('Invalid')
    if input_day > 31:
        print('Invalid')
if input_month not in months:
    print('Invalid')

if input_month == ('September' or 'April' or 'June' or 'November') and input_day > 30:
    print('Invalid')
elif input_month == 'February' and input_day > 29:
    print('Invalid')
    if input_month == ('January' or 'March' or 'May' or 'July' or 'August' or 'October' or 'December') and input_day > 31:
        print('Invalid')

if input_month == ('January' or 'February'): # I parsed out what months would be which season regardless of day
    print('Winter')
elif input_month == ('April' or 'May'):
    print('Spring')
elif input_month == ('July' or 'August'):
    print('Summer')
elif input_month == ('October' or 'November'):
    print('Autumn')
if input_month == spring[0]:  # here is where I defined the cusp of spring/winter depending on the March date
    if input_day >= 20:
        print('Spring')
    else:
        print('Winter')
if input_month == summer[0]: # here is where I defined the cusp of spring/summer depending on the June date
    if input_day <= 20:
        print('Spring')
    else:
        print('Summer')
if input_month == autumn[0]: # here is where I defined the cusp of autumn/summer depending on the September date
    if input_day >= 22:
        print('Autumn')
    else:
        print('Summer')
if input_month == winter[0]: # here is where I defined the cusp of winter/autumn depending on the December date
    if input_day >= 21:
        print('Winter')
    else:
        print('Autumn')
