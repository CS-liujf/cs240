def auxInput() -> tuple[int, int]:
    input_string = input()
    parts = input_string.split()
    if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
        w = int(parts[0])
        b = int(parts[1])
        if w < 0 or w > 100:
            raise Exception('invalid w')
        elif b < 0 or b > 100:
            raise Exception('invalid b')
        elif w+b < 1:
            raise Exception('sum must be ast least 1')

        return w, b
    else:
        raise Exception('invalid input')


def handle_input() -> list[tuple[int, int]]:
    n = input()
    if not n.isdigit():
        raise Exception('invalid n')

    n = int(n)
    if n < 0 or n > 10:
        raise Exception('0<=n<=10')

    ans: list[tuple[int, int]] = []
    for _ in range(n):
        ans.append(auxInput())

    return ans


pattern = 'wbwbwwbwbwbw'
p_length = len(pattern)


def lookupInStr(length: int, w: int, b: int) -> bool:
    if length > p_length:
        return False

    w_num, b_num = 0, 0
    for i in range(0, p_length-length+1):
        if i == 0:
            for j in range(i, i+length):
                if pattern[j] == 'w':
                    w_num += 1
                else:
                    b_num += 1
        else:
            if pattern[i-1] == 'w':
                w_num -= 1
            else:
                b_num -= 1

            if pattern[i+length-1] == 'w':
                w_num += 1
            else:
                b_num += 1

        if w_num == w and b_num == b:
            return True

    return False


def lookupAtJunction(length: int, w: int, b: int) -> bool:
    if length > p_length:
        return False

    w_num, b_num = 0, 0
    for i in range(length+1):
        # lookup the forward part
        for j in range(-1, -1-i, -1):
            if pattern[j] == 'w':
                w_num += 1
            else:
                b_num += 1
        # lookup the backward part
        for j in range(0, length-i):
            if pattern[j] == 'w':
                w_num += 1
            else:
                b_num += 1

        if w_num == w and b_num == b:
            return True

    return False


def auxFunc(w: int, b: int) -> bool:
    if lookupInStr(w+b, w, b) or lookupAtJunction(w+b, w, b):
        return True

    repeat_num = (w+b) // p_length
    w_num = repeat_num*7
    b_num = repeat_num*5
    resd_length = (w+b) % p_length

    if lookupInStr(resd_length, w-w_num, b-b_num) or lookupAtJunction(resd_length, w-w_num, b-b_num):
        return True

    return False



def main():
    arr = handle_input()
    ans: list[bool] = [auxFunc(w, b) for w, b in arr]
    for value in ans:
        print("Yes" if value else "No", end=' ')

    print()


if __name__ == '__main__':
    main()
