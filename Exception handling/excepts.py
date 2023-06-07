def Exceptionhandling():
    """funciton for performing different operations on a file 
    like calculating average of all positive numbers , 
    division of two consecutive numbers till end ,
    and handle if any exception occurs
    """
    # docstring for function - sample
    try:
        fileopen = open('number.txt',"r")
        data = fileopen.readlines()
        total = 0
        cnt = 0
        for i in data:
            try:
                i = int(i)
                if i > 0:
                    total += i
                    cnt += 1
            except ValueError:
                print("Non numeric value is present")
                continue
        average = total/cnt
        print("average is :",average)

        for i in range (0,len(data)):
            try:
                if i==(len(data)-1):
                    average = int(data[i]) / int(data[0])
                    # print(f"average of {data[i]} and {data[0]} is {average}",end = ' ')
                    print("average of ",data[i].rstrip() ,"and", data[0].rstrip() ,"is : ",average)
                else:
                    average = int(data[i]) / int(data[i+1])
                    # print(f"average of {data[i]} and {data[i+1]} is {average}",end = ' ' )
                    print("average of ",data[i].rstrip() ,"and", data[i+1].rstrip() ,"is : ",average)

            except(ZeroDivisionError):
                print("number cannot be devided by 0")
                continue
            except(ValueError):
                print("Non numeric value is present")
                continue
    except(FileNotFoundError):
        print("File with this name is not present")
    

Exceptionhandling()