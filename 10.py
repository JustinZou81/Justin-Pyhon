from tkinter import *
 
root=Tk()
#每行显示一句：每句5个汉字加一个中文标点符号（英文为6）warplength=5*12+12
Lab1=Label(root,bg='red',text='床前明月光，疑是地上霜，举头望明月，低头思故乡。',width=24,height=4,wraplength=72,justify='left').pack()
#height与默认的汉字高度约一致，一个汉字约为2个单位的width
Lab2=Label(root,bg='Green',text='疑是地上霜',width=18,height=5,wraplength=12,anchor='nw').pack()
Lab3=Label(root,bg='Yellow',text='举头望明月',width=18,height=2,anchor='ne',justify='right').pack()
root.mainloop()
