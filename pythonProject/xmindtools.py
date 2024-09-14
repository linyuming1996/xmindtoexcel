import tkinter as tk
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showinfo
from xmindtoexcel import xmind_to_xls
import re


# 定义MainUI类表示应用/窗口，继承Frame类
class MainUI(tk.Frame):
    # Application构造函数，master为窗口的父控件
    def __init__(self, master=None):
        # 初始化Application的Frame部分
        tk.Frame.__init__(self, master)
        # 显示窗口，并使用grid布局
        self.grid()
        self.path = tk.StringVar()
        # 创建控件
        self.createWidgets()

    def selectPath(self):
        '''选择要转换成excel的xmind地址'''
        self.path_ = askopenfilename()
        self.path.set(self.path_)

    # 创建控件
    def createWidgets(self):
        '''生成gui界面'''
        # 创建一个标签，输出要显示的内容
        self.firstLabel = tk.Label(self, text="目标路径")
        # 设定使用grid布局
        self.firstLabel.grid(row=0, column=0)
        self.firstEntry = tk.Entry(self, textvariable=self.path)
        self.firstEntry.grid(row=0, column=1)
        # 创建一个按钮，用来触发answer方法
        self.clickButton = tk.Button(self, text="路径选择", command=self.selectPath)
        # 设定使用grid布局
        self.clickButton.grid(row=0, column=2)
        self.clickButton = tk.Button(self, text="提交", command=self.getvalue)
        # 设定使用grid布局
        self.clickButton.grid(row=4, column=1)

    def getvalue(self):
        '''执行转换excel函数'''
        xmindPath = self.path.get()
        xmindPath = xmindPath.replace("/","\\")
        self.regvalue = '.*\.xmind$'
        self.xmind_reg = re.match(self.regvalue, xmindPath)
        if self.xmind_reg:
            # xmind转换成xls
            self.xmind_to_xls = xmind_to_xls()
            self.xmind_to_xls.run(xmindPath)
        else:
            showinfo(title='提示', message='请选择正确的xmind文件，谢谢！')


# 创建一个MainUI对象
app = MainUI()
# 设置窗口标题
app.master.title('Xmind 转 xls ')
# 设置窗体大小
app.master.geometry('290x90')
app.master.resizable(False, False)
# 主循环开始
app.mainloop()
