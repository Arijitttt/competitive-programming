from stack import Stack

def divide_by_two(dec_num):
    s = Stack()

    while dec_num > 0:
        reminder = dec_num%2
        s.push(reminder)
        dec_num = dec_num // 2
    bin_num = ''
    while not s.is_empty():
        bin_num += str(s.pop())

    return bin_num

print(divide_by_two(8))