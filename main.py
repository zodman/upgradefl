import pygtk
import gtk
import gtk.glade


class appgui:
    def set_text(self,text):
        buff = gtk.TextBuffer()
        buff.set_text(text)
        return buff
    def set_text_intro(self):
        textviewer = self.glade.get_widget("textview1")
        custom_text = """Updates to Foresight are now available.  For a variety of technical reasons, the update process is temporarily more complex than usual.  After this update process is complete,your update process will return to normal.\n
In order to complete this update process, you should first close running programs."""
        textviewer.set_buffer(self.set_text(custom_text))
    def set_step_zero(self):
        self.set_text_intro()
        btn1 = self.glade.get_widget("button1")
        btn1.set_sensitive(False)

        
    def set_step_one():
        pass
    def set_step_two():
        pass
    def set_step_three():
        pass
    def __init__(self):
        gladefile = 'upgrade.glade'
        self.glade = gtk.glade.XML(gladefile)
        win = self.glade.get_widget("window1")
        self.set_step_zero()
        win.show_all()

        
def main():
    app = appgui()
    gtk.main()


if __name__ == "__main__":
    main()
