# coding: UTF-8
import wx  #导入包
class MyFrame(wx.Frame):  #子类化应用
    def __init__(self):    #定义一个应用程序的初始化方法
        wx.Frame.__init__(self, None, -1, "My Frame", size=(300, 300), )
        panel = wx.Panel(self, -1)
        panel.SetBackgroundColour('White')


        statusBar = self.CreateStatusBar()#创建状态栏
        toolbar = self.CreateToolBar() #创建工具栏
        #toolbar.AddSimpleTool(wx.NewId(), images.getNewBitmap(), "New", "Long help for'New") #给工具栏增加一个工具
        toolbar.Realize()  #准备显示工具栏

        menuBar = wx.MenuBar()
        menu1 = wx.Menu()
        menuBar.Append(menu1, "&File")
        menu2 = wx.Menu()
        menu2.Append(wx.NewId(), "&Copy", "Copy in status bar")
        menu2.Append(wx.NewId(), "&Cut", "")
        menu2.Append(wx.NewId(), "Paste", "")
        menu2.AppendSeparator()
        menu2.Append(wx.NewId(), "&Options...", "Display Options")
        menuBar.Append(menu2, "&Edit") # 在菜单栏上附上菜单
        self.SetMenuBar(menuBar)

        panel.Bind(wx.EVT_MOTION, self.OnMove)
        wx.StaticText(panel, -1,"Pos:", pos=(10, 12))
        self.posCtrl = wx.TextCtrl(panel, -1, "", pos=(40, 10))

        #创建按键
        button = wx.Button(panel, label = "Close", pos=(125, 50), size=(50,50))
        self.Bind(wx.EVT_BUTTON, self.OnCloseMe, button)
        #self.Bind(wx.EVT_CLOSE, self.OnCloseWidow)

    def OnCloseMe(self, evnet):
        self.Close(True)

    def OnCloseWidow(self,event):
        self.Destroy()

    def OnMove(self, event):
        pos = event.GetPosition()
        self.posCtrl.SetValue("%s, %s" %(pos.x, pos.y))

if __name__ =='__main__':
    app = wx.PySimpleApp()       #创建一个实例
    frame = MyFrame()
    frame.Show(True)
    app.MainLoop()    #事件主循环
