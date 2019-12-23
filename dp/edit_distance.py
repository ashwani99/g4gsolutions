# https://www.geeksforgeeks.org/edit-distance-dp-5/

def edit_distance_recursive(string, other, string_len, other_len):
    if string_len == 0:
        return other_len
    if other_len == 0:
        return string_len

    if string[string_len-1] == other[other_len-1]:
        return edit_distance_recursive(string, other, string_len-1, other_len-1)

    return 1 + min(edit_distance_recursive(string, other, string_len-1, other_len),
               edit_distance_recursive(string, other, string_len, other_len-1),
               edit_distance_recursive(string, other, string_len-1, other_len-1))


def edit_distance(string, other):
    string_len = len(string)
    other_len = len(other)
    table = [[0]*(string_len+1) for _ in range(other_len+1)]

    for i in range(other_len+1):
        for j in range(string_len+1):
            if i == 0:
                table[i][j] = j
            elif j == 0:
                table[i][j] = i
            elif other[i-1] == string[j-1]:
                table[i][j] = table[i-1][j-1]
            else:
                table[i][j] = 1 + min(table[i-1][j],
                                      table[i][j-1],
                                      table[i-1][j-1])
    
    return table[other_len][string_len]
    

if __name__ == '__main__':
    string1 = "ashwxesadasdasdas"
    string2 = "ashwxe"
    print(edit_distance_recursive(string1, string2, len(string1), len(string2)))
    print(edit_distance(string1, string2))
