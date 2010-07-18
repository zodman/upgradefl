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
        self.disable_button()
        self.disable_button("1")

    def disable_button( self,num =None):
        btns = self.glade.get_widget_prefix("button")
        for but in btns[:]:
            but.set_sensitive(False)
        if num is not None:
            self.glade.get_widget("button" +  num ).set_sensitive(True)
    def update_conary(self,widget):
        print "update conary"
        self.set_step_one()
    def update_all(self,widget):
        print "update all"
        self.set_step_two()
    def migrate(self,widget):
        print "migrate "
        gtk.main_quit()
    def set_step_one(self):
        self.disable_button("2")
    def set_step_two(self):
        self.disable_button("3")


    def connect_buttons(self):
        btn = self.glade.get_widget("button1")
        btn.connect("clicked",self.update_conary)
        btn = self.glade.get_widget("button2")
        btn.connect("clicked",self.update_all)
        btn = self.glade.get_widget("button3")
        btn.connect("clicked",self.migrate)

    def __init__(self):
        gladefile = 'upgrade.glade'
        self.glade = gtk.glade.XML(gladefile)
        win = self.glade.get_widget("window1")
        win.connect("destroy", gtk.main_quit )
        self.connect_buttons()
        self.set_step_zero()
        win.show_all()

        
def main():
    app = appgui()
    gtk.main()


if __name__ == "__main__":
    main()
