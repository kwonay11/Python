# 여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있다..
# 그렇다면..reverse에서 lost와 같은것이 있으면 제거
def solution(n, lost, reserve):
    #set으로 중복(같은거) 제거
    lost2 = list(set(lost) - set(reserve))
    reserve2 = list(set(reserve) - set(lost))

    for i in reserve2:
        if i-1 in lost2:
            lost2.remove(i-1)
            continue
        elif i+1 in lost2:
            lost2.remove(i+1)
            continue

    # print(lost2)
    # print(reserve2)
    answer = n - len(lost2)
    return answer

print(solution(7,[1,2,3,4,5,6,7],[1,2,3]))