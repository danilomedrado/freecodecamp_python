
#Write a function named add_time that takes in two required parameters and one optional parameter:

#a start time in the 12-hour clock format (ending in AM or PM)
#a duration time that indicates the number of hours and minutes
#(optional) a starting day of the week, case insensitive
#The function should add the duration time to the start time and return the result.

#If the result will be the next day, it should show (next day) after the time. 
#If the result will be more than one day later, it should show (n days later) after the time, where "n" is the number of days later.

#If the function is given the optional starting day of the week parameter, then the output should display the day of the week of the result. 
#The day of the week in the output should appear after the time and before the number of days later.

def add_time(start, duration, day_of_the_week=''):
    #hour_start = int(start.split(':')[0])
    #min_start = int(start.split(':')[1].split(' ')[0])
    #start_period = start.split(':')[1].split(' ')[1]

    # Parsing start time
    start_hour, rest = start.split(':')
    start_min, start_period = rest.split(' ')
    start_hour, start_min = int(start_hour), int(start_min)

    # Parsing duration
    duration_hour, duration_min = map(int, duration.split(':'))
    #hour_duration = int(duration.split(':')[0])
    #min_duration = int(duration.split(':')[1])

    new_hour = start_hour + duration_hour
    new_min = start_min + duration_min

    #print ('1', 'new_hour', new_hour, 'new_min', new_min, 'start_period', start_period)

    if new_min >= 60:
        new_hour += 1
        new_min -= 60
    
    number_of_days = new_hour // 24
    new_hour = new_hour % 24

    #print ('2', 'new_hour', new_hour, 'new_min', new_min, 'start_period', start_period, 'number_of_days', number_of_days)

    if new_hour >= 12:
        if new_hour > 12:
            new_hour -= 12
        if start_period == 'AM':
            start_period = 'PM'
        else:
            start_period = 'AM'
            number_of_days += 1
    
    #print ('3', 'new_hour', new_hour, 'new_min', new_min, 'start_period', start_period, 'number_of_days', number_of_days)

    
    if number_of_days > 1:
        per = f'({number_of_days} days later)'
    elif number_of_days == 1:
        per = '(next day)'
    else:
        per = ''
    
    new_min = str(new_min).rjust(2,'0')

    new_day = ''
    if day_of_the_week:
        days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        index = (days_of_week.index(day_of_the_week.capitalize()) + number_of_days) % 7
        new_day = f', {days_of_week[index]}'

    new_time = f'{new_hour}:{new_min} {start_period}{new_day} {per}'
    
    #print ('new_hour', new_hour, 'new_min', new_min, 'start_period', start_period, 'number_of_days', number_of_days)
    return new_time

print('3:30 PM', '2:12')
print(add_time('3:30 PM', '2:12'), '\n')

print('11:55 AM', '3:12')
print(add_time('11:55 AM', '3:12'), '\n')

print('2:59 AM', '24:00')
print(add_time('2:59 AM', '24:00'), '\n')

print('8:16 PM', '466:02')
print(add_time('8:16 PM', '466:02'), '\n')

print('3:30 PM', '2:12', 'Monday')
print(add_time('3:30 PM', '2:12', 'Monday'), '\n')

print('11:59 PM', '24:05', 'Wednesday')
print(add_time('11:59 PM', '24:05', 'Wednesday'),'\n')

print('2:59 AM', '24:00', 'saturDay')
print(add_time('2:59 AM', '24:00', 'saturDay'), '\n')

print('8:16 PM', '466:02', 'tuesday')
print(add_time('8:16 PM', '466:02', 'tuesday'))