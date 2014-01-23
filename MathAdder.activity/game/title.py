import spyral
import sys
from constants import images, SIZE

BG_COLOR = (255, 255, 255)

class TabletInstructions(spyral.Sprite): pass

class PreTitleScene(spyral.Scene):
    def __init__(self):
        spyral.scene.Scene.__init__(self, SIZE)
        self.background = spyral.Image(size=SIZE)
        self.load_style("game/title.spys")
        
        instructions = TabletInstructions(self)
        instructions.pos = self.rect.center
        
        self.register("system.quit", sys.exit)
        self.register("input.keyboard.down.*", self.goto_title)
    
    def goto_title(self):
        spyral.director.replace(TitleScene())
        
class TitleScene(spyral.Scene):
    def __init__(self):
        spyral.scene.Scene.__init__(self, SIZE)
        self.load_style("game/title.spys")

        class MainMenu(spyral.Form):
            start = spyral.widgets.Button("Start")
            characters = spyral.widgets.Button("Characters")
            help = spyral.widgets.Button("Help")
            quit = spyral.widgets.Button("Quit")
        main_menu = MainMenu(self)
        main_menu.anchor = 'center'
        main_menu.pos = self.rect.center
        main_menu.focus(main_menu.start)
        
        self.register("system.quit", sys.exit)
        #self.register("form.RegisterForm.okay.changed", test_print)
        #self.register("form.RegisterForm.name.changed", test_react)
        #self.register("director.update", self.report_boxes)

