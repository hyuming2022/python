from cgi import print_environ_usage
import numpy as np
double_precision = np.finfo(np.float64)
print(double_precision.max)