"""
The following problem is from Chapter 6. Try it again, this time using a dictionary whose
keys are the names of the time zones and whose values are offsets from the Eastern time zone.
Write a program that converts a time from one time zone to another. The user enters the time
in the usual American way, such as 3:48pm or 11:26am. The first time zone the user enters
is that of the original time and the second is the desired time zone. The possible time zones
are Eastern, Central, Mountain, or Pacific.
Time: 11:48pm
Starting zone: Pacific
Ending zone: Eastern
2:48am
"""

zones = {'eastern': 0, 'central': -1, 'mountain': -2, 'pacific': -3}

time = input('Time:')
st_zone = input('Starting zone:')
end_zone = input('Ending zone:')


diff = zones[end_zone.lower()] - zones[st_zone.lower()]

am_pm = time[-2:]

hours, minutes = time[:-2].split(':')


hours = int(hours) + diff

if hours > 12:
    hours %= 12
    if am_pm == 'am':
        am_pm = 'pm'
    else:
        am_pm = 'am'

print(str(hours), ':', minutes, am_pm, sep='')
