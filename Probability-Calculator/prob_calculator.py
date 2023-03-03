import copy
import random
# Consider using the modules imported above.


class Hat():

  def __init__(self, **listOfBalls):
    self.contents = []
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
  hatContentCopy = copy.deepcopy(hat.contents)
  for colorBallExpected, countBallExpected in expected_balls.items():
    for ballsExpected in range(countBallExpected):
      listExpected.append(colorBallExpected)
  for num_ball_drawn in range(num_experiments):
    drawNumBallsDrawn = hat.draw(num_balls_drawn)
    hat.contents = copy.deepcopy(hatContentCopy)
    counter = 0
    for li in listExpected:
      for dr in drawNumBallsDrawn:
        if li == dr:
          drawNumBallsDrawn.pop(drawNumBallsDrawn.index(dr))
          counter = counter + 1
          break
      if counter == len(listExpected):
        m = m + 1 
  return m / num_experiments