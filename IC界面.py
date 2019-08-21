#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.22
#  in conjunction with Tcl version 8.6
#    Apr 28, 2019 12:03:02 PM CST  platform: Windows NT

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True



def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
   
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)

    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("600x450+417+136")
        top.title("051-贴片-复合-分切用OfflineTestingRec")
        top.configure(background="#d9d9d9")

        self.style.configure('TNotebook.Tab', background=_bgcolor)
        self.style.configure('TNotebook.Tab', foreground=_fgcolor)
        self.style.map('TNotebook.Tab', background=
            [('selected', _compcolor), ('active',_ana2color)])
        self.TNotebook1 = ttk.Notebook(top)
        self.TNotebook1.place(relx=0.067, rely=0.111, relheight=0.68
                , relwidth=0.773)
        self.TNotebook1.configure(width=464)
        self.TNotebook1.configure(takefocus="")
        self.TNotebook1_t0 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t0, padding=3)
        self.TNotebook1.tab(0, text="离线测试记录",compound="left",underline="-1",)
        self.TNotebook1_t0.configure(background="#d9d9d9")
        self.TNotebook1_t0.configure(highlightbackground="#d9d9d9")
        self.TNotebook1_t0.configure(highlightcolor="black")
        self.TNotebook1_t1 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t1, padding=3)
        self.TNotebook1.tab(1, text="查询页面",compound="left",underline="-1",)
        self.TNotebook1_t1.configure(background="#d9d9d9")
        self.TNotebook1_t1.configure(highlightbackground="#d9d9d9")
        self.TNotebook1_t1.configure(highlightcolor="black")
        self.TNotebook1_t2 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t2, padding=3)
        self.TNotebook1.tab(2, text="填写测试记录",compound="left",underline="-1",)
        self.TNotebook1_t2.configure(background="#d9d9d9")
        self.TNotebook1_t2.configure(highlightbackground="#d9d9d9")
        self.TNotebook1_t2.configure(highlightcolor="black")
        self.TNotebook1_t3 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t3, padding=3)
        self.TNotebook1.tab(3, text="打印测试结果标签",compound="left",underline="-1",)
        self.TNotebook1_t3.configure(background="#d9d9d9")
        self.TNotebook1_t3.configure(highlightbackground="#d9d9d9")
        self.TNotebook1_t3.configure(highlightcolor="black")
        self.TNotebook1_t4 = tk.Frame(self.TNotebook1)
        self.TNotebook1.add(self.TNotebook1_t4, padding=3)
        self.TNotebook1.tab(4, text="使用说明",compound="left",underline="-1",)
        self.TNotebook1_t4.configure(background="#d9d9d9")
        self.TNotebook1_t4.configure(highlightbackground="#d9d9d9")
        self.TNotebook1_t4.configure(highlightcolor="black")
       

        # self.TLabelframe1 = ttk.Labelframe(self.TNotebook1_t0)
        # self.TLabelframe1.place(relx=0.041, rely=0.073, relheight=0.136
        #         , relwidth=0.932)
        # self.TLabelframe1.configure(relief='')
        # self.TLabelframe1.configure(text='''You can do it''')
        # self.TLabelframe1.configure(width=690)

        # self.TCombobox1 = ttk.Combobox(self.TLabelframe1)
        # self.TCombobox1.place(relx=0.188, rely=0.533, relheight=0.28
        #         , relwidth=0.207, bordermode='ignore')
        # self.value_list = [DC1,AC,]
        # self.TCombobox1.configure(values=self.value_list)
        # self.TCombobox1.configure(show="vfd   ?")
        # self.TCombobox1.configure(textvariable=inter_support.combobox)
        # self.TCombobox1.configure(foreground="#000000")
        # self.TCombobox1.configure(takefocus="")
        # tooltip_font = "TkDefaultFont"
        # ToolTip(self.TCombobox1, tooltip_font, '''??''', delay=0.5)

if __name__ == '__main__':
    vp_start_gui()





