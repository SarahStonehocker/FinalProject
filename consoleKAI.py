import pygame
import sys
import globalVariables

pygame.init()

clock = pygame.time.Clock()
screen = pygame.display.set_mode([600, 500])
base_font = pygame.font.Font(None, 32)
user_text = ''
input_rect = pygame.Rect(170, 430, 140, 32)
input_rect_BG = pygame.Rect(160, 420, 450, 300)
color_active = pygame.Color('lightskyblue3')
color_passive = pygame.Color('chartreuse4')
color = color_passive
active = False

def init():
    pass

def draw():
    global user_text, active, color

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if input_rect.collidepoint(event.pos):
                active = True
            else:
                active = False

        if event.type == pygame.KEYDOWN:
            if active:
                if event.key == pygame.K_RETURN:
                    active = False
                    user_text = user_text.strip()
                    if (globalVariables.decision == 1):
                        if (user_text == "Fly straight away from Earth"):
                            globalVariables.decision += 1
                    elif (globalVariables.decision == 2):
                        if (user_text == "yes"):
                            globalVariables.decision += 1
                    globalVariables.user_input = user_text
                    user_text = ''
                elif event.key == pygame.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    user_text += event.unicode

    #screen.fill((255, 255, 255))
    pygame.draw.rect(screen, (0,255,0), input_rect_BG)

    if active:
        color = color_active
    else:
        color = color_passive

    pygame.draw.rect(screen, color, input_rect)

    text_surface = base_font.render(user_text, True, (255, 255, 255))
    screen.blit(text_surface, (input_rect.x+5, input_rect.y+5))

    input_rect.w = max(100, text_surface.get_width()+10)

    pygame.display.flip()

    clock.tick(60)

def output(text, x, y, color):
    text_surface = base_font.render(text, True, color)
    screen.blit(text_surface, (input_rect.x + x, input_rect.y + 40 + y))
    pygame.display.flip()

def key_pressed(key):
    global user_text, active
    if active:
        if key == pygame.K_RETURN:
            active = False
            user_text = user_text.strip()
            output(user_text)
            user_text = ''
        elif key == pygame.K_BACKSPACE:
            user_text = user_text[:-1]
        else:
            user_text += pygame.key.name(key)

