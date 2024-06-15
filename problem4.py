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


def main():
    res=handle_input()

if __name__ == '__main__':
    main()
