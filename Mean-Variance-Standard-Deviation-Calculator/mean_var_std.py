import numpy as np

def calculate(list):
  x = np.array(list).reshape(3,3)
  
  if len(list) == 9:
      calculations = {
  'mean': meanList,
  'variance': varianceList,
  'standard deviation': standevList,
  'max': mAXList,
  'min': minList,
  'sum': sumList
    }

  else:
      calculations = "List must contain nine numbers" 

    return calculations