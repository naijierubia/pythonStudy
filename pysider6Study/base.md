[TOC]

# pyside6基础

## 基本结构

```python
import random
import sys

# 导入所需的模块
from PySide6 import QtCore, QtWidgets


class MyWidget(QtWidgets.QWidget):
    def __init__(self, *args, **kwargs):
        # 调用父类的初始化方法
        super().__init__(*args, **kwargs)  

        self.hello = ["你好世界", "Hallo Welt", "Hei maailma", "Hola Mundo", "Привет мир"]

        # 设置窗口大小，单位为像素
        self.resize(800, 600)

        # 创建一个按钮控件，其上文字为“点击我”
        self.button = QtWidgets.QPushButton("点击我！")

        # 创建一个标签控件，内容为Hello World,对齐方式为居中
        self.text = QtWidgets.QLabel("Hello World", alignment=QtCore.Qt.AlignCenter)

        # 创建一个「垂直盒子」布局管理器
        self.layout = QtWidgets.QVBoxLayout(self)

        # 将之前创建的控件添加到布局管理器中，即完成布局
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        # 将button.clicked这个信号与self.magic槽函数连接
        self.button.clicked.connect(self.magic)  # type: ignore

    @QtCore.Slot()
    def magic(self) -> None:
        """槽函数"""
        self.text.setText(random.choice(self.hello))  # 从列表中随机显示一条问候语


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)  # 创建APP，将运行脚本时（可能的）的其他参数传给Qt以初始化
    widget = MyWidget()  # 实例化一个MyWidget类对象
    widget.show()  # 显示窗口
    sys.exit(app.exec())  # 正常退出APP：app.exec()关闭app，sys.exit()退出进程

```

## 基本属性

### 窗口和控件

1. QWidget是所有控件的基类，当不传入父控件时，则单独为窗口，即在传入的QWidget下创建控件，默认就是桌面
2. 控件都是矩形的，且根据创建顺序按照Z轴排列

```py
import sys
from PySide6 import QtWidgets

class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        # self创建时未传入父控件，故成为窗口
        # 窗口会被自动修饰标题、最小化最大化关闭按钮等，称为「框架」，可以手动修改其行为
        self.setWindowTitle("QWidget简介")  # 设置窗口标题
        self.resize(800, 600)  # 设置大小
        self.setup_ui()

    def setup_ui(self) -> None:
        """设置界面"""

        # 创建一个名为red的QWidget
        red = QtWidgets.QWidget(self)  # red的父控件为self,故不成为单独窗口
        red.resize(100, 100)
        red.setStyleSheet("background-color: red;")
        red.move(300, 100)

        # 创建一个名为green的QWidget
        green = QtWidgets.QWidget(self)
        green.resize(100, 100)
        green.setStyleSheet("background-color: green;")
        green.move(300, 150)  # 体现QWidget沿z轴绘制，后面的控件可以覆盖前面的控件


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    window = MyWidget()
    window.show()
    sys.exit(app.exec())
```

### 大小和尺寸

```py
# 设置大小
.resize(800, 600)

# 设置最大最小尺寸，限制最大尺寸，且无法被resize超出
.setMaximumSize(1000, 800)
.setMinimumSize(200,160)
.setMaximumWidth(1000)
.setMaximumHeight(800)

# 固定尺寸，用户不能通过拖拽改变尺寸
.setFixedSize(500, 500)  
.setFixedWidth(500)  
.setFixedHeight(500)

# 根据内容自动调节大小
.adjustSize()
```

### 位置

1. 左上角为原点，向右为x轴正方向，向下为y轴正方向
2. 为窗口时设置获取的是相对窗口的位置
3. 为控件时设置获取的是相对父控件的位置

```py
# 设置位置
.move(x,y)
# 同时设置位置和大小
.setGeometry(x,y,w,h)

# 读取位置
.pos()
.geometry()
```

### 内容边距

实际上为css中的padding，调整实际内容和控件的边缘距离

