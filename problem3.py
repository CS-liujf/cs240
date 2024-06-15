def handle_input() -> str:
    input_string = input()
    if not input_string.isdigit():
        raise Exception('Invalid input')
    if len(input_string) > 50:
        raise Exception('The sequence length no more than 50')

    return input_string


class Solution:
    def __init__(self) -> None:
        self.string = handle_input()
        self.num = 0

    def getNum(self) -> int:
        for i in range(0, 10):
            self.auxFunc(2, i)

        return self.num

    def auxFunc(self, i: int, g_prev: int):
        if i > len(self.string):
            self.num += 1
            return

        temp = int(self.string[-1*i]) + g_prev
        self.auxFunc(i+1, temp//2)
        if temp % 2 != 0:
            self.auxFunc(i+1, temp//2+1)


if __name__ == '__main__':
    sol = Solution()
    print(sol.getNum())
