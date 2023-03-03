import copy
import random
# Consider using the modules imported above.


class Hat():

  def __init__(self, **listOfBalls):
    self.contest = []
    for colorBall, countBall in listOfBalls.items():
      for balls in range(countBall):
        self.contents.append(colorBall)

  def draw(self, num_balls_drawn):
    if num_balls_drawn <= len(self.contents):
      drawn_balls = []
      for i in range(num_balls_drawn):
        random_int = random.randrange(len(self.contents))
        drawn_balls.append(self.contents[random_int])
        self.contents.pop(random_int)
      return drawn_balls
    else:
      return self.contents


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  m = 0
  listExpected = []
  for colorBallExpected, countBallExpected in expected_balls.items():
    for ballsExpected in range(countBallExpected):
      listExpected.append(colorBallExpected)
  for num_ball_drawn in range(num_balls_drawn):
    drawNumBallsDrawn = hat.draw.(num_ball_drawn)
    
    
    
    
  return m / num_experiments
