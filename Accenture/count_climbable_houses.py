def count_climbable_houses(house_roofs):
    count  = 0
    for height in house_roofs:
        if height%3 == 0:
            count += 1
    return count
if __name__ == "__main__":
    house_roofs = list(map(int,input('enter the no of house: ').split()))
    print(count_climbable_houses(house_roofs))