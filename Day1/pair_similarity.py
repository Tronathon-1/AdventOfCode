
# def calculate_list_distance(left_list, right_list):
#     # Sort both lists
#     left_sorted = sorted(left_list)
#     right_sorted = sorted(right_list)

#     # Ensure lists are the same length by padding with 0 if needed
#     max_length = max(len(left_sorted), len(right_sorted))
#     left_sorted += [0] * (max_length - len(left_sorted))
#     right_sorted += [0] * (max_length - len(right_sorted))

#     # Calculate distances between pairs
#     total_distance = sum(abs(left - right) for left, right in zip(left_sorted, right_sorted))

#     return total_distance
from collections import Counter
def pair(a1, a2):

    s= 0
    for i in range(len(a1)):
        min1 = min(a1)
        min2 = min(a2)
        s += abs(min1-min2)
        a1.pop(a1.index(min1))
        a2.pop(a2.index(min2))
    return s

def similarity(a1, a2):

    count = Counter(a2)
    sim = 0

    for i in a1:
        if i in count:
            sim += (i * count[i])

    return sim

def main():
    arr1 = []
    arr2 = []
    with open("in.txt") as file:
        for line in file:
            a, b = line.split()
            arr1.append(int(a))
            arr2.append(int(b))

    file.close()
    tmp1, tmp2 = arr1.copy(), arr2.copy()
    print(pair(tmp1, tmp2))
    res = similarity(arr1, arr2)
    print(res)

if __name__ == "__main__":
    main()
