import sys,pygame
#引入pygame中所有常量，比如 QUIT
from pygame.locals import *
pygame.init()

screenWidth = 1200
screenHeight = 900

FPS = 60
clock = pygame.time.Clock()
running = True

screen = pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption('c语言中文网')
#加载一张图片
image_surface = pygame.image.load("./pic/test2.png").convert()

imageSize = image_surface.get_size()

imageSizeWidth = imageSize[0]

imageSizeHeight = imageSize[1]
# rect(left,top,width,height)指定图片上某个区域
# special_flags功能标志位,指定颜色混合模式，默认为 0 表示用纯色填充
image_surface.fill((0,0,255),rect=(0,0,imageSizeWidth,imageSizeHeight),special_flags=2)
# 200,100 表示图像在水平、垂直方向上的偏移量，以左上角为坐标原点
image_surface.scroll(0,0)
# 无限循环，让窗口停留
while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            pygame.quit()
            sys.exit()

    print(clock.get_fps())
    # 将图像放置在主屏幕上
    screen.blit(image_surface,((screenWidth - imageSizeWidth)/2,(screenHeight - imageSizeHeight)/2))
    pygame.display.update()
