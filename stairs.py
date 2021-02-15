###
## Problem: 
# Your sopposed to find a formula for how many ways you can climb a staircase. This will have to work for any number of stairs. 
# Rule: You can only climb 1 step or 2 steps each time.
## Examples:
# if you had 3 staircases you would get 3 ways: [1,2], [2,1], [1,1,1]
# Corner cases: For 0 steps you would get 1 way because you already got there.
## Solution: 
# I pre-calculated the answers for the problem, and put them in a list. 
# The user uses the number of stairs as an input. The input (number of stairs) is the index to summon the answer in the list.


steps = -1

def promptProblem():
  print("You are climbing a staircase. You can go one step or two steps. There are n number of steps. ")
  print("how much ways would there be to climb it. You must find a formula that works for n every time. You can type a number to get how many ways you can do it. ")
  print("For example if you type 5 you get 8. On a 5 step staircase there are eight ways to climb it. Good luck!")

def inputStairs():
  #steps
  global steps 
  steps = int(input('Pick a number for the machine.\n There are 9 choices. (1, 2, 3, 4, 5, 6, 7, 8, or 9, ) \n'''))
  if steps > 9:
    print("I'm sorry, our system does not go that high.")
    return

def listSteps():
  list = [1,1,2,3,5,8,13,21,34,55]
  print(list[steps])



# what you really do/execute
def main():
  promptProblem()
  inputStairs()
  listSteps()



if __name__ == "__main__":
  # execute only if run as a script
  main()