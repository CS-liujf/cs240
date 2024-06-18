from functools import reduce


def handle_input() -> str:
    input_string = input().rstrip()
    if not input_string.isdigit():
        raise Exception('Invalid input')
    if len(input_string) > 50:
        raise Exception('The sequence length no more than 50')

    return input_string


class Solution:
    def __init__(self) -> None:
        self.string = ""

    def getNum(self) -> int:
        self.string = handle_input()
        dp: list[list[int]] = [[0] * len(self.string) for _ in range(10)]
        for i in range(10):
            dp[i][0] = 1

        for i in range(1, len(dp[0])):
            for j in range(10):
                temp = 2*j
                s_i = int(self.string[i])
                if (temp+1-s_i >= 0 or temp-s_i >= 0 or temp-1-s_i >= 0):
                    g_prev = temp-s_i
                    if (g_prev >= 0 and g_prev < 10):
                        dp[j][i] += dp[g_prev][i-1]

                    g_prev += 1
                    if (g_prev >= 0 and g_prev < 10):
                        dp[j][i] += dp[g_prev][i-1]

                    g_prev -= 2
                    if (g_prev >= 0 and g_prev < 10):
                        dp[j][i] += dp[g_prev][i-1]

        # for it in dp:
        #     print(it)

        ans = sum([sub[-1] for sub in dp])
        # check
        if len(self.string) > 1:
            for i in range(1, len(self.string)):
                g_i = int(self.string[-i])
                if dp[g_i][-i] == 0:
                    break

                g_prev = int(self.string[-(i+1)])
                temp = g_prev+g_i
                if temp % 2 != 0 and temp//2+1 != g_i and temp//2 != g_i:
                    break
                elif temp % 2 == 0 and temp//2 != g_i:
                    break
            else:
                ans -= 1

        return ans


if __name__ == '__main__':
    sol = Solution()
    ans = sol.getNum()
    print(ans)
