def add_time(start, duration, day=False):
    
    #start 
    PMAM_start = start[len(start)-2] + start[len(start)-1]
    startToMinutes = int(start.split(':')[0]) * 60 + int(start[len(start)-5] + start[len(start)-4])
    if PMAM_start == "PM": startToMinutes = startToMinutes + 720    
    #duration 
    durationToMinutes = int(duration.split(':')[0]) * 60 +  int(duration.split(':')[1])    
    minutes = 0
    day_list = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    counter = 0
                
    if day:
        day = day.lower()
        while day_list[counter] != day:
            counter = counter + 1
            minutes = minutes + 1440 
    minutes = minutes + startToMinutes + durationToMinutes    
    nrOfDay = minutes / 1440
    ##to  jeszcze
    hours_result = str(int((minutes - int(nrOfDay) * 1440) / 60))
    minutes_result = str(minutes - int(nrOfDay) * 1440 - int(hours_result) * 60)
    
    PMAM_result = "AM"
    if int(hours_result) >= 12:
        PMAM_result = "PM"
        if int(hours_result) != 12:
            hours_result = int(hours_result) - 12
    
    if int(hours_result) == 0 and PMAM_result == "AM":
            hours_result = int(hours_result) + 12
        
    
    hours_result = str(int(hours_result))
    
    numberOfDays = str(int(nrOfDay) - counter)
    day_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
            
    while nrOfDay > 7:
        nrOfDay = nrOfDay - 7
        
    nameOfDay = ""
    if day:
        nameOfDay = day_list[int(nrOfDay)]
    
    day_result = ""
    rest_results = ""
    
     
    #, Monday
    if nameOfDay != "": day_result = ", " + nameOfDay
    # (2 days later)
    if int(numberOfDays) > 1: rest_results = " (" + numberOfDays + " days later)"
    # (next day)
    if numberOfDays == "1": rest_results = " (next day)" 
    
    if len(minutes_result) == 1: minutes_result = "0" + minutes_result
    new_time = ""
    new_time= hours_result + ":" + minutes_result + " " + PMAM_result + day_result + rest_results
    
    return new_time
