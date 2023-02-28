
def add_time(time1, time2, day=False):
    
    if len(time1) == 7:
        if time1[5] == "A":
            minutes = int(time1[0]) * 60 + int(time1[2]) * 10 + int(time1[3])
        else:
            minutes = int(time1[0]) * 60 + int(time1[2]) * 10 + int(time1[3]) + 12 * 60
    else:
        if time1[6] == "A":
            minutes = int(time1[0]) * 600 + int(time1[1]) * 60 + int(time1[3]) * 10 + int(time1[4])
        else:
            minutes = int(time1[0]) * 600 + int(time1[1]) * 60 + int(time1[3]) * 10 + int(time1[4]) + 12 * 60
    if len(time2) == 4:
        minutes = minutes + int(time2[0]) * 60 + int(time2[2]) * 10 + int(time2[3])
    if len(time2) == 5:
        minutes = minutes + int(time2[0]) * 600 + int(time2[1]) * 60 + int(time2[3]) * 10 + int(time2[4])
    if len(time2) == 6:
        minutes = minutes + int(time2[0]) * 6000 + int(time2[1]) * 600 + int(time2[2]) * 60 + int(time2[4]) * 10 + int(time2[5])
    
    print(minutes)
    if day:
        day_list = ["Monday", "Tuesday", "Wednsday", "Thursday", "Friday", "Saturday", "Sunday"]
        counter = -1
        while day_list[counter] != day:
            counter = counter + 1
            minutes = minutes + 1440    
    
    days = (minutes - minutes % 1440) / 1440
    hours = ((minutes - 1440 * days) - (minutes - 1440 * days) % 60) / 60
    rest_minutes = minutes - days * 1440 - hours * 60
    AMPM = "AM"
    if hours > 12:
        AMPM = "PM"
        hours = int(hours) - 12
    
    
    print(minutes)
    print(hours)
    print(days)
    print(rest_minutes)
    hours_result = str(hours)
    minutes_result = str(int(rest_minutes))
    if len(minutes_result) < 2:
        minutes_result = "0" + minutes_result
    
    day_result = str(day_list[int(days) - 1])
    result = hours_result + ":" + minutes_result + " " + AMPM + ", " + day_result
    print(result)
    if day: return result

add_time("11:30 AM", "2:32", "Friday")


        #print(day_list[int(days) - 1]) #next day