from collections import deque
def solution(progresses, speeds):
    progresses = deque(progresses)
    speeds = deque(speeds)
    cnt = 0
    complete = deque()
    while True:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        
        while True:
            if len(progresses) == 0:
                complete.append(cnt)
                break

            if progresses[0] >= 100:
                progresses.popleft()
                speeds.popleft()
                cnt += 1
                continue
            
            if cnt > 0:
                complete.append(cnt)
                print(complete)
                cnt = 0

            
            break
        if len(progresses) == 0:
            break

        
    print(complete)
                
            
    
        
    



progresses = [93,30,55]
speeds = [1,30,5]
solution(progresses,speeds)
