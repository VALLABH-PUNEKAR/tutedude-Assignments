try:
    file1 = open("sample.txt",'r+')
    c=0
    i = file1.readlines()
    print("Reading File Content: ")
    while c<len(i):
        print("Line ",c+1,": ",i[c])
        c+=1
    file1.close()
except FileNotFoundError:
    print("Error: The File 'sample.txt' was not found")
