# 우주여행을 하던 머쓱이는 엔진 고장으로 PROGRAMMERS-962 행성에 불시착하게 됐습니다. 입국심사에서 나이를 말해야 하는데, PROGRAMMERS-962 행성에서는 나이를 알파벳으로 말하고 있습니다. a는 0, b는 1, c는 2, ..., j는 9입니다. 예를 들어 23살은 cd, 51살은 fb로 표현합니다. 나이 age가 매개변수로 주어질 때 PROGRAMMER-962식 나이를 return하도록 solution 함수를 완성해주세요.

dic = {
    0 : "a",
    1 : "b",
    2 : "c",
    3 : "d",
    4 : "e",
    5 : "f",
    6 : "g",
    7 : "h",
    8 : "i",
    9 : "j"
}
def solution(age):
    numbers = list(map(int, str(age)))
    answer = ''
    for i in numbers:
        answer += dic[i]
    return answer

# map 함수
# map(적용할 함수, 반복할 값)
# map(int, "23")일 경우 "2"와 "3"에 각각 int 적용

# 또 다른 풀이
# age = str(age)
# age = age.replace("0", "a")
# age = age.replace("1", "b")
# age = age.replace("2", "c")
# age = age.replace("3", "d")
# age = age.replace("4", "e")
# age = age.replace("5", "f")
# age = age.replace("6", "g")
# age = age.replace("7", "h")
# age = age.replace("8", "i")
# age = age.replace("9", "j")
# 문자열로 바꾸고 replace() 함수 이용하기