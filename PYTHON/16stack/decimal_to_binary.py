def highest_gap(num):
    binary_str = bin(num)[2:]
    max_gap = 0
    current_gap = 0
    for chr in binary_str:
        if chr == '1':
            max_gap = max(max_gap, current_gap)
            current_gap = 0
        else:
            current_gap += 1
    return max_gap

        

            

if __name__ == '__main__':
    # num = int(input())
    print(highest_gap(32))