import numpy as np

def calculate(list):
  
  if len(list) == 9:
    x = np.array(list).reshape(3,3)
    
    calculations = {
      'mean': [np.mean(x, axis=0).tolist(), np.mean(x, axis=1).tolist(), np.mean(x).tolist()],
      'variance': [np.var(x, axis=0).tolist(), np.var(x, axis=1).tolist(), np.var(x).tolist()],
      'standard deviation': [np.std(x, axis=0).tolist(), np.std(x, axis=1).tolist(), np.std(x).tolist()],
      'max': [np.max(x, axis=0).tolist(), np.max(x, axis=1).tolist(), np.max(x).tolist()],
      'min': [np.min(x, axis=0).tolist(), np.min(x, axis=1).tolist(), np.min(x).tolist()],
      'sum': [np.sum(x, axis=0).tolist(), np.sum(x, axis=1).tolist(), np.sum(x).tolist()]
    }

  else:
    raise ValueError('List must contain nine numbers.')
    
  print(calculations)


calculate([0,1,2,3,4,5,6,7,8])