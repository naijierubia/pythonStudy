import numpy as np

data = [("zs", [90, 98, 96], 15), ("ls", [91, 92, 92], 16), ("ww", [92, 95, 94], 17)]

ary01 = np.array(data, dtype="2str, 3int32, int32")
print(ary01)

# 但遇到庞大的数据量时，用index索引数据会导致代码难以维护，需要为每列数据命名
ary02 = np.array(
    data, dtype={"names": ["name", "score", "age"], "formats": ["S3", "3i", "i"]}
)
ary03 = np.array(data, dtype=[("name", "S3"), ("score", "3i"), ("age", "i")])
