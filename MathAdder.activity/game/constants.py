from os import path

SIZE = (1200, 900)

model = {"snake" : "adder", "color": "0"}

strings = {}
strings['names'] = {"adder" : "Adder Adam",
                    "anaconda" : "Sal Amander",
                    "diamondback" : "Darryl Diamondback",
                    "caterpillar" : "Colonel Caterpillar"}

images = {}
images['background_pretitle'] = path.join('game','images','backgrounds', 'pretitle.png')
images['background_level'] = path.join('game','images','backgrounds', 'level.png')
images['background_title'] = path.join('game','images','backgrounds', 'title.png')
images['background_characters'] = path.join('game','images','backgrounds', 'characters.png')
snake_images = images["snakes"] = {}
for snake in strings['names'].iterkeys():
    snake_images[snake+"_button"] = path.join("game","images","forms",snake+".png")
    for direction in ("E", "N", "S", "W"):
        snake_images[snake+"_highlight_"+direction] = path.join("game","images","characters",snake,"60", "Highlight_"+direction+".png")
    for color in ("0", "1", "2"):
        snake_images[snake+"_selector_"+color] = path.join("game","images","characters",snake,"CharSelect",color+".png")
        for direction in ("E", "N", "S", "W"):
            snake_images[snake+"_body_"+color+direction] = path.join("game","images","characters",snake,"60",color, "Body_"+direction+".png")
            snake_images[snake+"_head_fine_"+color+direction] = [
                path.join("game","images","characters",snake,"60",color, "Head_"+direction+str(frame)+".png")
                    for frame in xrange(0, 6)]
            snake_images[snake+"_head_dead_"+color+direction] = path.join("game","images","characters",snake,"60",color, "Head_"+direction+"6.png")
	
	#images['menu_title'] = spyral.util.load_image(path.join('games/snake/Images/Other', 'menu_title.png'))
	#images['character_title'] = spyral.util.load_image(path.join('games/snake/Images/Other', 'character_title.png'))
	#images['button_normal'] = spyral.util.load_image(path.join('games/snake/Images/Other', 'Button0.png'))
	#images['button_highlight'] = spyral.util.load_image(path.join('games/snake/Images/Other', 'Button2.png'))
	#images['color_select'] = spyral.util.load_image(path.join('games/snake/Images/Other', 'color_select.png'))
