def add_time(start, duration, week = 0):

    st = start.replace(':', '')
    dur = duration.replace(':', '')
    sta = st.split()

    time = int(sta[0])
    add = int(dur)
    day = 0
    
    # AM PM
    if sta[1] == 'PM': 
        ntime = time + add + 1200 

    elif sta[1] == 'AM': 
        ntime = time + add
    
    while ntime > 2400:
        day = day + 1
        ntime = ntime - 2400

    if ntime >= 1200:
        MP = ' PM'
        ntime = ntime - 1200
    else:
        MP = ' AM'
    
    # Make str clean
    nt = str(ntime)
    if len(nt) == 1:
        new_time = ["0", ":", "0", nt[0]]
    elif len(nt) == 2:
        new_time = ["0", ":", nt[0], nt[1]]
    elif len(nt) == 3:
        new_time = [nt[0], ":", nt[1], nt[2]]
    elif len(nt) == 4:
        new_time = [nt[0], nt[1], ":", nt[2], nt[3]]

    # optional week day
    if week != 0:
        if week == 'Monday':
            weekday = 1 + day
        elif week == 'Tuesday':
            weekday = 2 + day
        elif week == 'Wednesday':
            weekday = 3 + day
        elif week == 'Thursday':
            weekday = 4 + day
        elif week == 'Friday':
            weekday = 5 + day
        elif week == 'Saturday':
            weekday = 6 + day
        elif week == 'Sunday':
            weekday = 7 + day
        while weekday > 7:
            weekday = weekday - 7
        
        if weekday == 1:
            weekday = ', Monday'
        elif weekday == 2:
            weekday = ', Tuesday'
        elif weekday == 3:
            weekday = ', Wednesday'
        elif weekday == 4:
            weekday = ', Thursday'
        elif weekday == 5:
            weekday = ', Friday'
        elif weekday == 6:
            weekday = ', Saturday'
        elif weekday == 7:
            weekday = ', Sunday'
    else:
        weekday = ''
        
    # Print results
    if day == 0:
        print("".join(new_time), MP, weekday)
    elif day == 1:
        print("".join(new_time), MP, weekday, "(next day)")
    elif day > 1:
        print("".join(new_time), MP, weekday, "(", day, "days later)")

add_time("3:30 PM", "2:12")
add_time("11:55 AM", "3:12")
add_time("9:15 PM", "5:30")
add_time("11:40 AM", "0:25")
add_time("2:59 AM", "24:00")
add_time("11:59 PM", "24:05")
add_time("8:16 PM", "466:02")
add_time("5:01 AM", "0:00")
add_time("3:30 PM", "2:12", "Monday")
add_time("2:59 AM", "24:00", "Saturday")
add_time("11:59 PM", "24:05", "Wednesday")
add_time("8:16 PM", "466:02", "Tuesday")