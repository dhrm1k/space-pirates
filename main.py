import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Invader")

icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)


playerImage = pygame.image.load("player.png")
playerX = 376 
playerY = 510

playerY_change = 0
playerX_change = 0

enemyImage = pygame.image.load("enemy.png")
enemyX = 20
enemyY = 20
enemyX_change = 0.2
enemyY_change = 40


def player(x, y):
	screen.blit(playerImage, (x, y))

def enemy(x, y):
	screen.blit(enemyImage, (x, y))

running = True

while running:
	screen.fill((0, 0, 0))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				playerX_change = -0.3
			if event.key == pygame.K_RIGHT:
				playerX_change = 0.3
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
				playerX_change = 0


	playerX += playerX_change

	if playerX <= 0:
		playerX = 0
	elif playerX >= 736:
		playerX = 736

	if enemyX <= 0:
		enemyX_change = 0.2
		enemyY += enemyY_change

	elif enemyX >= 736:
		enemyX_change = -0.2
		enemyY += enemyY_change
		

	enemyX += enemyX_change



	enemy(enemyX, enemyY)
	player(playerX, playerY)

	pygame.display.update()