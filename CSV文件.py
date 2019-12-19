import numpy as np

t = np.arange(len(bhp_returns)) 
plot(t, bhp_returns, lw=1) 
plot(t, vale_returns, lw=2) 
show()