import numpy as np

def calculate(list):
  
  if len(list) == 9:
    x = np.array(list).reshape(3,3)

    meanList = [np.mean(x, axis=0, dtype=np.float32), x.mean(axis=1), x.mean()]
    varianceList = 5
    standevList = 5
    maxList = 5
    minList = 5
    sumList = 5

    calculations = {
      'mean': meanList,
      'variance': varianceList,
      'standard deviation': standevList,
      'max': maxList,
      'min': minList,
      'sum': sumList
    }

  else:
    calculations = ValueError("List must contain nine numbers")
    
  print(calculations)


calculate([0,1,2,3,4,5,6,7,8])