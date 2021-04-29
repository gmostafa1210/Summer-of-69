def summer_of_69(*args):
    startn = 0
    endn = 0
    mylist = list(args)
    for newnum in range(0, len(args)-1):
        if args[newnum] == 9:
            endn = newnum + 1
            break
    for num in range(0, len(args)-1):
        if args[num] == 6:
            startn = num
            break
    for num in range(0,len(args)-1):
        if startn > 0 and endn > 0 and startn < endn:
            while(startn != endn):
                mylist.pop(startn)
                endn -= 1

    print(sum(mylist))

summer_of_69(1, 4, 6, 5, 9, 7, 5)