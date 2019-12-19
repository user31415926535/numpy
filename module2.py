import numpy as np
import sys
import matplotlib.pyplot as plot
N = int(sys.argv[1]) 
weights = np.hanning(N) 
print("Weights", weights)
t = np.arange(N - 1, len(bhp_returns)) 
plot(t, bhp_returns[N-1:], lw=1.0) 
plot(t, smooth_bhp, lw=2.0) 
plot(t, vale_returns[N-1:], lw=1.0) 
plot(t, smooth_vale, lw=2.0) 
plot.show()
