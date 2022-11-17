import math
import sys
def microwave():
    A = 300
    B = 60
    C = 10

    click_A = 0
    click_B = 0
    click_C = 0

    T = int(sys.stdin.readline())
    
    if T >= A:
        click_A = math.floor(T/A)
        T = T % A
    
    if T >= B:
        click_B = math.floor(T/B)
        T = T % B

    if T >= C:
        click_C = math.floor(T/C)
        T = T % C
    
    if T != 0:
        print(-1)
    else:
        print(f'{click_A} {click_B} {click_C}')
    
microwave()