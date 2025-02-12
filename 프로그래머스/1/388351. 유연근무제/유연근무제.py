def solution(schedules, timelist, startday):
    answer = 0 
    for i in range(len(schedules)):
        schedules[i] += 10
        time = str(schedules[i])
        if len(time) == 3:
            hour = int(time[:1])
            minute = int(time[1:])

            if minute >= 60: 
                hour += 1
                minute -= 60
            if minute < 10:
                minute = '0' + str(minute)
                time = str(hour) + minute
        
        elif len(time) == 4:
            hour = int(time[:2])
            minute = int(time[2:])
    
            if minute >= 60: 
                hour += 1
                minute -= 60
            if minute < 10:
                minute = '0' + str(minute)
                time = str(hour) + minute
        schedules[i] = int(time)

        print(schedules[i])

        cnt = 0 
        
        for day in timelist[i]:
            startday = startday % 7
            if (startday != 6 and startday != 0) and day <= schedules[i]:
                cnt += 1
            startday += 1
        if cnt == 5:
            answer += 1
    return answer