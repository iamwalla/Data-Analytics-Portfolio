import numpy as np

def calculate(list):

  if len(list)!=9:
    raise ValueError('List must contain nine numbers.')
  else: 
    array=np.array(list).reshape(3,3)
    calculations={'mean':[np.mean(array,axis=0),np.mean(array,axis=1),np.mean(array)],
         'variance':[np.var(array,axis=0),np.var(array,axis=1),np.var(array)],
         'standard deviation':[np.std(array,axis=0),np.std(array,axis=1),np.std(array)],
         'max':[np.max(array,axis=0),np.max(array,axis=1),np.max(array)],
         'min':[np.min(array,axis=0),np.min(array,axis=1),np.min(array)],
         'sum':[np.sum(array,axis=0),np.sum(array,axis=1),np.sum(array)]}
    return print('{' + '\n' .join("{!r}: {!r},".format(k, v) for k, v in calculations.items()) + "}")


    return calculations