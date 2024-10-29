def cars_dates(arr,date):
    fine = 0
    for num in arr:
        if date % num != 0:
            fine += 250
        else:
            fine += 0
    return fine
print(cars_dates([3,4,1,2],15))