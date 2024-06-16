def handle_input() -> list[tuple[int, int]]:
    n = input()
    if not n.isdigit():
        raise Exception('invalid n')
    n = int(n)
    if n < 1 or n > 10**4:
        raise Exception('1<= n <=10**4')

    res: list[tuple[int, int]] = []
    for _ in range(n):
        input_string = input()
        parts = input_string.split()
        if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
            l_i = int(parts[0])
            r_i = int(parts[1])
            if l_i < 1:
                raise Exception('starting should be greater than 0')
            if r_i > 2*(10**4):
                raise Exception('End should be less than 2*10^4')

            if l_i > r_i:
                raise Exception('starting should be less than or equal to end')

            res.append((l_i, r_i))
        else:
            raise Exception('invalid duration')

    return res


def main() -> list[int]:
    res = handle_input()
    n = len(res)
    res.sort(key=lambda x: x[1])
    maxDay = res[-1][-1]
    minDay = 2*(10**4)
    for i in range(len(res)):
        if res[i][0] < minDay:
            minDay = res[i][0]
        if minDay == 1:
            break

    table: dict[int, list[int]] = dict()
    for idx, duration in enumerate(res):
        for d in range(duration[0], duration[1]+1):
            if d not in table:
                table[d] = []
            table[d].append(idx)
    ans: list[int] = []
    # n lines
    for k in range(1, n+1):
        num = 0
        # j denotes starting day
        for j in range(minDay, maxDay-k+2):
            invited: set[int] = set()
            # k consecutive days starting from day j. Each day is denoted by day i
            for i in range(j, j+k):
                flag = False
                if i not in table:
                    break
                avaliable = table[i]
                for d in avaliable:
                    if d not in invited:
                        invited.add(d)
                        flag = True
                        break

                # this means that we can not hold a conference from j to j+k because of day i
                if not flag:
                    break
            else:
                # this meas that we can hold a conference from j to j+k
                num += 1

        ans.append(num)

    return ans


if __name__ == '__main__':
    ans = main()
    for i in range(len(ans)):
        print(ans[i])

# total time: 1:21:54.75
# coding time: 36min
