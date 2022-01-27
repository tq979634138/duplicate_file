import wx
from Operate_file import *

class MinUi(wx.App):
    def OnInit(self):  #初始化接口，子类覆盖父类的方法
        frame = wx.Frame(parent=None,title="删除重复文件", size=(600, 600))  #新建框架
        frame.Centre()
        self.panel = wx.Panel(frame, -1)
        button = wx.Button(self.panel, -1, "选择", pos=(500, 10))
        button.Bind(wx.EVT_BUTTON, self.open_file)
        bt_a = wx.Button(self.panel, -1, "扫描", pos=(500, 35))
        bt_a.Bind(wx.EVT_BUTTON, self.get_path)
        bt_b = wx.Button(self.panel, -1, "删除", pos=(500, 70))
        bt_b.Bind(wx.EVT_BUTTON, self.action)
        self.text_path = wx.TextCtrl(self.panel, pos=(10, 10), size=(480, 50), value="文件夹路径")
        self.text_path.Bind(wx.EVT_LEFT_DCLICK, self.clear_text)
        font1 = wx.Font(15, wx.MODERN, wx.NORMAL, wx.NORMAL, False, 'Consolas')
        self.text_path.SetFont(font1)
        frame.Show()
        return True

    def open_file(self, event):
        dlg = wx.DirDialog(None, "选择文件夹", style=wx.DD_DEFAULT_STYLE)
        if dlg.ShowModal() == wx.ID_OK:
            self.text_path.SetValue(dlg.GetPath())
        dlg.Destroy()

    def clear_text(self, event):
        self.text_path.SetValue("")

    def get_path(self, event):
        self.path = self.text_path.GetValue()
        if os.path.isdir(self.path):
            self.file_li = operate(self.path)
            self.listbox = wx.CheckListBox(self.panel, -1, (10, 70), (480, 480), self.file_li)
        else:
            tone = wx.MessageDialog(None, "文件路径错误", "警告！！！", wx.ICON_EXCLAMATION | wx.YES_DEFAULT)
            if tone.ShowModal() == wx.ID_YES:
                tone.Destroy()

    def action(self, event):
        check = self.listbox.GetCheckedItems()
        dia = wx.MessageDialog(None, "你确定要删除这些文件吗？", "文件删除确认!", wx.YES_NO | wx.ICON_QUESTION)
        if dia.ShowModal() == wx.ID_YES:
            for i in check:
                file_path = self.path + "/" + self.file_li[i]
                delete_file(file_path)
        dia.Destroy()



app = MinUi()
app.MainLoop()