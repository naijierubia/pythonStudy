# 转换时间，只识别- 不识别/
import numpy as np

dates = np.array(["2011", "2011-02", "2011-03-01", "2011-04-01 10:10:10"])
ndates = dates.astype("M8[D]")
print(ndates, ndates.dtype)
print(ndates[-1] - ndates[0])
