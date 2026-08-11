class Solution:
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        answer = [0] * n

        stack = []

        for i in range(n):

            while stack and temperatures[i] > temperatures[stack[-1]]:
                previous_day = stack.pop()
                answer[previous_day] = i - previous_day

            stack.append(i)

        return answer