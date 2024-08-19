def  all_subsequences(inp,opt):
    if len(inp) == 0:
        print(opt,end=' ')
        return
    all_subsequences(inp[1:],opt+inp[0])
    all_subsequences(inp[1:],opt)

all_subsequences('abc','')