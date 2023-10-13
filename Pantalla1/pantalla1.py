import pygame
import sys

# Inicializa pygame
pygame.init()

# Configura la resolución de la pantalla HDMI
screen = pygame.display.set_mode((1920, 1080))  # Ajusta la resolución según tus necesidades

# Define tu lógica y gráficos aquí
# Por ejemplo, para mostrar un rectángulo rojo en la pantalla:
red = (255, 0, 0)
rect = pygame.Rect(100, 100, 200, 200)
pygame.draw.rect(screen, red, rect)

# Refresca la pantalla
pygame.display.flip()

# Ejecuta un bucle para mantener la ventana abierta
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Finaliza pygame
pygame.quit()
sys.exit()