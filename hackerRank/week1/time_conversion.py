def time_conversion(s):
    temp1 = []
    s1 = s.endswith('PM')
    if s1:
        time = s.split('PM')
        time = time[0]
        #time = int(time)
        time  = time.split(':')
        for value in time:
            temp1.append(int(value))
        if temp1[0] != 12:
            temp1[0]=temp1[0]+12
        # print(temp1)
        converted_time =f'{temp1[0]:02}:{temp1[1]:02}:{temp1[2]:02}PM'
        print(converted_time)
    if 'AM' in s:
        time = s.split('AM')
        time = time[0]
        time  = time.split(':')
        for value in time:
            temp1.append(int(value))
        if temp1[0] == 12:
            temp1[0]=0
        converted_time =f'{temp1[0]:02}:{temp1[1]:02}:{temp1[2]:02}AM'
        print(converted_time)
s ='07:5:54AM'
time_conversion(s)
