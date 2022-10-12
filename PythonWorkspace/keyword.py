def std_weight(height, gender):
    global weight
    if(gender == "남자"):
        weight = height * height * 22
    else:
        weight = height * height * 21
    return weight

int(height), gender = input("성별과 키를 입력하시오").split()
weight = std_weight(height, gender)
print("키 {0}cm {1}의 표준 체중은 {2} 입니다. ".format(height,gender,weight))


