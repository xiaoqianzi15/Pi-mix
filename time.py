
import time  # 导入此模块，获取当前时间
import tkinter # 导入控件

#设定界面
top = tkinter.Tk()
top.title('宝宝爱美丽')#标题
#添加label组件
label = tkinter.Label(master = top, text = '请输入小时')
label.pack()

entry = tkinter.Entry(master = top)
entry.pack()
#添加button 组件
button = tkinter.Button(master = top, text = '提交')
button.pack()


top.mainloop()

# 设置定时时间
hour = 3
minute = 0
sec = 0

flag = 1
while flag:
    if sec<1 and minute>0:
        minute = minute -1
        sec = 60
    if minute<1 and hour>0:
        hour = hour -1
        minute = 60
    if hour == 0 and minute ==0 and sec ==0:
        print("time out")
        flag = 0
    sec = sec - 1
    
    time.sleep(1)
    print("hour:", hour,"minute:", minute,"sec:", sec)
