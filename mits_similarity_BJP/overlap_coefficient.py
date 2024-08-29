def overlap_coefficient(a, b):
    if len(a) < 3 or len(b) < 3:
        return "Input string Size must be atleast 3"
        # string error message if length is less than 3
    set1, set2 = set(a), set(b)
    intersection = len(set1.intersection(set2))
    minn = min(len(set1), len(set2))

    return float(intersection) / minn