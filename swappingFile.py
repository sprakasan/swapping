def swapping():
    file1=input("Enter the name of your file.")
    file2=input("Enter the name of your second file.")
    file=open(file1,"r")
    data_a=file.read()
    fileb=open(file2,"r")
    data_b=fileb.read()
    with open(file1,"w") as a:
        a.write(data_b)
    with open(file2,"w")as a:
        a.write(data_a)

swapping()