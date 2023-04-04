num = input("Enter a number")
def pyramid(num:int):
    '''This function print a pyramid'''
    for i in range(num):
        for j in range(j+1):
            print(j+1, end=" ")
        print("\n") 