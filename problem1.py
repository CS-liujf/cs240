def handle_input() -> tuple[int, int]:
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


def main() -> bool:
    pattern = 'wbwbwwbwbwbw'
    p_length = len(pattern)
    w, b = handle_input()
    w_num, b_num = 0, 0
    if w+b <= len(pattern):
        for i in range(0, p_length-(w+b)+1):
            if i == 0:
                for j in range(i, i+w+b):
                    if pattern[j] == 'w':
                        w_num += 1
                    else:
                        b_num += 1
            else:
                if pattern[i-1] == 'w':
                    w_num -= 1
                else:
                    b_num -= 1

                if pattern[i+w+b-1] == 'w':
                    w_num += 1
                else:
                    b_num += 1

            if w_num == w and b_num == b_num:
                return True

        return False

    else:
        for chr in pattern:
            if chr == 'w':
                w_num += 1
            else:
                b_num += 1

        repeat_num = (w+b) // len(pattern)
        w_num = repeat_num*w_num
        b_num = repeat_num*b_num
        resd_length = (w+b) % len(pattern)
        for i in range(resd_length+1):
            # lookup the forward part
            for j in range(-1, -1-i, -1):
                if pattern[j] == 'w':
                    w_num += 1
                else:
                    b_num += 1
            # lookup the backward part
            for j in range(0, resd_length-i):
                if pattern[j] == 'w':
                    w_num += 1
                else:
                    b_num += 1

            if w_num == w and b_num == b_num:
                return True

    return False


if __name__ == '__main__':
    print('Yes' if main() else 'No')
