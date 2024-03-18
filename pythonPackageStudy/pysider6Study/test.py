from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import QApplication, QPushButton

app = QApplication()
# 读取图像文件
pixmap = QPixmap(r"F:\creation\std\python\pysider6Study\PySide6-Code-Tutorial\Resources\Icons\C_128px.png")
# 将图像转换为图标
icon = QIcon(pixmap)
# 创建按钮并设置图标
button = QPushButton()
button.setIcon(icon)
# 显示按钮
button.show()
app.exec()
