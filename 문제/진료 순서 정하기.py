# 외과의사 머쓱이는 응급실에 온 환자의 응급도를 기준으로 진료 순서를 정하려고 합니다. 정수 배열 emergency가 매개변수로 주어질 때 응급도가 높은 순서대로 진료 순서를 정한 배열을 return하도록 solution 함수를 완성해주세요.

# 원래 배열 [3, 76, 24]
# 정렬된 배열 [76, 24, 3]
# 원래배열을 순회하면서 index로 대체
def solution(emergency):
    sorted_emergency = sorted(emergency, reverse=True)
    answer = []
    for i in emergency:
        rank = sorted_emergency.index(i) + 1
        answer.append(rank)
    return answer

# .index() 함수는 리스트의 특정 값에 해당하는 인덱스를 반환

# 다른 풀이
# def solution(emergency):
#     e = sorted(emergency,reverse=True)
#     return [e.index(i)+1 for i in emergency]