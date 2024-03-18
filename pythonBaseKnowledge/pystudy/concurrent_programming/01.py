"""
同时执行两个函数，一个执行3秒，一个执行两秒
"""

import time, os

pid = os.fork()
if pid < 0:
    print("Create process error.")
elif pid == 0:
    time.sleep(3)
    print("Parent process over")
else:
    time.sleep(2)
    print("Child process over")
