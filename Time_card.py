from tkinter import *
import time
import os

frames = []
root = Tk()


def parse_geometry(geometry):
    geometry = geometry.replace('x', '+')
    geometry = geometry.split('+')
    for i in range(len(geometry)):
        geometry[i] = int(geometry[i].strip())
    return geometry


def trigger_start(func):
    global frames

    def wrapper(self):
        for i in range(len(frames)):
            if i > 0:
                frames[i].Stop()
        func(self)
    return wrapper


def list_ids():
    global frames
    id_list = [0]
    for i in range(len(frames)):
        if i > 0:
            id_list.append(frames[i]._id)
    return id_list


def trigger_close(func):
    global root
    global frames

    def wrapper(self):
        geometry = parse_geometry(root.geometry())
        if len(frames) > 2:
            frame_size = int(geometry[0] / (len(frames) - 1))
            width = geometry[0] - frame_size
            root.geometry("{}x{}".format(width, geometry[1]))
        root.geometry('+{}+{}'.format(geometry[2], geometry[3]))
        ids = self._id
        func(self)
        id_list = list_ids()
        ind = id_list.index(ids)
        del frames[ind]
    return wrapper


class ProjectTimer(Frame):
    def __init__(self, parent=None, nframes=0, **kw):
        self.frame = Frame.__init__(self, parent, kw, bg='#29323b')
        self._start = 0.0
        self._elapsedtime = 0.0
        self._id = nframes
        self._running = -1
        self.timestr = StringVar()
        self.proj = StringVar(value='Project {}'.format(self._id))
        self.makeWidgets()

    def makeWidgets(self):
        topframe = Frame(self)
        topframe.pack(side=TOP, expand=YES, fill=BOTH)
        bottomframe = Frame(self)
        bottomframe.pack(side=BOTTOM, expand=YES, fill=BOTH)
        top_widgets = []
        bottom_widgets = []
        top_widgets.append(Entry(topframe, textvariable=self.proj, bg='#29323b', fg='#ebe8dd', justify='center'))
        top_widgets.append(Button(topframe, text="X", command=self.Close, bg='#29323b', fg='#ebe8dd'))
        bottom_widgets.append(Button(bottomframe, text='Start', command=self.Start, bg='#627eab', fg='#82ff91'))
        bottom_widgets.append(Button(bottomframe, text='Stop', command=self.Stop, bg='#627eab', fg='#ff8b80'))
        bottom_widgets.append(Button(bottomframe, text='Reset', command=self.Reset, bg='#627eab', fg='#ebe8dd'))
        bottom_widgets.append(Label(bottomframe, textvariable=self.timestr, bg='#29323b', fg='#ebe8dd'))
        for widget in top_widgets:
            widget.pack(side=LEFT, expand=YES, fill=BOTH)
        for widget in bottom_widgets:
            widget.pack(side=TOP, expand=YES, fill=BOTH)
        self._setTime(self._elapsedtime)
        top_widgets[0].focus()

    def _setTime(self, elp):
        hours = int(elp/3600)
        minutes = int((elp - hours*3600.0)/60)
        seconds = int(elp - hours*3600.0 - minutes*60.0)
        self.timestr.set('{}:{}:{}'.format(hours, minutes, seconds))

    @trigger_close
    def Close(self):
        self.Stop()
        self.pack_forget()
        self.destroy()

    @trigger_start
    def Start(self):
        if not self._running == self._id:
            self._start = time.time() - self._elapsedtime
            self._running = self._id
            self.timestr.set('Active')

    def Stop(self):
        if self._running == self._id:
            self._elapsedtime = time.time() - self._start
            self._setTime(self._elapsedtime)
            self._running = -1

    def Reset(self):
        self._start = time.time()
        self._elapsedtime = 0.0
        self._setTime(self._elapsedtime)


def add_project():
    global frames
    global root
    geometry = parse_geometry(root.geometry())
    if len(frames) > 1:
        frame_size = int(geometry[0]/(len(frames) - 1))
        width = geometry[0] + frame_size
        root.geometry("{}x{}".format(width, geometry[1]))
    else:
        root.geometry("")
    id_list = list_ids()
    new_id = max(id_list) + 1
    sw = ProjectTimer(root, new_id)
    sw.pack(side=LEFT, expand=YES, fill=BOTH)
    frames.append(sw)
    geometry = parse_geometry(root.geometry())


def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def main():
    global frames
    global root
    root.title('Time card')
    frames.append(root)

    # Sets background color of the frame and sets icon
    # TODO:  Needs to be tested with windows and mac
    root.configure(background='#324159')
    icon_image = PhotoImage(file=resource_path('Timer.png'))
    root.iconphoto(True, icon_image)

    # Add the buttons to the main window
    inspiration = Label(root, text='Have a good day', bg='#324159', fg='#ebe8dd').pack(side=TOP)
    addButton = Button(root, text='Add Project', command=lambda: add_project(), bg='#627eab', fg='#ebe8dd').pack(side=BOTTOM)
    root.pack_propagate(1)
    root.mainloop()


if __name__ == '__main__':
    main()

