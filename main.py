import pygame

class App:
    def if_press_to_close(self):
        global screen_status
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                screen_status = False
            else:
                screen_status = True

class Tools:
    def get_mouse_position_and_key_pressed(self):
        self.pressed_0, self.pressed_1, self.pressed_2 = pygame.mouse.get_pressed()
        if self.pressed_0:        
            return pygame.mouse.get_pos(), "pressed 0"
        elif self.pressed_1:
            return pygame.mouse.get_pos(), "pressed 1"
        elif self.pressed_2:
            return pygame.mouse.get_pos(), "pressed 2"

    def render_position(self):
        font = pygame.font.Font('fonts\\roboto\\Roboto-Regular.ttf', 12)
        text = font.render(str(pygame.mouse.get_pos()), True, (255,255,255), (212, 184, 106))
        textRect = text.get_rect()
        textRect.center = (1265, 51)
        screen.blit(text, textRect)

    def render_text(self, text, text_color, background_color, position_option, position, size ):
        font = pygame.font.Font('fonts\\roboto\\Roboto-Regular.ttf', int(size))
        text = font.render(str(text), True, text_color, background_color)
        textRect = text.get_rect()
        if position_option == 0:
            textRect.center = position
            screen.blit(text, textRect)
        elif position_option == 1:
            screen.blit(text, position)
        else:
            print("position_option error (wrong paramter)")
    
    def resize_image(self, image, size):
        """
            size is a list;
            size[0] = width;
            size[1] = height;
            if do you wanna the automatic calcule to keep with 
            the same scale, just replace one of that by "auto".
        """
        # rect = image.get_rect()
        width = image.get_width()
        height = image.get_height()
        if size[1] == "auto":
            size = (size[0],(size[0]*height)//width)
            # print(size[0],(size[0]*height)/width,"Zz", size[0],(size[0]*height)//width)
        elif size[0] == "auto":
            size = ((size[1]*width)//height, size[1])     
        return pygame.transform.scale(image, size)
            
    def draw_image(self, path, size, position, border_width=0, border_color=(0,0,0), padding=0):
        self.pencil_image = pygame.image.load(path)
        image = self.resize_image(self.pencil_image, size)
        if border_width > 0:
            screen.blit(image, [position[0]+padding, position[1]+padding])
            width = image.get_width()
            height = image.get_height()
            pygame.draw.rect(screen, border_color, (position[0],position[1],width+padding*2,height+padding*2), border_width)  #draw border
            # pygame.draw.rect(screen, border_color, (position[0],position[1],width+padding*2,25), border_width)  #draw border (25 is the default heigth [Gambiarra])
        else:
            screen.blit(image, position)
    

class Renderizer_Header():
    def __init__(self):
        self.draw_context()
        self.draw_functions()
        self.draw_colors_options()

        #---LOGO---#
        
    def render_logo(self):
        tools.render_text("PixelArt-app", (255,255,255), (212, 184, 106), 0, (1300/2, 102/2), 40)

    def draw_context(self):
        pygame.draw.line(screen, (212, 184, 106), (0,50), (1300,50), 102)  #fill the rect main
        pygame.draw.rect(screen, (170, 137, 57), (0,0,1300,101), width=2)  #the rect main
        pygame.draw.rect(screen, (170, 137, 57), (70,10,200,80), width=2)  #the rect of functions
        pygame.draw.rect(screen, (170, 137, 57), (300,10,66,80), width=2)  #the rect of functions's options of size
        self.render_logo()
        pygame.draw.rect(screen, (170, 137, 57), (900,10,100,80), width=2) #the rect of colors
        pygame.draw.rect(screen, (170, 137, 57), (1030,10,200,80), width=2) #the rect of colors's options

    def draw_functions(self):    
        # pygame.draw.rect(screen, (170, 137, 57), (0,0,1300,101), width=2)  #the rect main
        #Functions:
        tools.draw_image("Images/pencil_option.png", (20,20), (82,22), border_width=2, padding=3)    #draw pencil
        tools.draw_image("Images/color-fill-tool.png", (20,20), (120,22), border_width=2, padding=2) #draw color-fill
        tools.draw_image("Images/dropper.png", (20,20), (82,57), border_width=2, padding=2)          #draw dropper
        tools.draw_image("Images/paint-spray.png", (20,20), (120,57), border_width=2, padding=1)     #draw spray
        tools.draw_image("Images/image-line.png", (60,60), (174,22), border_width=0, padding=1)      #draw image
    
    def draw_size_pencil(self):
        #Size pencil:
        if function_selected == "pencil":
            pygame.draw.line(screen, (0,0,0), (310,18),(356,18), 10) #little
            pygame.draw.line(screen, (0,0,0), (310,38),(356,38), 20) #medium
            pygame.draw.line(screen, (0,0,0), (310,70),(356,70), 30) #large
            tools.render_text("}", (230,230,230), (212, 184, 106), 1, (370,6), 70) #beatifully signal

    def draw_colors(self):
        pygame.draw.rect(screen, color_list[0], pygame.Rect(905,20,25,25))  #Color white
        pygame.draw.rect(screen, color_list[1], pygame.Rect(937,20,25,25))  #Color black
        pygame.draw.rect(screen, color_list[2], pygame.Rect(970,20,25,25))  #Color blue
        pygame.draw.rect(screen, color_list[3], pygame.Rect(905,55,25,25))  #Color red
        pygame.draw.rect(screen, color_list[4], pygame.Rect(937,55,25,25))  #Color i don't know
        pygame.draw.rect(screen, color_list[5], pygame.Rect(970,55,25,25))  #Color green
    
    def draw_colors_options(self):
        tools.draw_image("Images/colors_board.png", (197,77), (1032,12))

class Config_Header():
    # def __init__():
         
        
    def draw_selected_function(self):
        pygame.draw.rect(screen, white, function_list_position[function_selected], 3) #draw border

def do_header():
    #In __init__ the header gonna draw the style
    renderizer_header.draw_size_pencil()  #if the tool is a pencil, the sizes will be show
    renderizer_header.draw_colors()       #draw colors in colors selctions
    config_header.draw_selected_function()


    tools.render_position()    #render mouse posiiton 

#======================================================================

white = (255,255,255)
black = (0,0,0)
blue  = (0,0,255)
red   = (255,0,0)
idont = (0,130,255)
green = (0,255,0)

color_list = [
    white, # -- 0
    black, # -- 1
    blue,  # -- 2
    red,   # -- 3
    idont, # -- 4
    green  # -- 5
]

function_list_position = {
    "pencil":(82,22,27,27), 
    "bucket":(120,22,25,25),
    "dropper":(82,57,25,25),
    "spray":(120,57,23,23),
    "image":(174,22,61,61)
}

function_selected = "pencil"
color_selected = white

#======================================================================
pygame.init()

screen_status = True
screen = pygame.display.set_mode((1300,800))
pygame.display.set_caption("Skin creator")
clock = pygame.time.Clock()
clock.tick(60)

app = App(); tools = Tools();
renderizer_header = Renderizer_Header()
config_header = Config_Header()
#======================================================================

def run():
    app.if_press_to_close() 
    pygame.display.update()
    do_header()


while screen_status:
    run()
pygame.quit()

