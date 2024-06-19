from typing import TypedDict


def handle_input() -> list[tuple[int, int]]:
    n = input().rstrip()
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


class Invitation(TypedDict):
    flag: bool
    sDate: int
    persons: set[int]


def main() -> list[int]:
    res = handle_input()
    n = len(res)
    res.sort(key=lambda x: x[1])  # must sort. We take greedy algorithm
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
    ans: list[int] = [0 for _ in range(n)]

    ans[0] = len(table)
    if (ans[0] == 0):
        return ans

    # in tuple[int, set[int]],
    # the first ele denotes whether this arragement is valid
    # the second element denote the starting day
    invitationList: list[Invitation] = []
    # find all 2days combination
    k = 2
    # j denotes starting day
    for j in range(minDay, maxDay-k+2):
        invited: set[int] = set()
        for i in range(j, j+k):
            flag = False
            if i not in table:
                break
            avaliable = table[i]
            for person in avaliable:
                if person not in invited:
                    invited.add(person)
                    flag = True
                    break

            if not flag:
                break

        else:
            invitationList.append(
                {'flag': True, 'sDate': j, 'persons': invited})

    ans[1] = len(invitationList)
    if (ans[1] == 0):
        return ans

    invalidNum = 0
    total = len(invitationList)
    for k in range(3, n+1):
        if invalidNum == total:
            break

        for i in range(len(invitationList)):
            if invitationList[i]['flag'] == False:
                continue

            d = invitationList[i]['sDate']+len(invitationList[i]['persons'])
            if d not in table:
                invitationList[i]['flag'] = False
                invalidNum += 1
                continue

            avaliable = table[d]
            for person in avaliable:
                if person not in invitationList[i]['persons']:
                    invitationList[i]['persons'].add(person)
                    break
            else:
                invitationList[i]['flag'] = False
                invalidNum += 1

        else:
            ans[k-1] = total-invalidNum

    return ans


if __name__ == '__main__':
    ans = main()
    for i in range(len(ans)):
        print(ans[i])

# total time: 1:21:54.75
# coding time: 36min
