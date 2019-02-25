##Python Web Development Techdegree
##Project 1 - Number Guessing Game


import random
counter=0
score_record=[]


### this function is used to ask if the player wants to play again.
def ask_to_playagain():
  
  choice=input('\nDo you want to play again? Y/N : ')
  counter=0 ## setting the counter to 0  to count all over again for the new session
  
  if choice.upper()=='Y':
    print("\nGreat!  let's keep playing.")
            
    print('\n',highscore(),'\n')
    answer_number=random_generator()## setting a new random number for the new session
    start_game()
            
  if choice.upper()=='N':
    print('\nthank you \n good bye')
    quit()## closes the program
    
  else:
    print('\noops you entered invalid answer.\n please try again\n')
    ask_to_playagain()
  
  
  

def highscore():
  
  high_score=min(score_record)
  
  score= 'Current High Score =  {} '.format(high_score)
  return score

def random_generator():
      return random.randint(1,10)

print('........... WELCOME TO MY NUMBER GUESSING GAME ............\n\n')
def start_game():
    
    ## sets the random number to avariable
    answer_number=random_generator()
    
    ## used to count the number of trys
    counter=0
    
    while True:
      
      ##checks for errors
      try:
        answer=int(input('GUESS A NUMBER BETWEEN 1 AND 10 : '))
        
      except ValueError as Err:
        print('\n please use numbers only.\n please, try again\n')
      
      else:
        counter +=1
        if answer==answer_number:
          print('\nGOOD JOB! you got the answer after trying {} times\n'.format(counter))
          
          ##saves the score to a list so we can compare and find the high score
          score_record.append(counter)
          
          ## calls the function that asks if you want to play again
          ask_to_playagain()
  
        ##checks if the answer is lower    
        if answer>answer_number and answer <=10:
          print('\nIts lower')
          continue
          
        ## checks if the answer is higher 
        if answer<answer_number and answer >=1:
          print('\nits higher')
          continue
          
        ## to check if the answer is in the range
        if answer > 10 or answer<1:
          print('\nplease only numbers between 1 and 10\n')
          continue
          
        

        
         
start_game()         

    
    
