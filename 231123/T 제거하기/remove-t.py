def remove_T_from_S(S, T):
    while T in S:
        S = S.replace(T, '', 1)
    return S

S = input()
T = input()
print(remove_T_from_S(S, T))