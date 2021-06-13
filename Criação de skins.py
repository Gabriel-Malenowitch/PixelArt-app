import pygame

def g_out():
	global janela_ativa, save
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			janela_ativa = False; save = 1
            


class do():

    def __init__(self, n, g):
        self.n = n; self.a = 10; self.g = g

    def mouse_position_if_k1(self, n, num):
        self.n, self.num = n, num
        self.pressed1, self.pressed2, self.pressed3 = pygame.mouse.get_pressed()
        self.h = pygame.mouse.get_pos()
        if self.h[0] > 0 and self.h[0] < 500 and self.h[1] > 0 and self.h[1] < 500:
            if self.num == 0:
                if self.h[0] > 0 and self.h[1] > 0 and self.h[1] < 24:
                    if self.pressed1:
                        return self.h
                    else:
                        return self.n
                else:
                    return self.n
            elif self.num == 1:
                if self.h[0] > 0 and self.h[1] > 0 and self.h[1] > 24:
                    if self.pressed1:
                        self.h = pygame.mouse.get_pos()
                        return self.h
                    else:
                        return self.n
                else:
                    return self.n
            else:
                return self.n
        else:
            return self.g

    def extract_color(self):
        self.g = self.mouse_position_if_k1(self.g, 0)
        self.n = janela_skin.get_at(self.g)
        return self.n

    def draw(self, n):
        self.posicao_0, self.posicao_1 = self.mouse_position_if_k1(self.g, 1)
        self.posicao_0, self.posicao_1 = (int(self.posicao_0/10))*self.a, (int(self.posicao_1/10))*self.a
        pygame.draw.rect(janela_skin, n, pygame.Rect(self.posicao_0,self.posicao_1,10,10))



#======================================================================
janela_skin = pygame.display.set_mode((500,500))
pygame.display.set_caption("Criação de skin")
relogio = pygame.time.Clock()
relogio.tick(60)

janela_ativa = True; save = 0; n = (33,33,33); g = (0,0); work = do(n, g)
icones = pygame.image.load("Imagens Criação de skins\\Icones.png")
#======================================================================



while janela_ativa:
    g_out()
    pygame.display.update()
    
    #janela_skin.fill((0,0,0))        

    n = work.extract_color()
    work.draw(n)
    
    if save != 1:
        janela_skin.blit(icones,(0,0))
        pygame.draw.rect(janela_skin, n, pygame.Rect(480,480,10,10))
        pygame.image.save(janela_skin,"Imagem.png")

pygame.quit()
