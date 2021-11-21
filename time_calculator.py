import re


def add_time(start, duration, current_day=None):
    weeks = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    cur_hour = int(re.findall('(^.+?):', start)[0])
    cur_minutes = int(re.findall(':(\S.)', start)[0])
    cur_abbr = re.findall('\s(\S.)', start)[0]
    
    dur = duration.split(':')
    dur_hour = int(dur[0])
    dur_minutes = int(dur[1])

    new_day = 0
    new_hour = 0
    new_minutes = 0
    new_minutes = cur_minutes + dur_minutes
    if new_minutes >= 60:
        dur_hour += 1
        new_minutes -= 60
    
    while dur_hour >= 0:
        if dur_hour >= 12:
            temp_hour = 12
            dur_hour -= 12
        else:
            temp_hour = dur_hour
            dur_hour = -1
        new_hour += cur_hour + temp_hour
        cur_hour = 0
        if new_hour >= 12:
            if cur_abbr == 'PM':
                new_day += 1
                if new_hour > 12:
                    new_hour -= 12
                cur_abbr = 'AM'
            else:
                if new_hour > 12:
                    new_hour -= 12
                cur_abbr = 'PM'

    next_day = ''
    if new_day == 1:
        next_day = ' (next day)'
    elif new_day > 1:
        next_day = ' ({} days later)'.format(new_day)

    new_minutes = str(new_minutes)
    if len(new_minutes) == 1:
        new_minutes = '0{}'.format(new_minutes)

    day = ''
    if current_day is not None:
        cur_day = current_day.lower()
        idx_day = weeks.index(cur_day.lower()) 
        add_day = new_day
        while add_day > 0:
            if idx_day >= 6:
                idx_day = 0
            else:
                idx_day += 1
            add_day -= 1
        day = ', {}'.format(weeks[idx_day].title())
        
    new_time = "{}:{} {}{}{}".format(new_hour, new_minutes, cur_abbr, day, next_day).strip()

    return new_time