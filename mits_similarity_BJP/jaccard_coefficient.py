def jaccard_coefficient(a, b):
    if len(a) < 3 or len(b) < 3:
        return "Input String Size must be atleast 3"
        # string error message if length is less than 3
    set1, set2 = set(a), set(b)
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))

    return float(intersection) / union