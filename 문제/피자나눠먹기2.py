#머쓱이네 피자가게는 피자를 여섯 조각으로 잘라 줍니다. 피자를 나눠먹을 사람의 수 n이 매개변수로 주어질 때, n명이 주문한 피자를 남기지 않고 모두 같은 수의 피자 조각을 먹어야 한다면 최소 몇 판을 시켜야 하는지를 return 하도록 solution 함수를 완성해보세요.

# 6과 n의 최소공배수를 찾아서 6으로 나눈 몫을 구하기
import math
def solution(n):
    a = abs(n * 6) // math.gcd(n, 6)
    answer = a // 6
    return answer

# abs는 절댓값 구하기