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
import timeit

def promptProblem():
  print("You are climbing a staircase. You can go one step or two steps. There are n number of steps. ")
  print("how much ways would there be to climb it. You must find a formula that works for n every time.")
  print("You can type a number to get how many ways you can do it.")
  print("For example if you type 5 you get 8. On a 5 step staircase there are eight ways to climb it. Good luck!")

def inputStairs():
  steps = int(input('Pick a number for the machine.\n There are 9 choices. (1, 2, 3, 4, 5, 6, 7, 8, or 9, ) \n'''))
  if steps > 9:
    print("I'm sorry, our system does not go that high.")
    return None
  else:
    return steps
  
def listSteps(s):
  # Argument s is the total steps. 
  # I used s to draw out the index.
  if s == None:
    print("You can only pick 0 to 9.")  
    return
  list = [1,1,2,3,5,8,13,21,34,55]
  print("There is " + str(list[s]) + " way/ways to climb the staircase.")

def calculateWaysFormula(steps):
  # Argument steps would be the number of steps. 
  # You can take any number.
  # It returns the number of ways to climb the staircase. 
  # If the "steps" is less than 0 then the function will return "None".
  # This method is called an Up-Down approach. The implementation is simple and easy to understand.
  # The greater the number the more time it will take. When you start reaching the 40s it takes a few more minutes.
  if steps < 0:
    return None 
  if steps == 0:
    return 1
  if steps == 1:
    return 1
  return(calculateWaysFormula(steps-1) + calculateWaysFormula(steps-2))

  mem = [0] * 100
  def ways(steps):
    global mem
def memory():
 if mem == 0
  print("Nothing in memory")
 if mem>0
  print("In storage")
  
# what you really do/execute
def main():
  # promptProblem()
  # s = inputStairs()
  # listSteps(s)
  print(timeit.timeit("calculateWaysFormula(1)", setup="from __main__ import calculateWaysFormula", number=100))


if __name__ == "__main__":
  # execute only if run as a script
  main()