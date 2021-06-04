def conditioner():
    troom, tcond = map(int, input().split())
    mode = input()
    if mode == "freeze":
        if troom > tcond:
            print(tcond)
        else:
            print(troom)
    elif mode == "heat":
        if troom > tcond:
            print(troom)
        else:
            print(tcond)
    elif mode == "auto":
        print(tcond)
    elif mode == "fan":
        print(troom)
    else:
        print("wrond mode")

if __name__ == '__main__':
    conditioner()
