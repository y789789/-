import pygame
import math

# macOS 专属初始化（修复窗口渲染）
pygame.init()
pygame.mixer.quit()  # 避免音频权限问题（可选）
screen = pygame.display.set_mode((800, 600), pygame.DOUBLEBUF | pygame.HWSURFACE)
clock = pygame.time.Clock()

class Car:
    def __init__(self):
        self.image = pygame.Surface((40, 20), pygame.SRCALPHA)  # 支持透明通道
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect(center=(400, 300))
        self.angle = 0
        self.speed = 0
        self.max_speed = 8
        self.nitro = 100
        self.drifting = False

    def update(self):
        keys = pygame.key.get_pressed()

        # 方向控制（适配 Mac 键盘布局）
        if keys[pygame.K_LEFT]:
            self.angle += 5
        if keys[pygame.K_RIGHT]:
            self.angle -= 5

        # 加速/刹车
        if keys[pygame.K_UP]:
            self.speed = min(self.max_speed, self.speed + 0.2)
        elif keys[pygame.K_DOWN]:
            self.speed = max(-self.max_speed/2, self.speed - 0.2)
        else:
            self.speed *= 0.98

        # 漂移（空格键）
        if keys[pygame.K_SPACE] and self.speed != 0:
            self.drifting = True
            self.speed *= 0.95
            self.nitro = min(100, self.nitro + 1)
        else:
            self.drifting = False

        # 氮气加速（左 Shift）
        if keys[pygame.K_LSHIFT] and self.nitro > 0:
            self.speed = min(self.max_speed * 1.5, self.speed + 0.3)
            self.nitro -= 2

        radians = math.radians(self.angle)
        self.rect.x += self.speed * math.cos(radians)
        self.rect.y -= self.speed * math.sin(radians)
        self.rect.clamp_ip(screen.get_rect())

    def draw(self, surface):
        rotated_image = pygame.transform.rotate(self.image, self.angle)
        new_rect = rotated_image.get_rect(center=self.rect.center)
        surface.blit(rotated_image, new_rect.topleft)
        pygame.draw.rect(surface, (0, 0, 255), (10, 10, self.nitro, 20))

# 运行主循环
car = Car()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((128, 128, 128))
    car.update()
    car.draw(screen)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()