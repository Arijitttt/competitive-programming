def counting_vallys(steps,path):
    vally = 0
    sea_level =current_level= 0
    for direction in path:
        if direction == 'U':
            current_level += 1
        elif direction == 'D':
            current_level -= 1
    if sea_level==current_level :
        vally += 1
    return vally
steps = 8
path = 'UDDDUDUU'
print(counting_vallys(steps,path))