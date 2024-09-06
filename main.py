import pygame
import random
import math
from pygame import mixer

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


enemyImage = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
no_of_enemies = 6

for i in range(no_of_enemies):
	enemyImage.append(pygame.image.load("enemy.png"))
	enemyX.append(random.randint(0, 736))
	enemyY.append(random.randint(50, 150))
	enemyX_change.append(0.2)
	enemyY_change.append(40)


bulletImage = pygame.image.load("bullet.png")
bulletX = 0
bulletY = 520
bulletX_change = 0.5
bulletY_change = -0.5
bullet_state = 'ready'

def player(x, y):
	screen.blit(playerImage, (x, y))

def enemy(x, y, i):
	screen.blit(enemyImage[i], (x, y))

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

score_value = 0

font = pygame.font.Font('freesansbold.ttf', 32)
testX = 10
testY = 10


game_over = pygame.font.Font('freesansbold.ttf', 64)

def game_over_text():
	over_text = game_over.render("GAME OVER", True, (255, 255, 255))
	screen.blit(over_text, (200, 250))

def showScore(x, y):
	score = font.render("Score: " + str(score_value), True, (255, 255, 255))
	screen.blit(score, (x, y))

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
				bullet_Sound = mixer.Sound('laser.wav')
				bullet_Sound.play()
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

	for i in range(no_of_enemies):

		if enemyY[i] > 440:
			for j in range(no_of_enemies):
				enemyY[j] = 2000
			game_over_text()
			break



		if enemyX[i] <= 0:
			enemyX_change[i] = 0.2
			enemyY[i] += enemyY_change[i]

		elif enemyX[i] >= 736:
			enemyX_change[i] = -0.2
			enemyY[i] += enemyY_change[i]


		enemyX[i] += enemyX_change[i]
		
		collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)

		if collision == True:
				bulletY = 480
				bullet_state = "ready"
				score_value += 1
				enemyX[i] = random.randint(0, 736)
				enemyY[i] = random.randint(50, 150)


		enemy(enemyX[i], enemyY[i], i)

	if bulletY <= 0:
		bullet_state = 'ready'
		bulletY = 520

	if bullet_state == 'fire':
		bullet(bulletX, bulletY)
		bulletY += bulletY_change

	player(playerX, playerY)
	showScore(testX, testY)

	pygame.display.update()