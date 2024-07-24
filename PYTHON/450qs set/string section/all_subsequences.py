def all_subsequence(inp,opt):
    # print(len(inp))
    if len(inp)==0:
        print(opt,end=' ')
        return
    all_subsequence(inp[1:],opt+inp[0])
    # print('gap')
    all_subsequence(inp[1:],opt)
inp = "abcd"
opt = ""

all_subsequence(inp,opt)