"""
	images['button_start'] = (spyral.util.load_image(path.join('games/snake/Images/Other/Buttons', 'Play0.png')),
							  spyral.util.load_image(path.join('games/snake/Images/Other/Buttons', 'Play1.png')))
	images['button_charselect'] = (spyral.util.load_image(path.join('games/snake/Images/Other/Buttons', 'CharSelect0.png')),
							 	   spyral.util.load_image(path.join('games/snake/Images/Other/Buttons', 'CharSelect1.png')))
	images['button_quit'] = (spyral.util.load_image(path.join('games/snake/Images/Other/Buttons', 'Quit0.png')),
						     spyral.util.load_image(path.join('games/snake/Images/Other/Buttons', 'Quit1.png')))
	
	images['button_help'] = (spyral.util.load_image(path.join('games/snake/Images/Other/Buttons', 'Help0.png')),
						     spyral.util.load_image(path.join('games/snake/Images/Other/Buttons', 'Help1.png')))
	
	
	images['adderColors'] = []
	for i in range(3):
		images['adderColors'].append(spyral.util.load_image(path.join('games/snake/Images/Adder/CharSelect', '%d.png' % i)))
	
	images['condaColors'] = []
	for i in range(3):
		images['condaColors'].append(spyral.util.load_image(path.join('games/snake/Images/Anaconda/CharSelect', '%d.png' % i)))
	
	images['diamondColors'] = []
	for i in range(3):
		images['diamondColors'].append(spyral.util.load_image('games/snake/Images/Diamondback/CharSelect/' + str(i) + '.png'))

	images['caterpillarColors'] = []
	for i in range(3):
		images['caterpillarColors'].append(spyral.util.load_image('games/snake/Images/Caterpillar/CharSelect/'+str(i)+'.png'))
	
	images['characters'] = [images['adderColors'],images['condaColors'],images['diamondColors'],images['caterpillarColors']]

	#load CharSelect images
	images['tiles'] = []
	for i in range(len(strings['char_sources'])):
		images['tiles'].append(spyral.util.load_image('games/snake/Images/Other/CharSelect/'+strings['char_sources'][i]+'.png'))
	images['colorSelectTile'] = spyral.util.load_image('games/snake/Images/Other/CharSelect/ColorSelect.png')
	images['arrows'] = spyral.util.load_image('games/snake/Images/Other/CharSelect/Arrows.png')

	#load level images
	images['level'] = []
	images['blank'] = spyral.util.load_image('games/snake/Images/Other/blank.png')
	images['level'].append(images['blank'].copy())
	for i in range(3):
		images['level'].append( spyral.util.load_image('games/snake/Images/Other/Level' + str(i+1) +'.png'))
        images['Final'] = spyral.util.load_image('games/snake/Images/Other/FinalScore.png')

	#load scoreBox images
	images['score'] = []
	#images['score'].append(images['clear'])
	for i in range(3):
		images['score'].append( spyral.util.load_image('games/snake/Images/Other/ScoreBox' + str(i) +'.png'))
	
	
	images['tablet_instructions'] = fonts
	
	fonts['node'] = pygame.font.SysFont(None,3*BLOCK_SIZE/5)
	fonts['number'] = pygame.font.SysFont(None,BLOCK_SIZE)
	fonts['operator'] = pygame.font.SysFont(None,BLOCK_SIZE)
	fonts['length'] = pygame.font.SysFont(None,BLOCK_SIZE/2)
	fonts['expression'] = pygame.font.Font('games/snake/MangaTemple.ttf',BLOCK_SIZE/2)
	fonts['goal'] = fonts['expression']
	fonts['score'] = pygame.font.Font('games/snake/MangaTemple.ttf', BLOCK_SIZE)
	fonts['pop_up'] = fonts['expression']
	
	fonts['menu_start'] = pygame.font.SysFont(None,2*images['button_start'][0].get_height() / 3)
	fonts['menu_character'] = pygame.font.SysFont(None,images['button_start'][0].get_height() / 2)
	fonts['menu_unlock'] = pygame.font.SysFont(None,images['button_start'][0].get_height() / 3)
	fonts['menu_quit'] = pygame.font.SysFont(None,2*images['button_start'][0].get_height() / 3)
	fonts['character_unlock'] = pygame.font.SysFont(None,images['button_start'][0].get_height() / 4)
	fonts['character_back'] = pygame.font.SysFont(None,2*images['button_start'][0].get_height() / 3)
	fonts['character_name'] = pygame.font.Font('games/snake/MangaTemple.ttf',images['button_start'][0].get_height() / 3)
	fonts['character_color'] = pygame.font.Font('games/snake/MangaTemple.ttf',images['button_start'][0].get_height() / 3)

	geom['lengthx'] = WIDTH - BLOCK_SIZE*2
	geom['expressionx'] = 0
	geom['goalx'] = (WIDTH - BLOCK_SIZE*2)
	geom['text_height'] = 0
	geom['text_height_bottom'] = HEIGHT - BLOCK_SIZE
	geom['level_score_y'] = HEIGHT - 500 - BLOCK_SIZE/2
	geom['total_score_y'] = HEIGHT - 300 - BLOCK_SIZE/2
	geom['score_x'] = 3*WIDTH/4
	
	geom['menu_start'] = pygame.Rect(300, 240, 200, 48)
	geom['menu_character'] = pygame.Rect(300, 325, 200, 70)
	geom['menu_unlock'] = pygame.Rect(24, 518, 210, 54)
	geom['menu_quit'] = pygame.Rect(684, 542, 85, 28)
		 
	geom['menu_title_y'] = HEIGHT / 6
	geom['menu_start_y'] = HEIGHT / 2 - images['button_start'][0].get_height()/8
	geom['menu_character_y'] = geom['menu_start_y'] + images['button_start'][0].get_height()
	geom['menu_quit_y'] = geom['menu_character_y'] + images['button_charselect'][0].get_height()
	
	geom['character_title_y'] = HEIGHT / 6
	#geom['character_unlock_x'] = WIDTH * 2/100
	#geom['character_unlock_y'] = 13*HEIGHT/14 - images['button_normal'].get_height()/2
	geom['character_back_x'] = 40
	geom['character_back_y'] = geom['menu_quit_y']
	geom['character_image_y'] = HEIGHT/2 
	geom['character_name_y'] = HEIGHT/2 + images['characters'][0][0].get_height()
	geom['character_color_y'] = geom['character_name_y'] + images['tiles'][0].get_height()
	#geom['character_color_select_y'] = geom['character_color_y'] + images['color_select'].get_height()
	
	geom['total_colors'] = 3
	
	images['tablet_instructions'] = fonts['goal'].render(_("Press Any Key To Continue"), True, (0,0,0))

	#images['head'] = pygame.image.load("games/snake/Images/Adder/Adder_Head_E0.png")
	#images['head'].fill(colors['head'])
"""