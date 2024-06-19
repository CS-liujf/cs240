def handle_input() -> tuple[str, str]:
    input_string = input()
    parts = input_string.split()
    if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
        n = int(parts[0])
        m = int(parts[1])
        if n < 1 or n > 2*(10**5):
            raise Exception('invalid n')
        elif m < 1 or m > min(n, 5):
            raise Exception('invalid m')

        s = input().rstrip()
        if len(s) != n:
            raise Exception('invalid string S')
        t = input().rstrip()
        if len(t) != m:
            raise Exception('invalid stirng T')
        return s, t

    else:
        raise Exception('invalid input')


def isSame(s: list[str], t: list[str]) -> bool:
    if len(s) != len(t):
        return False

    for i in range(len(s)):
        if s[i] == '#':
            continue
        elif s[i] == t[i]:
            continue
        else:
            return False
    return True


def main() -> bool:
    s, t = handle_input()
    if s[0] != t[0] or s[-1] != t[-1]:
        return False

    set_s = set(s)
    set_t = set(t)
    if set_s != set_t:
        return False

    # find the first t in s
    for i in range(0, len(s)-len(t)+1):
        if s[i:i+len(t)] == t:
            break
    else:
        return False #not found

    s_list: list[str] = list(s)
    len_s = len(s_list)
    t_list: list[str] = list(t)
    len_t = len(t_list)

    temp = ['#' for _ in range(len_t)]
    temp2 = ['#' for _ in range(len_s)]

    # find all t in s:
    # overlapped denotes those ranges have been overlapped.
    # ie. [[1,4]] means [1,4] can be overlapped
    overlapped: list[tuple[int, int]] = []
    i = 0
    while (i < (len_s-len_t+1)):
        if s_list[i:i+len_t] == t_list:
            s_list[i:i+len_t] = temp
            overlapped.append((i, i+len_t-1))
            i += len_t
        else:
            i += 1

    if s_list == temp2:
        return True

    for interval in overlapped:
        l = interval[0]
        r = interval[1]
        # expand to the left
        i = l-1
        while i >= 0 and l-i < len_t:
            temp3 = ['#' for _ in range(l-i)]
            if s_list[i:l] == temp3:
                break
            if (isSame(s_list[i:i+len_t], t_list)):
                s_list[i:l] = temp3
                l = i
            i -= 1

        # expand to the right
        i = r+1
        while i < len_s and i-r < len_t:
            temp3 = ['#' for _ in range(i-r)]
            if s_list[r+1:i+1] == temp3:
                break
            if (isSame(s_list[i-len_t+1:i+1], t_list)):
                s_list[r+1:i+1] = temp3
                r = i
            i += 1

    return s_list == temp2


if __name__ == '__main__':
    print('Yes' if main() else 'No')
