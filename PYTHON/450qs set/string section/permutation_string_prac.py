def permutation_string(str,i=0):
    n = len(str)
    if i == n:
        print(''.join(str))
    for j in range(i,n):
        words = [c for c in str]
        words[i],words[j]=words[j],words[i]
        permutation_string(words,i+1)
permutation_string('abc',0)