```py
# 设置内容边距
.setContentsMargins(left,top,right,bottom)
# 获取内容边距
.contentsMargins()
```

### 父子控件

通过多种API来获取控制父子控件

```py
# 指定控件的父控件
.setParent(QWidget)
# 获取控件的父控件
.parentWidget()
# 获取控件的所有子控件列表
.children()
# 获取指定坐标的子控件
.childAt(x,y)
# 所有子控件（被隐藏的除外）构成的矩形
.childrenRect()
# 所有子控件（被隐藏的除外）构成的范围
.childrenRegion()
```

### 可见和可用

1. 设置控件不可见后，控件原先的位置依然会被占据
2. 按钮，下拉框，文本输入框设置为不可用后无法交互

```py
# 设置可见状态
.setVisible(bool)
# 获取可见状态
.isVisible()
# 隐藏，等同于self.setVisible(False)
.hide()   
# # 显示，等同于self.setVisible(True)
.show() 

# 设置可用状态
.setEnabled(bool)
# 获取可用状态
.isEnable()
```

### 层级关系

默认后绘制的控件在上

```py
# 降低层级
.lower()
# 提高层级
.raise_()
# 降低层级到指定控件之下
.stackUnder(QWidget)
```

### 焦点控制

1. 获得了焦点的控件才可以与用户交互
2. 可以使用TAB键在控件间移动焦点，可以指定获取的先后顺序

#### 本控件焦点控制

```py
# 返回控件的是否有焦点
.hasFocus() -> bool
# 如果父控件为活动窗口，则为此控件设置焦点
.setFocus(reason: Qt.FocusReason) 
# 移除焦点
.clearFocus()
```

#### 子控件焦点控制

```py
.focusNextChild() -> bool
.focusPreviousChild() -> bool
# 上两种方法的结合，当next为True时向前搜索，否则向后搜索
.focusNextPrevChild(next: bool) -> bool 
# 返回最后被设置焦点的子部件
.focusWidget() -> QWidget
```

#### Qt.FocusReason

| Constant                      | Value | Description                                                |
| ----------------------------- | ----- | ---------------------------------------------------------- |
| `Qt::MouseFocusReason`        | `0`   | 鼠标活动导致                                               |
| `Qt::TabFocusReason`          | `1`   | 按下了Tab键                                                |
| `Qt::BacktabFocusReason`      | `2`   | Backtab导致，例如按下Shift+Tab键                           |
| `Qt::ActiveWindowFocusReason` | `3`   | 窗口系统使该窗口处于活动或非活动状态                       |
| `Qt::PopupFocusReason`        | `4`   | 应用程序打开/关闭一个弹出窗口，该弹出窗口抓取/释放键盘焦点 |
| `Qt::ShortcutFocusReason`     | `5`   | 用户输入了一个标签的伙伴快捷键（参阅QLabel.buddy）         |
| `Qt::MenuBarFocusReason`      | `6`   | 菜单栏获得了焦点                                           |
| `Qt::OtherFocusReason`        | `7`   | 其他原因                                                   |

#### 焦点策略

切换焦点为setFocusPolicy方法

1. 对于QPushButton、QTextEdit等控件的默认策略为StrongFocus，即可以通过键盘Tab键和鼠标点击两种方式获得焦点
2. 对于QLabel等不需要与用户进行键盘输入交互的控件，焦点策略为NoFocus，不加入焦点链
3. 焦点链默认顺序为子控件创建顺序，即按下键盘Tab键时会按子控件创建顺序依次切换焦点
4. 焦点链默认顺序为子控件创建顺序，即按下键盘Tab键时会按子控件创建顺序依次切换焦点

   .setTabOrder(fist: QWidget, second: QWidget) 将第二个控件从焦点链中移除，并放置到第一个控件之后

