def yangjojang():
    cnt = int(input())
    dic = {}
    result = []
    for i in range(cnt):
        school, alcohol =input().split(" ")
        dic[school] = int(alcohol)

    dic = sorted(dic.items(), key=lambda x:x[1],reverse=True)    
    
    #for i in range(len(dic[0])):
     #   if ord(dic[0][i]) >= 48 and ord(dic[0][i]) <= 57:
      #      result.append(dic[0][i])
    
    print(dic[0][0])
    

cnt = int(input())
for i in range(cnt):
    yangjojang()