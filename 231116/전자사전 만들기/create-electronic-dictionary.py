N, T = map(int, input().split())
words = [input().strip() for _ in range(N)]
indexed_words = sorted((word, i) for i, word in enumerate(words))

def binary_search(prefix, find_last=False):
    left, right = 0, len(indexed_words) - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if indexed_words[mid][0].startswith(prefix):
            result = mid
            if find_last:
                left = mid + 1
            else:
                right = mid - 1
        elif indexed_words[mid][0] < prefix:
            left = mid + 1
        else:
            right = mid - 1
    return result

for _ in range(T):
    k, prefix = input().split()
    k = int(k)

    first = binary_search(prefix)
    last = binary_search(prefix, find_last=True)

    if first == -1 or last - first + 1 < k:
        print(-1)
    else:
        print(indexed_words[first + k - 1][1] + 1)