
# recursive solution
def lcs(str1, str2):
    if str1 == '' or str2 == '':
        return 0
    if str1[-1] == str2[-1]:
        return 1 + lcs(str1[:-1], str2[:-1])
    return max(lcs(str1, str2[:-1]), lcs(str1[:-1], str2))


# recursive with memoization
def lcs_memo(str1, str2, memo):
    if str1 == '' or str2 == '':
        return 0
    if (str1, str2) in memo:
        return memo[(str1, str2)]

    if str1[-1] == str2[-1]:
        memo[(str1, str2)] = 1 + lcs_memo(str1[:-1], str2[:-1], memo)
    else:
        memo[(str1, str2)] = max(lcs_memo(str1, str2[:-1], memo), lcs_memo(str1[:-1], str2, memo))
    return memo[(str1, str2)]


# bottom-up version with tabulation
def lcs_tab(str1, str2):
    tab = {}
    for i in range(len(str1)+1):
        for j in range(len(str2)+1):
            if i == 0 or j == 0:
                tab[(i, j)] = 0
            elif str1[i-1] == str2[j-1]:
                tab[(i, j)] = 1 + tab[(i-1, j-1)]
            else:
                tab[(i, j)] = max(tab[(i, j-1)], tab[(i-1, j)])
    return tab[(len(str1), len(str2))]

if __name__ == '__main__':
    print(lcs('COOL', 'OLW'))
    memo = {}
    print(lcs_memo('COOL', 'OLW', memo))
    print(lcs_tab('COOL', 'OLW'))

