# weeks = {'monday':1, 'tuesday':2, 'wednesday':3, 'thursday':4, 'friday':5, 'saturday':6, 'sunday':7}
weeks = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
a = 'Tuesday'
idx_day = weeks.index(a.lower())
c = None
add_day = 20
print(a)

i = 0
while add_day > 0:
    if idx_day >= 6:
        idx_day = 0
    else:
        idx_day += 1
    print("Hari ke-{}: {}".format(i+1, weeks[idx_day].title()))
    i += 1
    add_day -= 1

print("Our Promise:", weeks[idx_day].title())

    # temp_dur_hour = list()
    # if dur_hour > 12:
    #     times = dur_hour
    #     while times > 12:
    #         temp_dur_hour.append(12)
    #         times -= 12
    #     temp_dur_hour.append(times)
    # else:
    #     temp_dur_hour.append(dur_hour)

    # for hour in temp_dur_hour:
    #     new_hour += cur_hour + hour
    #     # print("Current new hour:", new_hour)
    #     cur_hour = 0
    #     if new_hour >= 12:
    #         # print('{} >= 12'.format(new_hour))
    #         if cur_abbr == 'PM':
    #             # print('{} == PM'.format(cur_abbr))
    #             new_day += 1
    #             if new_hour > 12:
    #                 new_hour -= 12
    #             cur_abbr = 'AM'
    #         else:
    #             # print('{} = AM'.format(cur_abbr))
    #             if new_hour > 12:
    #                 new_hour -= 12
    #             cur_abbr = 'PM'