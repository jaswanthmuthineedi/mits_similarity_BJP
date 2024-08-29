def hamming_distance(str1, str2):
    if len(str1) < 3 or len(str2) < 3:
        return "Input string length must be atleast 3"
    if len(str1) != len(str2):
        return "Strings must be of equal length"
    distance = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            distance += 1

    return distance