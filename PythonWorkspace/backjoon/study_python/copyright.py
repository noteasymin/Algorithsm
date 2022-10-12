def copyright():
    song, ave = map(int,input().split())

    ave = ave * song - song + 1
    print(ave)

copyright()