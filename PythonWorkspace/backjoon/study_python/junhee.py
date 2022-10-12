def junhee():
    cnt = int(input())
    yes = 0
    no = 0
    for i in range(cnt):
        cute = int(input())

        if cute == 1:
            yes += 1
        else:
            no += 1
    if yes >= no:
        print("Junhee is cute!")
    else:
        print("Junhee is not cute!")

junhee()
