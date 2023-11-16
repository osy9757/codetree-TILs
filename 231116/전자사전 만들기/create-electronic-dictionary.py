def binary_search(array, prefix):
    left, right = 0, len(array) - 1
    while left <= right:
        mid = (left + right) // 2
        if array[mid].startswith(prefix):
            if mid == 0 or not array[mid - 1].startswith(prefix):
                return mid
            right = mid - 1
        elif array[mid] < prefix:
            left = mid + 1
        else:
            right = mid - 1
    return -1

N, T = map(int, input().split())
words = [input() for _ in range(N)]
sorted_words = sorted(words)

for _ in range(T):
    pass_num, search_word = map(str, input().split())
    pass_num = int(pass_num)
    
    start_index = binary_search(sorted_words, search_word)
    if start_index == -1 or start_index + pass_num - 1 >= len(sorted_words) or not sorted_words[start_index + pass_num - 1].startswith(search_word):
        print(-1)
    else:
        print(words.index(sorted_words[start_index + pass_num - 1]) + 1)