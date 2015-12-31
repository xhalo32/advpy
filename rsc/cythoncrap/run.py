from time import time
import pyximport; pyximport.install(  )
n = time(  )

import c

print time(  ) - n