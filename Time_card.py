from tkinter import *
import time
import os


class Project_timer(Frame):
    def __init__(self, parent=None, **kw):
        self.frame = Frame.__init__(self, parent, kw, bg='#29323b')
        self._start = 0.0
        self._elapsedtime = 0.0
        self._running = 0
        self.timestr = StringVar()
        self.proj = StringVar()
        self.makeWidgets()


    def makeWidgets(self):
        h = 20
        w = 100
        labelProject = Label(self, text="Project", bg='#29323b', fg='#ebe8dd').grid(row=0, column=0)
        entryProject = Entry(self, textvariable=self.proj, bg='#627eab', fg='#ebe8dd', justify='center').grid(row=1, column=0, sticky='news')
        buttonStart = Button(self, text='Start', command=self.Start, bg='#627eab', fg='#82ff91').grid(row=3, column=0, sticky='news')
        buttonStop = Button(self, text='Stop', command=self.Stop, bg='#627eab', fg='#ff8b80').grid(row=4, column=0, sticky='news')
        buttonReset = Button(self, text='Reset', command=self.Reset, bg='#627eab', fg='#ebe8dd').grid(row=5, column=0, sticky='news')
        cumTime = Label(self, textvariable=self.timestr, bg='#29323b', fg='#ebe8dd').grid(row=6, column=0, sticky='news')
        self._setTime(self._elapsedtime)

    def _update(self):
        self._elapsedtime = time.time() - self._start
        self._setTime(self._elapsedtime)
        self._timer = self.after(50, self._update)

    def _setTime(self, elap):
        hours = int(elap/3600)
        minutes = int((elap - hours*3600.0)/60)
        seconds = int(elap - hours*3600.0 - minutes*60.0)
        self.timestr.set('{}:{}:{}'.format(hours, minutes, seconds))

    def Start(self):
        if not self._running:
            self._start = time.time() - self._elapsedtime
            #self._update()
            self._running = 1
            self.timestr.set('Running')

    def Stop(self):
        if self._running:
            #self.after_cancel(self._timer)
            self._elapsedtime = time.time() - self._start
            self._setTime(self._elapsedtime)
            self._running = 0

    def Reset(self):
        self._start = time.time()
        self._elapsedtime = 0.0
        self._setTime(self._elapsedtime)


def add_project(root):
    width = root.winfo_width()
    if width == 124:
        width = 0
    root.geometry('{}x200'.format(width+125))
    sw = Project_timer(root)
    sw.pack(side=LEFT)


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def main():
    root = Tk()
    root.title('Time card')
    root.geometry('124x50')
    root.configure(background='#324159')
    root.iconbitmap(resource_path('timer_icon.ico'))

    # frame = Frame(root)
    inspiration = Label(root, text='Have a good day', bg='#324159', fg='#ebe8dd').pack(side=TOP)
    addButton = Button(root, text='Add Project', command=lambda:add_project(root), bg='#627eab', fg='#ebe8dd').pack(side=BOTTOM)
    # sw = Project_timer(root)
    # sw.pack(side=TOP)
    root.mainloop()

if __name__ == '__main__':
    main()
# from datetime import datetime
# root = tk.Tk()
# root.geometry('400x200+100+200')
# root.title('Time card')
#
# def startTime():
#     now = datetime.now()
#
#
# proj = tk.StringVar()
# labelProject = tk.Label(root, text = "Project Name").grid(row=0, column=0)
# entryProject = tk.Entry(root, textvariable=proj).grid(row=1, column=0)
# buttonStart = tk.Button(root, text="Start", command=startTime).grid(row=2, column=0)
#
# root.mainloop()