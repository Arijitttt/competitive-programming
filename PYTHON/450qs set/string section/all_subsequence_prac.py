def all_subsequence(inp,opt):
    if len(inp) == 0:
        print(opt,end=' ')
        return
    all_subsequence(inp[1:],opt+inp[0])
    all_subsequence(inp[1:],opt)
inp = "abcd"
opt = ""
all_subsequence(inp,opt)