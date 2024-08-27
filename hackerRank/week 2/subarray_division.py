def subarray_division(inp,opt):
    if len(inp) == 0 :
        print(opt,end=' ')
        return
    subarray_division(inp[1:],inp[0]+opt)
    subarray_division(inp[1:],opt)
inp = 'abcd'
opt = ''
subarray_division(inp,opt)
