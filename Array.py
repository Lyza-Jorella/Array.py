print("********** Programmed by: **********")
print("********** Lyza Jorella R. Del Rosario **********")


list1 = [1, 4, 3, 4, 4, 5, 6, 2, 56, 200]
print(list1)


def menu() :
        print("\n\n********** What do you want to do? **********\n\n"
"1. ->> Add an element \n"
"2. ->> Insert an element \n"
"3. ->> Modify an element \n"
"4. ->> Delete an element\n"
"5. ->> Arrange in ascending order\n"
"6. ->> Arrange in descending order\n")
  
          
menu()
option = int(input("**********Enter your option:**********"))

while option !=0:
    if option == 1:
        #add an element
        for item in list1:
            print(item)
            list1.append(110)
            print(list1)
            break
        
    elif option == 2:
        #insert an element
        for item in list1:
            print(item)
            list1.insert(3,0)
            print(list1)
            break
        
    elif option == 3:
        #Modify an element
        for item in list1:
            print(item)
            list1[4]=120
            print(list1)
            break
        
    elif option == 4:
        #Delete an element
        for item in list1:
            print(item)
            list1.remove(30)
            print(list1)
            break
            
    elif option == 5:
        #arrange in ascending order
        for item in list1:
            print(item)
            list1.sort()
            print(list1)
            break
        
    elif option == 6:
        #arrange in descending order
        for item in list1:
            print(item)
            list1.sort()
            list1.reverse()
            print(list1)
            break
        
    print()
    menu()
    option = int(input("**********Enter your option**********: "))
