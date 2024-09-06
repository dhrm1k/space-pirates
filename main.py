import pygame
import random
import math

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Space Pirates")

icon = pygame.image.load("ufo.png")
pygame.display.set_icon(icon)


playerImage = pygame.image.load("player.png")
playerX = 376 
playerY = 510

playerY_change = 0
playerX_change = 0

enemyImage = pygame.image.load("enemy.png")
enemyX = random.randint(0, 736)
enemyY = random.randint(50, 150)
enemyX_change = 0.2
enemyY_change = 40


bulletImage = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 520
bulletX_change = 0.2
bulletY_change = -0.2
bullet_state = 'ready'

def player(x, y):
	screen.blit(playerImage, (x, y))

def enemy(x, y):
	screen.blit(enemyImage, (x, y))

def bullet(x, y):
	global bullet_state
	bullet_state = 'fire'
	screen.blit(bulletImage, (x + 16, y))

def isCollision(x1, y1, x2, y2):
	distance = math.sqrt(math.pow((x2 - x1), 2) + math.pow((y2 - y1), 2))
	
	if distance < 30:
		return True
	else:
		return False

running = True

score = 0

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
			if event.key == pygame.K_SPACE and bullet_state == 'ready':
				bulletX = playerX
				bullet(bulletX, bulletY)
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

	if bulletY <= 0:
		bullet_state = 'ready'
		bulletY = 520

	if bullet_state == 'fire':
		bullet(bulletX, bulletY)
		bulletY += bulletY_change

	collision = isCollision(enemyX, enemyY, bulletX, bulletY)

	if collision == True:
		bulletY = 480
		bullet_state = "ready"
		score += 1
		enemyX = random.randint(0, 736)
		enemyY = random.randint(50, 150)
		print(score)

	player(playerX, playerY)

	pygame.display.update()