| `Qt::TabFocus`                        | 通过键盘Tab键获取焦点                                      |
| ----------------- |  ---------------------------------------------------------- |
| `Qt::ClickFocus`                 | 通过鼠标点击获取焦点                                       |
| `Qt::StrongFocus` | 通过键盘Tab或鼠标点击获取焦点                              |
| `Qt::WheelFocus`           | 在StrongFocus基础上，还支持鼠标滚轮滚动获取焦点            |
| `Qt::NoFocus`                         | 该控件不接受焦点，QLabel等不需要用户键盘操作的控件的默认值 |

### 光标

```py
# 设置光标形状
QWidget.setCursor(QCursor)  
# 取消设置光标形状
QWidget.unsetCursor()     
# 获取光标形状
QWidget.cursor() -> QCursor  
```

####  QCursor 类的常用方法：

```py
# 使用Qt内置的光标形状创建
QCursor.__init__(shape: Qt.CursorShape)    
# 使用QPixmap位图创建
QCursor.__init__(pixmap: Union[QPixmap, QImage, str], hotX: int = -1, hotY: int = -1)   
# 返回该光标当前所在位置坐标（相对于整个屏幕）
QCursor.pos() -> QPoint            
# 设置光标位置坐标（相对于屏幕）
QCursor.setPos(QPoint)            
```



#### 光标样式

