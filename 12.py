#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.22
#  in conjunction with Tcl version 8.6
#    Apr 28, 2019 12:03:02 PM CST  platform: Windows NT

import sys
# import  datetime
import time
# from datetime import datetime
# import tkinter


# try:
#     import Tkinter as tk
# except ImportError:
import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True



datestr=time.strftime('%y,%m,%d')
print(datestr)

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

    #设置变量
    var=tkinter.StringVar()
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

        top.geometry("900x700+200+6")
        top.title("051-贴片-复合-分切用OfflineTestingRec")
        top.configure(background="#d9d9d9")

        self.style.configure('TNotebook.Tab', background=_bgcolor)
        self.style.configure('TNotebook.Tab', foreground=_fgcolor)
        self.style.map('TNotebook.Tab', background=
            [('selected', _compcolor), ('active',_ana2color)])
        self.TNotebook1 = ttk.Notebook(top)
        self.TNotebook1.place(relx=0.01, rely=0.013, relheight=0.98
                , relwidth=0.98)
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
       

        self.TLabelframe1 = ttk.Labelframe(self.TNotebook1_t0)
        self.TLabelframe1.place(relx=0.009, rely=0.009, relheight=0.1
                , relwidth=0.99)
        self.TLabelframe1.configure(relief='')
        self.TLabelframe1.configure(text='''查询并导入班别信息''')
        self.TLabelframe1.configure(width=690)

        self.TCombobox1 = ttk.Combobox(self.TLabelframe1)
        self.TCombobox1.place(relx=0.07, rely=0.5, relheight=0.4
                , relwidth=0.09, bordermode='ignore')
        self.value_list = ["","贴合","复合","分切"]
        self.TCombobox1.configure(values=self.value_list)
        self.TCombobox1.configure(state='readonly')
        self.TCombobox1.configure(values=self.value_list)
        self.TCombobox1.configure(show="")
        self.TCombobox1.configure(textvariable=True)
        self.TCombobox1.configure(foreground="#000000")
        self.TCombobox1.configure(takefocus="")

        tooltip_font = "TkDefaultFont"
        ToolTip(self.TCombobox1, tooltip_font, self.value_list, delay=0.5)
        
        self.Label1 = tk.Label(self.TLabelframe1)
        self.Label1.place(relx=0.001, rely=0.50, height=22, width=50
                , bordermode='ignore')
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(font="-family {Segoe UI Black} -size 10 -weight bold")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#efb1d0")
        self.Label1.configure(text='''工序''')
        self.Label1.configure(width=50)

        self.TCombobox2 = ttk.Combobox(self.TLabelframe1)
        self.TCombobox2.place(relx=0.25, rely=0.5, relheight=0.4
                , relwidth=0.10, bordermode='ignore')
        self.value_list = ["DC1","DC2","DC3","10K2","10K3","15K1","15K2","15K3","15K4","15K5","15K6","15K7","15K8","DDA1","DDA2","Edla","TAL165-1","LsLitter","Leomat2"]
        self.TCombobox2.configure(values=self.value_list)
        self.TCombobox2.configure(state='readonly')
        self.TCombobox2.configure(values=self.value_list)
        # self.TCombobox2.configure(textvariable=inter_support.combobox)
        self.TCombobox2.configure(width=83)
        self.TCombobox2.configure(takefocus="")

        self.Label2 = tk.Label(self.TLabelframe1)
        self.Label2.place(relx=0.18, rely=0.5, height=22, width=50
                , bordermode='ignore')
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(font="-family {Segoe UI Black} -size 10 -weight bold")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#efb1d0")
        self.Label2.configure(text='''机台''')
        self.Label2.configure(width=50)


        self.TCombobox3 = ttk.Combobox(self.TLabelframe1)
        self.TCombobox3.place(relx=0.45, rely=0.5, relheight=0.4
                , relwidth=0.10, bordermode='ignore')
        self.value_list = ["A","A1","N","N1","B","B1","N","N1","C","C1","Oth"]
        self.TCombobox3.configure(values=self.value_list)
        self.TCombobox3.configure(state='readonly')
        self.TCombobox3.configure(values=self.value_list)
        # self.TCombobox2.configure(textvariable=inter_support.combobox)
        self.TCombobox3.configure(width=83)
        self.TCombobox3.configure(takefocus="")
        self.Label3 = tk.Label(self.TLabelframe1)
        self.Label3.place(relx=0.37, rely=0.5, height=22, width=50
                , bordermode='ignore')
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(font="-family {Segoe UI Black} -size 10 -weight bold")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#efb1d0")
        self.Label3.configure(text='''班别''')
        self.Label3.configure(width=50)

        self.Text1 = tk.Text(self.TLabelframe1)
        self.Text1.place(relx=0.63, rely=0.5, relheight=0.4, relwidth=0.1
                , bordermode='ignore')
        
        self.Text1.configure(background="white")
        self.Text1.configure(font="TkTextFont")
        self.Text1.configure(foreground="black")
        self.Text1.configure(highlightbackground="#d9d9d9")
        self.Text1.configure(highlightcolor="black")
        self.Text1.configure(insertbackground="black")
        self.Text1.configure(selectbackground="#c4c4c4")
        self.Text1.configure(selectforeground="black")
        self.Text1.configure(width=50)
        self.Text1.configure(wrap="word")
        # self.Text1.configure(text='datestr')

        self.Label4 = tk.Label(self.TLabelframe1)
        self.Label4.place(relx=0.56, rely=0.5, height=22, width=50
                , bordermode='ignore')
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(font="-family {Segoe UI Black} -size 10 -weight bold")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#efb1d0")
        self.Label4.configure(text='''日期''')
        self.Label4.configure(width=50)
