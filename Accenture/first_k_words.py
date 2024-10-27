def first_k_words(s,k):
    words = s.split()
    return ' '.join(words[:k])
if __name__ == '__main__':
    print(first_k_words('kesariya tera mera',2))