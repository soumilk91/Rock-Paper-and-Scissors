import sys
import time
import random


print "\n---------------------- ROCK, PAPER, SCISSORS -----------------------------------------"
print "\n"
#The user inputs the number of points he needs the game to last for . The user must input an integer value 

loop4=0 # loop4 is for repetition of the entire program
while(loop4!=1):
    loop1=0 # loop1 is for repetition of the point thing until the user inputs a valid option
    while(loop1!=1):
        try:
            point=int(raw_input("How many point game do you want to play ????"))
            loop1=1
        except:
            print"\nPlease Enter a valid option"
    
    
    # Randomly a letter is chosen from r,p,s
    
    computer_score=0
    user_score=0
    
    while(computer_score<point and user_score<point):
        items=['r','p','s']
        random_items=items[random.randrange(len(items))]
        #print random_items
        
        print"\n Enter your Choice."
        print"\n Choose 'r' or 'R' for Rock"
        print"\n Choose 'p' or 'P' for Paper"
        print"\n Choose 's' or 'S' for Scissors"
        
        
        
        
        # take an input from the user 
        print"\n"
    
    
        
        loop2=0
        while(loop2!=1):
            try:
                
                choice=raw_input("Please Enter your choice: ")
                #If both the user input and the computer preferences are the same. It results in a draw
                if(choice==random_items):
                    print"\nIt's a DRAW. No one gets points"
                    print"\nComputer's Score=%d"%computer_score
                    print"\nYour Score=%d"%user_score
                    loop2=1
                
                  
                #Paper wins against Rock
                elif ((choice=='r' or choice=='R') and random_items=='p'):
                    print"\n The computer chose 'Paper' and you chose 'Rock'. The computer wins"
                    computer_score=computer_score+1
                    print"\nComputer's Score=%d"%computer_score
                    print"\nYour Score=%d"%user_score
                    loop2=1
                
                #Rock wins against Scissor
                elif ((choice=='r' or choice=='R') and random_items=='s'):
                    print"\n The computer chose 'Scissor' and you chose 'Rock'. You win"
                    user_score=user_score+1
                    print"\nComputer's Score=%d"%computer_score
                    print"\nYour Score=%d"%user_score
                    loop2=1
                            
                #Paper wins against Rock
                elif ((choice=='p' or choice=='P') and random_items=='r'):
                    print"\nThe Computer chose 'Rock' and you chose 'Paper'. You Win"
                    user_score=user_score+1
                    print"\nComputer's Score=%d"%computer_score
                    print"\nYour Score=%d"%user_score
                    loop2=1
                    
                        
                #Scissor wins against Paper
                elif ((choice=='p' or choice=='P') and random_items=='s'):
                    print"\nThe Computer chose 'Scissor' and you chose 'Paper'. The Computer Wins"
                    computer_score=computer_score+1
                    print"\nComputer's Score=%d"%computer_score
                    print"\nYour Score=%d"%user_score
                    loop2=1
                    
                    
                #Rock wins against Scissor
                elif((choice=='s' or choice=='S') and random_items=='r'):
                    print"\nThe Computer chose 'Rock' and you chose 'Scissor'. The Computer Wins"
                    computer_score=computer_score+1
                    print"\nComputer's Score=%d"%computer_score
                    print"\nYour Score=%d"%user_score
                    loop2=1
                    
                    
                #Scissors win against Paper
                elif ((choice=='s' or choice=='S') and random_items=='p'):
                    print"\nThe Computer chose 'Paper' and you chose 'Scissor'. You win"
                    user_score=user_score+1
                    print"\nComputer's Score=%d"%computer_score
                    print"\nYour Score=%d"%user_score
                    loop2=1
                    
                    
                #If user inputs a wrong value, raise an exception.
                else:
                    raise NameError
            except:
                
                print"\nPlease enter a valid option."
                
    if (user_score>computer_score):
        print"\n --------------  You WIN  ---------------------------"
    if (computer_score>user_score):
        print"\n --------------  You Lose ----------------------------"
    
    # sniplet for restarting the program or  exiting the program
    loop3=0
    while(loop3!=1):
                
        try:
            deci=raw_input("Do you want to play again ??? y or n")
            if(deci=='y' or deci=='Y'):
                print"\n Let's PLAY AGAIN"
                loop3=1
            elif (deci=='n' or deci=='N'):
                print"\n BYE BYE ............. SEE YOU AGAIN ........"
                loop3=1
                loop4=1
            else:
                raise NameError
        except:
            print"\n Please enter a valid option"
    

    
        
        