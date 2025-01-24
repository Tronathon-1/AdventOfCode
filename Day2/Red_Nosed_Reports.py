def check_inc_dec(arr):
    test = arr.copy()
    # print("Original list" + str(test))
    re_inc = all(i<j for i, j in zip(test, test[1:]))
    re_dec = all(i>j for i, j in zip(test, test[1:]))
    if re_dec == False and re_inc == False:
        return False
    else:
        return True

def check_difference(arr):
    lst = arr.copy()
    for i, j in zip(lst, lst[1:]):
        if abs(i-j) > 3 or abs(i-j) < 1:
            return False
    return True


def check_safe(res): # res is 2-D
    tmp = {"Safe": 0, "Unsafe": 0}
    for lst in res:
        if check_inc_dec(lst) and check_difference(lst):
            tmp["Safe"] += 1
        else:
            tmp["Unsafe"] += 1

    return tmp["Safe"]

## good and check_again function provides result for both parts of problem
def good(d, s=0):
    for i in range(len(d)-1):
        if not 1 <= d[i]-d[i+1] <= 3:
            return s and any(good(d[j-1:j] + d[j+1:]) for j in (i,i+1))
    return True

def check_again(res):

    for s in 0, 1:
        print(sum(good(lst, s) or good(lst[::-1], s) for lst in res))


def main():
    res = []
    with open("input.txt") as file:
        for line in file:

            lst = [int(i) for i in line.split()]
            res.append(lst)

    file.close()
    check_again(res)

    # print(check_safe(res))


if __name__ == "__main__":
    main()
