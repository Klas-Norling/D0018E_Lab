    if a=="delete":
        x=a+" * from " +b
        mycursor.execute(x)
        for i in mycursor:
            print(i)