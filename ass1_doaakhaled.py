sigmoid fun by python
///////////////////////
import numpy as np
from numpy.testing import assert_allclose

def sigmoid(x):
    
    s = 1.0 / (1.0 + np.exp(-x))    
    return s
//////////////////////
#!/usr/bin/env python

import numpy as np
from numpy.testing import assert_allclose

def sigmoid(x):
    
    s = 1.0 / (1.0 + np.exp(-x))    
    y = s * (1 - s)
    return y
////////////////////////////
sigmoid fun by matlab
/////////////////////////////
x=-10:0.1:10;
s = 1./(1+exp(-x));
figure; plot(x,s); title('sigmoid');
/////////////////////////////////////////////////////
Normalize
//////////////////////////////////
import numpy as np
from numpy import linalg as LA
X = np.array([[1, 2, 3, 6],
              [4, 5, 6, 5],
              [1, 2, 5, 5],
              [4, 5,10,25],
              [5, 2,10,25]])

print (X.shape)
x = np.array([LA.norm(v,ord=1) for v in X])
print (x)

Output:

   (5, 4)             # array dimension
   [12 20 13 44 42]   # L1 on each Row
////////////////////////////////////////