| Constant                 | Value | Description                                                  |
| ------------------------ | ----- | ------------------------------------------------------------ |
| `Qt::ArrowCursor`        | `0`   | ![img](https://doc.qt.io/qt-6/images/cursor-arrow.png) The standard arrow cursor. |
| `Qt::UpArrowCursor`      | `1`   | ![img](https://doc.qt.io/qt-6/images/cursor-uparrow.png) An arrow pointing upwards toward the top of the screen. |
| `Qt::CrossCursor`        | `2`   | ![img](https://doc.qt.io/qt-6/images/cursor-cross.png) A crosshair cursor, typically used to help the user accurately select a point on the screen. |
| `Qt::WaitCursor`         | `3`   | ![img](https://doc.qt.io/qt-6/images/cursor-wait.png) An hourglass or watch cursor, usually shown during operations that prevent the user from interacting with the application. |
| `Qt::IBeamCursor`        | `4`   | ![img](https://doc.qt.io/qt-6/images/cursor-ibeam.png) A caret or ibeam cursor, indicating that a widget can accept and display text input. |
| `Qt::SizeVerCursor`      | `5`   | ![img](https://doc.qt.io/qt-6/images/cursor-sizev.png) A cursor used for elements that are used to vertically resize top-level windows. |
| `Qt::SizeHorCursor`      | `6`   | ![img](https://doc.qt.io/qt-6/images/cursor-sizeh.png) A cursor used for elements that are used to horizontally resize top-level windows. |
| `Qt::SizeBDiagCursor`    | `7`   | ![img](https://doc.qt.io/qt-6/images/cursor-sizeb.png) A cursor used for elements that are used to diagonally resize top-level windows at their top-right and bottom-left corners. |
| `Qt::SizeFDiagCursor`    | `8`   | ![img](https://doc.qt.io/qt-6/images/cursor-sizef.png) A cursor used for elements that are used to diagonally resize top-level windows at their top-left and bottom-right corners. |
| `Qt::SizeAllCursor`      | `9`   | ![img](https://doc.qt.io/qt-6/images/cursor-sizeall.png) A cursor used for elements that are used to resize top-level windows in any direction. |
| `Qt::BlankCursor`        | `10`  | A blank/invisible cursor, typically used when the cursor shape needs to be hidden. |
| `Qt::SplitVCursor`       | `11`  | ![img](https://doc.qt.io/qt-6/images/cursor-vsplit.png) A cursor used for vertical splitters, indicating that a handle can be dragged horizontally to adjust the use of available space. |
| `Qt::SplitHCursor`       | `12`  | ![img](https://doc.qt.io/qt-6/images/cursor-hsplit.png) A cursor used for horizontal splitters, indicating that a handle can be dragged vertically to adjust the use of available space. |
| `Qt::PointingHandCursor` | `13`  | ![img](https://doc.qt.io/qt-6/images/cursor-hand.png) A pointing hand cursor that is typically used for clickable elements such as hyperlinks. |
| `Qt::ForbiddenCursor`    | `14`  | ![img](https://doc.qt.io/qt-6/images/cursor-forbidden.png) A slashed circle cursor, typically used during drag and drop operations to indicate that dragged content cannot be dropped on particular widgets or inside certain regions. |
| `Qt::OpenHandCursor`     | `17`  | ![img](https://doc.qt.io/qt-6/images/cursor-openhand.png) A cursor representing an open hand, typically used to indicate that the area under the cursor is the visible part of a canvas that the user can click and drag in order to scroll around. |
| `Qt::ClosedHandCursor`   | `18`  | ![img](https://doc.qt.io/qt-6/images/cursor-closedhand.png) A cursor representing a closed hand, typically used to indicate that a dragging operation is in progress that involves scrolling. |
| `Qt::WhatsThisCursor`    | `15`  | ![img](https://doc.qt.io/qt-6/images/cursor-whatsthis.png) An arrow with a question mark, typically used to indicate the presence of What's This? help for a widget. |
| `Qt::BusyCursor`         | `16`  | ![img](https://doc.qt.io/qt-6/images/cursor-busy.png) An hourglass or watch cursor, usually shown during operations that allow the user to interact with the application while they are performed in the background. |
| `Qt::DragMoveCursor`     | `20`  | A cursor that is usually used when dragging an item.         |
| `Qt::DragCopyCursor`     | `19`  | A cursor that is usually used when dragging an item to copy it. |
| `Qt::DragLinkCursor`     | `21`  | A cursor that is usually used when dragging an item to make a link to it. |
| `Qt::BitmapCursor`       | `24`  |                                                              |

## 按钮控件

### 基本抽象按钮QAbstractButton

1. 提供按钮类通用的方法，如设置文字图标、被点击、键盘快捷键等

2. 自身不能被实例化，子类可以被实例化

3. 被 QPushButton、QRadioButton、QCheckBox 等类继承

```py
class MyButton(QtWidgets.QAbstractButton):
    """自定义的按钮控件，体验从按钮抽象基类继承"""

    def paintEvent(self, evt) -> None:
        """重写了父类的paintEvent"""

        # print("绘制")  # 取消本行注释，可观察绘制事件发生的时刻

        # 绘制按钮上要展示的一个界面内容，手动绘制
        painter = QtGui.QPainter(self)  # 创建一个画家；告诉画在什么地方
        pen = QtGui.QPen(QtGui.QColor(20, 154, 151), 5)  # 创建并设置一个笔
        painter.setPen(pen)  # 把笔给画家
        painter.drawText(20, 70, self.text())  # 把按钮文字画在按钮上
        painter.drawEllipse(5, 5, 100, 120)  # 画个椭圆
```

#### 按钮事件

1. clicked   光标在按钮上时按下鼠标主键，并在不离开按钮前提下抬起，才发射本信号

2. pressed   按下按钮时触发

3. released  松开按钮时触发

4. toggled   按钮状态改变时触发（单选按钮、复选框等）

#### 自动重复

即按住按钮不松触发的频率

```py
# 设置是否开启自动重复，默认关闭
.setAutoRepeat(bool) 
# 设置触发自动重复的延时，即按住多长时间后才开始自动重复，单位为毫秒
.setAutoRepeatDelay(int)  
# 设置自动重复的时间间隔，单位为毫秒
.setAutoRepeatInterval(int) 

# 获取自动重复状态
.autoRepeat() -> bool  
# 获取自动重复延时，单位毫秒
.autoRepeatDelay() -> int   
# 获取自动重复时间间隔，单位毫秒
.autoRepeatInterval() -> int
```

#### 快捷键

```py
#为按钮设置键盘快捷键
.setShortcut(QKeySequence)   
button_2.setShortcut(QtGui.QKeySequence(Qt.CTRL + Qt.Key_A)) 
# 快速添加快捷键，按键为 Alt + 紧贴'&'符号后面的字母
button_1 = QtWidgets.QPushButton("&button1", self)

# 获取按钮的键盘快捷键
.shortcut() -> QKeySequence   
```

#### 排他性

设置排他性后选择一个单选按钮会取消其他复选框

```py
# 设置是否开启自动排他性，默认为false
.setAutoExclusive(bool)
# 获取按钮是否开启了自动排他性
.autoExclusive() -> bool   
```

### 普通按钮QPushButton

#### 创建方式

```py
# 单个参数，父对象默认值为None
QPushButton(parent = None)
#  两个参数，指定按钮上的文字
QPushButton(text[, parent = None])  
# 三个参数，指定按钮上的图标和文字
QPushButton(icon : QIcon | QPixmap, text[, parent = None])  

# 创建QIcon
QtGui.QIcon(filename : str)

# 单独设置属性
# 创建时父对象为None,可用setParent方法指定
button.setParent(self) 
# 设置按钮上的文字
button.setText("普通按钮")  
# 设置按钮上的图标
button.setIcon(icon)  
```

#### 扁平化

设置扁平化后，除非按钮被按下，大部分样式不会绘制按钮背景，实现视觉上的扁平化

```py
#  是否设置为扁平化，默认为否
.setFlat(bool)  
#  是否为扁平化
.isFlat() -> bool 
```

#### 菜单按钮

可以将普通按钮添加菜单而使其成为菜单按钮，一个按钮可以实现多个功能

```py
# 为按钮设置菜单
.setMenu(menu: QMenu)
# 获取按钮的菜单
.Menu() -> QMenu  
#  槽函数：打开按钮的菜单
.showMenu()           
```

#### 默认按钮与自动默认

1. default 属性设置为 true 的按钮（即对话框的默认按钮）将在用户按下 Enter 时自动被按下
2. 如果 autoDefault 按钮当前具有焦点，则按下 autoDefault 按钮
3. 当对话框有 autoDefault 按钮但没有默认按钮时，按 Enter 将按下当前具有焦点的 autoDefault 按钮，或者如果没有按钮具有焦点，则按下焦点链中的下一个 autoDefault 按钮

```py
# 设置为默认/非默认
.setDefault(bool) 
# 获取默认状态
.isDefault() -> bool 
# 设置为自动默认/非自动默认
.setAutoDefault(bool)
# 获取自动默认状态
.autoDefault() -> bool   
```

### 单选按钮QRadioButton

1. 默认开启排他性，即在一个按钮组中，只能同时有一个单选按钮被选中
2. 属于同一个父控件的多个单选按钮，有排他性

#### 创建方式

```py
QRadioButton(text: str, parent: QWidget=None)
QRadioButton(parent: QWidget=None)
```

#### 按钮组QButtonGroup

常用于控制单选按钮的互斥性：同组内的按钮间互斥，不同组的间互不影响

```py
# 创建按钮组，父控件为可选参数
.__init__(self, parent: Optional[QObject] = None) 
# 将按钮添加到按钮组中，可以同时为该按钮设置id
.addButton(button: QAbstractButton, id: int = -1)  
# 将按钮从按钮组中移除
.removeButton(button: QAbstractButton)                
```

### 复选框 QCheckBox

#### 创建方式

1. 复选框一般有两种选中状态（选中/未选中），有时则是三种（全部选中/部分选中/未选中）用于让用户勾选/取消勾选某些选项等
2. 复选框默认没有排他性，也可以通过QButtonGroup分组后用setAutoExclusive()方法开启

```py
.__init__(self, parent: Optional[PySide6.QtWidgets.QWidget] = None)
# 创建时即设置文字
.__init__(self, text: str, parent: Optional[PySide6.QtWidgets.QWidget] = None)  
```

#### 选中状态

```py
# 设置是否开启三态，默认关闭
.setTristate(y: bool = True) 
# 获取是否开启了三态
.isTristate() -> bool  
# 设置选中状态
.setCheckState(state: Qt.CheckState) 
# 获取选中状态
.checkState() -> Qt.CheckState         
```

#### Qt.CheckState

| Constant               | Value | Description |
| ---------------------- | ----- | ----------- |
| `Qt::Unchecked`        | `0`   | 未选中      |
| `Qt::PartiallyChecked` | `1`   | 部分选中    |
| `Qt::Checked`          | `2`   | 已选中      |

当状态被改变时，会发出QCheckBox.stateChanged信号，Qt.CheckState的value值，可传输connect一个槽函数进行处理

```py
    def test_01(self) -> None:
        """测试信号"""

        @QtCore.Slot(int)
        def test_slot(state: int) -> None:
            print(self.cb.stateChanged)
            if state == 2:
                print("复选框被选中了！")
            elif state == 0:
                print("复选框被取消选中了！")
            elif state == 1:
                print("复选框被部分选中！")

        self.cb.stateChanged.connect(test_slot)  # type: ignore
```

### 单行文本编辑器QLineEdit

#### 创建方式

1. 用户可以输入单行文本。适用于输入用户名等场景。

2. 如需输入多行文本、富文本，请使用QTextEdit控件。
3. 默认自动支持常见键盘操作，如移动光标、Home/End、复制粘贴等

```py
.__init__(self, arg__1: str, parent: Optional[QWidget] = None)
.__init__(self, parent: Optional[QWidget] = None)
```

创建后设置文本

```py
line_edit.setText("QLineEdit")
```

#### 显示模式

1. 默认显示模式为正常，即用户输入什么就显示什么
2. 也可以通过设置输入模式，使用户的输入被隐藏，常用于输入密码的场景
3. 改变显示模式不会影响编辑器中真实存储的文字，仍可正常获取

```py
# 设置显示模式
.setEchoMode(QLineEdit.EchoMode)
# 获取显示模式
.echoMode() -> QLineEdit.EchoMode  
```

| Constant                        | Value | Description                                                  |
| ------------------------------- | ----- | ------------------------------------------------------------ |
| `QLineEdit::Normal`             | `0`   | 按字符输入时的形式显示。默认值                               |
| `QLineEdit::NoEcho`             | `1`   | 不显示任何内容。常见场景：密码的长度也需要被保护，例如Linux输入密码 |
| `QLineEdit::Password`           | `2`   | 显示时用平台决定的密码掩码字符替代真实输入的字符             |
| `QLineEdit::PasswordEchoOnEdit` | `3`   | 当字符正在被编辑时显示，否则行为与Password相同               |

```py
# 返回LineEdit内的文本，与显示模式无关
.text() -> str
# 返回LineEdit中显示的文本。例如Password模式下可能会获得"*******"
.displayText() -> str         
```

#### 长度限制

1. 单行文本编辑器可以限制用户输入的最大字符长度。
2. 如果长度超出限制则会被在max处截断。
3. 如果设置了掩码（见本目录其他文档），则长度由掩码限制

```py
# 设置文本最大长度，默认值为67327
.setMaxLength(length: int)
# 返回最大长度限制
.maxLength() -> int             
```

#### 占位文本

1. 可以在用户未输入任何内容时设置一个占位文本，起到提示作用，
2. 例如“在此处输入用户名”。当用户开始编辑时消失。

```py
# 设置占位文本
.setPlaceholderText(text: str) 
# 返回占位文本
.placeholderText() -> str       
```

#### 只读模式

1. 可以开启只读模式，用户无法编辑其中的内容，与不可用（QWidget.setEnabled(False)）的区别在于：
   1. 用户仍然可以复制其中的文本到剪切板、拖动文本等。
   2. 在只读模式下，不会显示光标。

```py
# 设置是否开启只读模式，默认为False
.setReadOnly(yes: bool)   
#  获取只读状态
.isReadOnly() -> bool          
```

