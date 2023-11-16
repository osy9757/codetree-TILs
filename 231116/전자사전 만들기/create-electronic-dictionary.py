N, T = map(int,input().split())
words = [input() for _ in range(N)]
sorted_words = sorted(words)

for _ in range(T):
    pass_num, search_word = map(str, input().split())
    for sorted_word in sorted_words:
        if sorted_word[:len(search_word)] == search_word:
            if sorted_words.index(sorted_word)+int(pass_num)-1>=len(sorted_words) or sorted_words[sorted_words.index(sorted_word)+int(pass_num)-1][:len(search_word)] != search_word:
                print(-1)
                break
            else:
                print(words.index(sorted_words[sorted_words.index(sorted_word)+int(pass_num)-1])+1) 
                break
    else:
        print(-1)