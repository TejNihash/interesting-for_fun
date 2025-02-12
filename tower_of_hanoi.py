
import sys

list1=[4,3,2,1]
list2=[]
list3=[]


# give the insturctions like a-b or b-a . 

def move_element(a,b):
    # moving the elements from one tower a -> b
    if not a:
        print("no elements in the tower, can't move")
        return 
    element = a[-1]

    if not b:
        #if b is empty, then just add it.
        b.append(element)
        a.pop()
    elif element> b[-1]:
        # we can't add higher elements. so no no
        print("can't add that way")
        return 
    elif element< b[-1]:

        #well if it is acceptable then just add it
        b.append(element)
        a.pop()




while True:
    print(list1)
    print(list2)
    print(list3)
    print()
    print()
    command = input(" enter the move (ab,ac,bc,ba,ca,cb)")

    if command.upper()=='QUIT':
        print("okay boss, I'm going!")
        sys.exit()
    if command =='ab':
        move_element(list1,list2)
    elif command =='ac':
        move_element(list1,list3)
    elif command == 'bc':
        move_element(list2,list3)
    elif command == 'ba':
        move_element(list2,list1)
    elif command == 'ca':
        move_element(list3,list1)
    elif command == 'cb':
        move_element(list3,list2)

    else:
        print("give me valid command bro!")


