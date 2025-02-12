#so this is a program to solve the tower of hanoi on it's own. it should just give me the output of the steps on its own.


import sys

list0=[4,3,2,1]
list1=[]
list2=[]
# give the insturctions with indication of movement along with the array

def move_top_element(lis1, lis2):
    # move top stack from lis1 -> lis2
    #just takes in the stack and moves the stack from one list to another. cool? nice and simple right

    if len(lis1)!=0:
        lis2.append(lis1.pop())
    else:
        print("can't do that operation bro")

    


def print_stack():
    print(list0)
    print(list1)
    print(list2)
    print()
    print()

def move_stack(k,a,b):
    #let's just assume that lists are available inside the function cause of globalness of them.

    if a==0 and b==1:
        
        
    
        #moving stack from left to middle    
        
       
        p=len(list2) # keep track of no.of things on the 3rd peg before elements are added to it
        if k==len(list0)-1:
            move_top_element(list0,list1)
            print_stack()
            return 
        move_stack(k+1,0,2)

        move_top_element(list0,list1)
        print_stack()

        
        move_stack(p,2,1)



    if a==0 and b==2:

        
        

        p=len(list1) # keep track of no. of things on the 2nd peg before elements are added to it
        if k==len(list0)-1:
            move_top_element(list0,list2)
            print_stack()
            return

        move_stack(k+1,0,1)

        move_top_element(list0,list2)
        print_stack()

        
        move_stack(p,1,2)

    if a==1 and b==0:

       
    
        p=len(list2) # keep track of no. of things on the 2nd peg before elements are added to it
        if k==len(list1)-1:
            move_top_element(list1,list0)
            print_stack()
            return

        move_stack(k+1,1,2)

        move_top_element(list1,list0)
        print_stack()

        move_stack(p,2,0)


    if a==1 and b==2:

        
    
        p=len(list0) # keep track of no. of things on the 2nd peg before elements are added to it

        if k ==len(list1)-1:
            move_top_element(list1,list2)
            print_stack()
            return


        move_stack(k+1,1,0)

        move_top_element(list1,list2)
        print_stack()

        move_stack(p,0,2)

    if a==2 and b==0:
       

        if k ==len(list2)-1:
            move_top_element(list2,list0)
            print_stack()
            return

        p=len(list1) # keep track of no. of things on the 2nd peg before elements are added to it
        move_stack(k+1,2,1)

        move_top_element(list2,list0)
        print_stack()

        
        move_stack(p,1,0)

    if a==2 and b==1:
        


        if k ==len(list2)-1:
            move_top_element(list2,list1)
            print_stack()
            return

        p=len(list0) # keep track of no. of things on the 2nd peg before elements are added to it
        move_stack(k+1,2,0)

        move_top_element(list2,list1)
        print_stack()

        
        move_stack(p,0,1)


#ask the input from the user
while True:
    print_stack()
    



    #they can be made to take input better way later on
    from_stack = int(input(" enter the move (a,b,c)"))
    to_stack = int(input("enter the move (a,b,c)"))

 

    move_stack(0,from_stack,to_stack)



  
    
        #print("give me valid command bro!")

    
    
    










