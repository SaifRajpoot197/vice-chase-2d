import pygame

pygame.init()
screen = pygame.display.set_mode((1000,720))
pygame.display.set_caption("Vice Heart")
clock = pygame.time.Clock()
lucia_x = 400
lucia_y = 300
car_x = 250
car_y = 200
police_x = 100
police_y = 80
in_car = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_f:
                if abs(lucia_x - car_x) < 50 and abs(lucia_y - car_y) < 50:
                    in_car = not in_car
    keys = pygame.key.get_pressed()
    speed = 10 if in_car else 5

    if keys[pygame.K_w]:
        lucia_y -= speed
        if in_car: car_y -= speed

    if keys[pygame.K_s]:
        lucia_y += speed
        if in_car: car_y += speed

    if keys[pygame.K_a]:
        lucia_x -= speed
        if in_car: car_x -= speed

    if keys[pygame.K_d]:
        lucia_x += speed
        if in_car: car_x += speed

    if lucia_x > police_x:
        police_x += 3
    else:
        police_x -= 3
    if lucia_y > police_y:
        police_y += 3
    else:
        police_y -= 3

    screen.fill((0,255,0))
    if not in_car:
        pygame.draw.rect(screen,(255,0,0),(lucia_x,lucia_y,100,100))
    pygame.draw.rect(screen,(0,0,255),(car_x,car_y,80,80))
    pygame.draw.rect(screen,(0,0,0),(police_x,police_y,80,80))
    pygame.display.update()
    clock.tick(60)
pygame.quit()