# ======================================================
# Modified by Rozen to remove Tkinter import statements and to receive
# the font as an argument.
# ======================================================
# Found the original code at:
# http://code.activestate.com/recipes/576688-tooltip-for-tkinter/
# ======================================================

from time import time, localtime, strftime
    
class ToolTip(tk.Toplevel):
    """
    Provides a ToolTip widget for Tkinter.
    To apply a ToolTip to any Tkinter widget, simply pass the widget to the
    ToolTip constructor
    """
    def __init__(self, wdgt, tooltip_font, msg=None, msgFunc=None,
                 delay=1, follow=True):
        """
        Initialize the ToolTip

        Arguments:
          wdgt: The widget this ToolTip is assigned to
          tooltip_font: Font to be used
          msg:  A static string message assigned to the ToolTip
          msgFunc: A function that retrieves a string to use as the ToolTip text
          delay:   The delay in seconds before the ToolTip appears(may be float)
          follow:  If True, the ToolTip follows motion, otherwise hides
        """
        self.wdgt = wdgt
        # The parent of the ToolTip is the parent of the ToolTips widget
        self.parent = self.wdgt.master
        # Initalise the Toplevel
        tk.Toplevel.__init__(self, self.parent, bg='black', padx=1, pady=1)
        # Hide initially
        self.withdraw()
        # The ToolTip Toplevel should have no frame or title bar
        self.overrideredirect(True)

        # The msgVar will contain the text displayed by the ToolTip
        self.msgVar = tk.StringVar()
        if msg is None:
            self.msgVar.set('No message provided')
        else:
            self.msgVar.set(msg)
        self.msgFunc = msgFunc
        self.delay = delay
        self.follow = follow
        self.visible = 0
        self.lastMotion = 0
        # The text of the ToolTip is displayed in a Message widget
        tk.Message(self, textvariable=self.msgVar, bg='#FFFFDD',
                font=tooltip_font,
                aspect=1000).grid()

        # Add bindings to the widget.  This will NOT override
        # bindings that the widget already has
        self.wdgt.bind('<Enter>', self.spawn, '+')
        self.wdgt.bind('<Leave>', self.hide, '+')
        self.wdgt.bind('<Motion>', self.move, '+')

    def spawn(self, event=None):
        """
        Spawn the ToolTip.  This simply makes the ToolTip eligible for display.
        Usually this is caused by entering the widget

        Arguments:
          event: The event that called this funciton
        """
        self.visible = 1
        # The after function takes a time argument in miliseconds
        self.after(int(self.delay * 1000), self.show)

    def show(self):
        """
        Displays the ToolTip if the time delay has been long enough
        """
        if self.visible == 1 and time() - self.lastMotion > self.delay:
            self.visible = 2
        if self.visible == 2:
            self.deiconify()

    def move(self, event):
        """
        Processes motion within the widget.
        Arguments:
          event: The event that called this function
        """
        self.lastMotion = time()
        # If the follow flag is not set, motion within the
        # widget will make the ToolTip disappear
        #
        if self.follow is False:
            self.withdraw()
            self.visible = 1

        # Offset the ToolTip 10x10 pixes southwest of the pointer
        self.geometry('+%i+%i' % (event.x_root+20, event.y_root-10))
        try:
            # Try to call the message function.  Will not change
            # the message if the message function is None or
            # the message function fails
            self.msgVar.set(self.msgFunc())
        except:
            pass
        self.after(int(self.delay * 1000), self.show)

    def hide(self, event=None):
        """
        Hides the ToolTip.  Usually this is caused by leaving the widget
        Arguments:
          event: The event that called this function
        """
        self.visible = 0
        self.withdraw()




# ===========================================================
#                   End of Class ToolTip
# ===========================================================

if __name__ == '__main__':
    vp_start_gui()





