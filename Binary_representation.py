# Binary_Representation.
def main():
    pass
    n=map(int,input())
    list_1=list(n)
    list_2=[]
    c=0
    for number in list_1:
       if(number==1 or number==0):
        c=+1
       else:
            list_2.append(number)
    if(len(list_2)==0):
        print("yes")
    else:
        print("no")
if __name__ == '__main__':
    main()
