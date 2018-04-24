import pygame


class MyPlane(pygame.sprite.Sprite):
    def __init__(self,bg_size):
        pygame.sprite.Sprite.__init__(self)
        self.image1 = pygame.image.load(r"C:\Users\ChengTao\Desktop\plane_game_test\Image\hero1.png").convert_alpha()
        self.image2 = pygame.image.load(r"C:\Users\ChengTao\Desktop\plane_game_test\Image\hero2.png").convert_alpha()
        self.destroy_images = []
        self.destroy_images.extend([\
            pygame.image.load(r"C:\Users\ChengTao\Desktop\plane_game_test\Image\hero_down1.png").convert_alpha(),\
            pygame.image.load(r"C:\Users\ChengTao\Desktop\plane_game_test\Image\hero_down2.png").convert_alpha(),\
            pygame.image.load(r"C:\Users\ChengTao\Desktop\plane_game_test\Image\hero_down3.png").convert_alpha(),\
            pygame.image.load(r"C:\Users\ChengTao\Desktop\plane_game_test\Image\hero_down4.png").convert_alpha()\
            ])
            
        self.rect = self.image1.get_rect()
        self.width,self.height = bg_size[0],bg_size[1]
        # 初始化位于下方的中间位置
        #下方预留60像素左右的位置作为“状态栏”

        self.rect.left,self.rect.top = (self.width - self.rect.width)//2,\
                                       self.height-self.rect.height-60
        self.speed = 10
        self.active = True
        self.invincible = False
        self.mask = pygame.mask.from_surface(self.image1)


    def moveUp(self):
        if self.rect.top>0:
            self.rect.top -= self.speed

        else:
            self.rect.top = 0

    def reset(self):
        self.active = True
        self.rect.left,self.rect.top = (self.width - self.rect.width)//2,\
                                       self.height-self.rect.height-60
        self.invincible = True
    





            

    def moveDown(self):
        if self.rect.bottom < self.height-60:
            self.rect.top += self.speed
        else:
            self.rect.bottom = self.height -60

    def moveLeft(self):
        if self.rect.left >0:
            self.rect.left -= self.speed
        else:
            self.rect.left=0

    def moveRight(self):
        if self.rect.right < self.width:
            self.rect.left += self.speed
        else:
            self.rect.right = self.width



            
