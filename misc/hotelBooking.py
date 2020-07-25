hotel={1:5 , 2:8 , 3:6}   # it has 5 (1 room), 8(2 room) and 6 (3 room)

cap = 0
print("Hotel Status :::: ",hotel)
opt = input("OTIONS: Y/N")
while (opt != 'N'):
    if (cap != 0):
        opt = input("OTIONS: Y/N")
        cap = 0
        if opt == 'N':
            exit(0)
    rtype = input("ROOM TYPE: 1/2/3")
    rtype = int(rtype)
    # print(opt, rtype)

    for k, v in hotel.items():
        cap = cap + v
    print("Current Capacity of hotel:", cap)
    if cap == 0:
        print ("Hotel is full with rooms available : ",cap)

    if (opt == 'Y' and cap > 0):
        for k, v in hotel.items():
            # print(k, rtype)
            if (k == rtype):
                print("Room type booked is : ",rtype)
                hotel[k] = v - 1
                cap = cap - 1
    print("Hotel Status now :::: ", hotel)
    print("Capacity of hotel after booking:", cap)