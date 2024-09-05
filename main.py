import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invader")

icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)


#playerimg
playerImage = pygame.image.load("player.png")
playerX = 10 
playerY = 260

playerY_change = 0



def player(x, y):
	screen.blit(playerImage, (x, y))




running = True

while running:
	screen.fill((0, 0, 0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
				playerY_change = -0.3
			if event.key == pygame.K_DOWN:
				playerY_change = 0.3
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
				playerY_change = 0


	playerY += playerY_change

	if playerY <= 0:
		playerY = 0
	elif playerY >= 536:
		playerY = 536


	



	player(playerX, playerY)

	pygame.display.update()