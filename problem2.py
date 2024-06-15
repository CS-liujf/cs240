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

        s = input()
        if len(s) != n:
            raise Exception('invalid string S')
        t = input()
        if len(t) != m:
            raise Exception('invalid stirng T')
        return s, t

    else:
        raise Exception('invalid input')


def main() -> bool:
    s, t = handle_input()
    set_s = set(s)
    set_t = set(t)
    if set_s != set_t:
        return False
    
    
    return True


if __name__ == '__main__':
    print('Yes' if main() else 'No')
