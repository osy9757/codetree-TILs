from itertools import combinations

def max_comb(nums, n):
    for i in range(n,1,-1):
        for comb in combinations(nums,i):
            num_list = list(comb)
            while True:
                sum_num = 0
                for num in num_list:
                    sum_num += num%10
                if sum_num >= 10:
                    break
                num_list = [num // 10 for num in num_list]
                if sum(num_list) == 0:
                    return len(list(comb))

n = int(input())
nums = [int(input()) for _ in range(n)]

print(max_comb(nums,n))