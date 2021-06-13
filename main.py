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
        font = pygame.font.Font('fonts\\roboto\\Roboto-Regular.ttf', 32)
        text = font.render(str(pygame.mouse.get_pos()), True, (0,0,255), (0,255,0))
        textRect = text.get_rect()
        textRect.center = (1300 / 2, 900 / 2)
        screen.blit(text, textRect)

    def render_text(self, text, text_color, background_color, position_option, position, size ):
        font = pygame.font.Font('fonts\\roboto\\Roboto-Regular.ttf', int(size))
        text = font.render(str(text), True, text_color, background_color)
        textRect = text.get_rect()
        if position_option == 0:
            textRect.center = position
            screen.blit(text, textRect)
        elif position_option == 1:
            textRect = position
            screen.blit(text, textRect)
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
            


class Header():
    def __init__(self):
        self.draw_context()
        self.draw_functions()

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
        self.draw_image_intern_margin("Images/pencil_option.png", (20,"auto"), (82,22), border_width=2, padding=3)
        self.draw_image_intern_margin("Images/color-fill-tool.png", (20,"auto"), (120,22), border_width=2, padding=2)
        self.draw_image_intern_margin("Images/dropper.png", (20,"auto"), (82,57), border_width=2, padding=2)
        self.draw_image_intern_margin("Images/paint-spray.png", (20,"auto"), (120,57), border_width=2, padding=1)


    def draw_image_resized(self, path, size, position):
        self.pencil_image = pygame.image.load(path)
        image = tools.resize_image(self.pencil_image, size)
        screen.blit(image, position)

    def draw_image_resized_with_border(self, path, size, position, border_width=1, border_color=(0,0,0)):
        self.pencil_image = pygame.image.load(path)
        image = tools.resize_image(self.pencil_image, size)
        screen.blit(image, position)
        width = image.get_width()
        height = image.get_height()
        pygame.draw.rect(screen, border_color, (position[0],position[1],width,height), border_width)  #draw border
    
    def draw_image_intern_margin(self, path, size, position, border_width=1, border_color=(0,0,0), padding=1):
        self.pencil_image = pygame.image.load(path)
        image = tools.resize_image(self.pencil_image, size)
        screen.blit(image, [position[0]+padding, position[1]+padding])
        width = image.get_width()
        height = image.get_height()
        pygame.draw.rect(screen, border_color, (position[0],position[1],width+padding*2,height+padding*2), border_width)  #draw border
        # pygame.draw.rect(screen, border_color, (position[0],position[1],width+padding*2,25), border_width)  #draw border (25 is the default heigth [Gambiarra])
        

def render_header():
    header = Header()
    tools.render_position()
    #In __init__ the header gonna draw the style
    #draw functions rect

    

#======================================================================
pygame.init()
app = App(); tools = Tools();
screen_status = True
screen = pygame.display.set_mode((1300,800))
pygame.display.set_caption("Skin creator")
clock = pygame.time.Clock()
clock.tick(60)
# icones = pygame.image.load("Imagens Criação de skins\\Icones.png")
#======================================================================

def run():
    app.if_press_to_close() 
    pygame.display.update()
    render_header()


while screen_status:
    run()
pygame.quit()

