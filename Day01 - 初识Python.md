## Day01 - 初识Python

今天是学习Python的第一天，自此开始用笔记来记录学习，希望可以坚持下去。

学习用的教材是GitHub上骆昊编写的[《Python - 100天从新手到大师》](https://github.com/jackfrued/Python-100-Days)

所有编写的源代码均放在GitHub上：[https://github.com/svip886/Python_learning](https://github.com/svip886/Python_learning)

### 一、环境配置
1. 下载安装
   
   Python官网：[https://www.python.org/](https://www.python.org/)
   
   Python学习使用版本为**V3.6.6**（之前就装了的，以后需要再升级好了）

2. 安装事项
   
   安装过程中应当注意添加环境变量Path，方便直接在命令行使用python

3. Python编辑器
   
   使用**VS Code**来写Python

### 二、运行Python程序
1. **确认Python版本**
    
    1. 直接使用命令行运行
    ```python
    python --version
    # Linux或Macos下应当使用
    # python3 --version
    ```

    2. 先输入`python`或`python3`进入交互环境,再执行
   
    ```python
    import sys
    print(sys.version_info)
    print(sys.version)
    ```

2. **编写Python源代码**

    💡第一个程序肯定是helloworld无疑了，不过相较于C语言，Python不需要先载入头文件，写函数体，输出语句只靠一句代码解决
    ```python
    print('Hello,World!')
    ```

3. **运行程序**

    1. 在VS Code中，直接按Crtl+F5运行
    
    2. 保存为.py后缀形式，在命令行中打开

4. **代码中的注释**

    1. 单行注释 - 以#和空格开头后的部分
    
    2. 多行注释 - 以3个双引号开头，3个双引号结尾

    代码示例：
    ```python
    """
    第一个Python程序 - Hello，World！
    
    Version: 0.1
    Author: Paranoid
    """

    print('Hello,World!')
    # print('你好，世界！')
    ```

### 三、练习

1. 在Python交互式环境中输入下面的代码并查看结果，请尝试将看到的内容翻译成中文。
    ```python
    import this
    ```
    
    输出结果为：
    ![The_Zen_of_Python](https://s3.ax1x.com/2021/01/18/s6SnLq.png)

2. 学习使用turtle在屏幕上绘制图形。

    1. 画布（canvas）

        以坐标系的形式来表示画布上各个点

        ```python
        turtle.screensize(canvwidth=None, canvheight=None, bg=None)
        # 参数分别为画布的宽(单位像素), 高, 背景颜色。
        ```

    2. 画笔

        默认点为坐标系原点，以一只小乌龟的形式来表示，绘图过程中，有两个参数，一个是位置，一个是方向

        ```python
        turtle.pensize() 
        # 设置画笔的宽度；
        turtle.pencolor()
        # 没有参数传入，返回当前画笔颜色，传入参数设置画笔颜色，可以是字符串如"green", "red",也可以是RGB 3元组。
        turtle.speed(speed)
        # 设置画笔移动速度，画笔绘制的速度范围[0,10]整数，数字越大越快。

        turtle.forward(200)
        # 设置笔划长度
        turtle.right(180)
        # 设置向右转（顺时针）的角度，同理可以使用向左
        ```
        
     3. 教程示例
    
        ```python
        import turtle
        
        turtle.pensize(4)
        turtle.pencolor('red')
        
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(100)
        
        turtle.mainloop()
        ```
