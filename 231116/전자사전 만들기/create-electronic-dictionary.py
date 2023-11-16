N, T = map(int, input().split())
words = [input() for _ in range(N)]
indexed_words = [(word, i) for i, word in enumerate(words)]
sorted_indexed_words = sorted(indexed_words, key=lambda x: x[0])

for _ in range(T):
    pass_num, search_word = map(str, input().split())
    pass_num = int(pass_num)
    found = False
    for sorted_word, idx in sorted_indexed_words:
        if sorted_word.startswith(search_word):
            pass_num -= 1
            if pass_num == 0:
                print(idx + 1)
                found = True
                break
    if not found:
        print(-1)