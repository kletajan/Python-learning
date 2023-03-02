import copy
import random
# Consider using the modules imported above.


class Hat():

  def __init__(self, listOfBalls):
    self.contest = []

    counter = 0

    for ball in listOfBalls:
      ballColor = listOfBalls[counter].split('=')[0]
      ballCount = int(listOfBalls[counter].split('=')[1])
      while ballCount > 0:
        self.contest(ballColor)
        ballCount = ballCount - 1
      counter = counter + 1

  def draw():
    return ""


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  m = 0
  return m / num_experiments
