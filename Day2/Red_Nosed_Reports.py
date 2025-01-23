def check_safe(res):
    flag = []
    prev = 0
    for lst in res:
        if lst == sorted(lst) or lst == lst.sort(reverse=True):
            continue
        else:
            flag.append(False)
            continue

        prev = lst[0]
        for i in range(1, len(lst)):
            if abs(lst[i] - prev) > 3 or abs(lst[i] - prev) < 1:
                flag.append(False)
                continue
            else:
                prev = lst[i]
                continue


    return len(res) - len(flag)

def main():
    res = []
    with open("input.txt") as file:
        for line in file:

            lst = [int(i) for i in line.split()]
            res.append(lst)

    print(check_safe(res))


if __name__ == "__main__":
    main()
