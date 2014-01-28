import spyral
import sys
from constants import images, SIZE, model, strings

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
        self.register("input.mouse.down.*", self.goto_title)
    
    def goto_title(self):
        spyral.director.push(TitleScene())
        
test = None
class TitleScene(spyral.Scene):
    def __init__(self):
        global test
        spyral.scene.Scene.__init__(self, SIZE)
        self.load_style("game/title.spys")

        class MainMenu(spyral.Form):
            start = spyral.widgets.Button("")
            characters = spyral.widgets.Button("")
            quit = spyral.widgets.Button("")
        main_menu = MainMenu(self)
        main_menu.pos = self.rect.center
        main_menu.anchor = 'center'
        main_menu.start.anchor = "center"
        main_menu.characters.anchor = "center"
        main_menu.quit.anchor = "center"
        main_menu.focus(main_menu.start)
        test = main_menu
        
        self.register("system.quit", sys.exit)
        self.register("form.MainMenu.quit.changed", sys.exit)
        self.register("form.MainMenu.characters.changed", self.goto_characters)
        self.chars = CharacterSelect()

    def goto_characters(self):
        print "in"
        spyral.director.push(self.chars)
        
class SnakeSelector(spyral.Sprite):
    def __init__(self, scene):
        spyral.Sprite.__init__(self, scene)
        self.snake = model["snake"]
        self.color = model["color"]
        self.set_image()
        
    def set_image(self):
        self.image = spyral.Image(images["snakes"][self.snake+"_selector_"+self.color])
        
    def update(self):
        model["snake"] = self.snake
        model["color"] = self.color
        self.image = spyral.Image(images["snakes"][self.snake+"_selector_"+self.color])

class CharacterSelect(spyral.Scene):
    def __init__(self):
        spyral.scene.Scene.__init__(self, SIZE)
        self.load_style("game/title.spys")
        
        class CharacterSelectForm(spyral.Form):
            colors = spyral.widgets.Button("")
            okay = spyral.widgets.Button("Okay")
        self.characters = CharacterSelectForm(self)
        self.characters.pos = self.rect.center
        self.characters.anchor = 'center'
        self.characters.focus(self.characters.colors)
        
        self.selector = SnakeSelector(self)
        
        self.register("system.quit", sys.exit)
        self.register("form.CharacterSelectForm.okay.changed", self._exit)
        self.register("input.keyboard.down.down", self.track)
        
    def _exit(self):
        print "out"
        spyral.director.pop()
        
    def track(self):
        import objgraph
        objgraph.show_backrefs([test], filename='sample-graph.png')
    #snake+"_button"
    #snake+"_highlight_"+direction
    #snake+"_selector_"+color
    #snake+"_body_"+color+direction
    #snake+"_head_fine_"+color+direction
    #snake+"_head_dead_"+color+direction
    