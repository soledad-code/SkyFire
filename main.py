import pygame

print('Setup Started')
pygame.init() # inicializando
window = pygame.display.set_mode(size=(600, 480)) # criando uma janela para o jogo
print('Setup Ended')

print('Loop Started')
while True:
    # Check for all events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print('Quitting...')
            pygame.quit() # Close Window
            quit() #end pygame
