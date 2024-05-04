import random
import globalVariables
import SolandGraphics
import sys
import pygame
import consoleKAIKAI

# Define game states
RUNNING = 0
WAITING_FOR_DECISION = 1

globalVariables.decision = 1
runGame = True

def main():
    # Set up Pygame
    SolandGraphics.setup()

    # Set up text input
    consoleKAI.init()

    # Start Game
    game_state = RUNNING
    while runGame:

        # Update background
        if globalVariables.decision == 1:
            SolandGraphics.earthLocation(0, 0, (0.5, 0.5), 0.1, 0)
        elif globalVariables.decision == 2:
            SolandGraphics.spaceLocation(0, 0, (0.5, 0.5), 0.1, 0)

        SolandGraphics.spaceShip(0, 0, (0.5, 0.5), 0.1, 0)

        # Draw text input
        consoleKAI.draw()

        # Handle Pygame events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if game_state == WAITING_FOR_DECISION:
                    if event.key == pygame.K_RETURN:
                        consoleKAI.enter_pressed()
                        game_state = RUNNING
                        globalVariables.decision += 1  # Increment decision
                        consoleKAI.user_input()
                        
                    else:
                        consoleKAI.key_pressed(event.key)

        # Update display
        pygame.display.update()

        # Handle game decisions
        handle_game_decisions(globalVariables.decision)

        # Check if the game is over
        if globalVariables.supplies <= 0 or globalVariables.crew <= 0:
            consoleKAI.output("Game over!")
            break

def handle_game_decisions(decision):
    friendlies = 0
    if decision == 1:
        consoleKAI.output("How shall we proceed?", 0, 0, (0,0,0))
        consoleKAI.output("Fly straight away from Earth?", 0,25, (0,0,255))
        consoleKAI.output("Slingshot around the moon? ", 0, 50, (0,0,255))
        if decision == 1 and globalVariables.user_input == "fly":
            globalVariables.decision += 1
            globalVariables.supplies -= 2
        elif decision == 1 and globalVariables.user_input == "slingshot":
            globalVariables.decision += 1
            globalVariables.supplies -= 1
        #globalVariables.user_input = ""
            
    elif decision == 2:
        consoleKAI.output("Jump to hyperspace now? (y/n) ", 0, 0, (0,0,0))
        if random.random() < 0.4:
            globalVariables.broken_solar = True
        else:
            globalVariables.broken_solar = False
        if decision == 2 and globalVariables.user_input == "y":
            globalVariables.decision += 1
            globalVariables.supplies -= 1
        
    elif decision == 3:
        if globalVariables.broken_solar:
            consoleKAI.output("Solar panel is broken! Send a crew member or robot to fix it? ", 0, 0, (0,0,0))
            consoleKAI.output("Send a crew member", 0, 25, (0,0,255))
            consoleKAI.output("Send robot to fix it? ", 0, 50, (0,0,255))
            if decision == 3 and globalVariables.user_input == "crew":
                if random.random() < 0.5:
                    globalVariables.crew -= 1
                    consoleKAI.output("Crew member lost!", 0, 100, (0,0,0))
                else:
                    globalVariables.broken_solar = False
                    consoleKAI.output("Solar panel is fixed! ", 0, 100, (0,0,0))
            elif decision == 3 and globalVariables.user_input == "robot":
                consoleKAI.output("The robot is destroyed by gamma rays.", 0, 75, (0,0,0))
                pygame.time.wait(2000)
        else:
            globalVariables.decision += 1
    elif decision == 4:
        if not globalVariables.broken_solar:
            consoleKAI.output("Distress signals must be investigated! ", 0, 0, (0,0,0))
            consoleKAI.output("How many crew members should ", 0, 25, (0,0,0))
            consoleKAI.output("investigate? ", 0, 50, (0,0,0))
            if random.random() < 0.3:
                friendlies = 0
            elif 0.3 < random.random() < 0.6:
                friendlies = 2
            elif 0.6 < random.random():
                friendlies = 1
            if decision == 4 and globalVariables.user_input == "1":
                if friendlies == 0:
                    consoleKAI.output("Your crew member never returns.", 0, 75, (0,0,0))
                    globalVariables.crew -= 1
                    pygame.time.wait(2000)
                    globalVariables.decision += 1
                elif friendlies == 1:
                        consoleKAI.output("Your crew member returns well fed.", 0, 75, (0,0,0))
                        globalVariables.decision += 1
                elif friendlies == 2:
                    consoleKAI.output("The crew returns empty handed.", 0, 75, (0,0,0))
                    globalVariables.supplies -= 1
                    pygame.time.wait(2000)
                    globalVariables.decision += 1
            elif decision == 4 and globalVariables.user_input == "2":
                if friendlies == 0:
                    consoleKAI.output("Your crew was able to escape the planet.", 0,75 ,(0,0,0))
                    pygame.time.wait(2000)
                    globalVariables.decision += 1
                elif friendlies == 1:
                    consoleKAI.output("Your crew members return well fed.", 0, 75, (0,0,0))
                    globalVariables.decision += 1
                elif friendlies == 2:
                    consoleKAI.output("The crew returns empty handed.", 0, 0, (0,0,0))
                    globalVariables.supplies -= 1
                    pygame.time.wait(2000)
                    globalVariables.decision += 1
                    
            elif decision == 4 and globalVariables.user_input == "3":
                if friendlies == 0:
                    consoleKAI.output("Your crew was able to escape the planet.", 0,0 ,(0,0,0))
                    pygame.time.wait(2000)
                    globalVariables.decision += 1
                elif friendlies == 1:
                    consoleKAI.output("Your crew members return well fed.", 0, 75, (0,0,0))
                    pygame.time.wait(2000)
                    globalVariables.decision += 1
                elif friendlies == 2:
                    consoleKAI.output("You sent all crew members.", 0, 0, (0,0,0))
                    consoleKAI.output("There's no way back to the ship!.", 0, 25, (0,0,0))
                    globalVariables.decision += 1
                    globalVariables.crew = 0
        else:
            globalVariables.decision += 1
    elif decision == 5:
        if globalVariables.broken_solar:
            consoleKAI.output("You successfully made the jump, but something seems off about the software of your ship." , 0, 0, (0,0,0))
        else:
            globalVariables.decision += 1
    elif decision == 6:
        
        consoleKAI.output("You arrive at another star system. There seems to be some sort of escape pod orbiting a nearby moon. Inspect it or leave it alone? ", 0, 0, (0,0,0))
        consoleKAI.output("Inspect the escape pod", 0, 25, (0,0,255))
        consoleKAI.output("Leave it alone", 0, 50, (0,0,255))
        if decision == 6 and globalVariables.user_input == "inspect":
            if random.random() < 0.5:
                consoleKAI.output("The escape pod is empty.", 0, 75, (0,0,0))
                globalVariables.supplies -= 1
            else:
                consoleKAI.output("You found some supplies in the escape pod.", 0, 75, (0,0,0))
                globalVariables.supplies += 2
        globalVariables.decision += 1
        

    elif decision == 7:
        if globalVariables.broken_solar:
            consoleKAI.output("Arriving at the next star system, something is very wrong. Lights are flashing in the cabin and you hear an automated voice saying LOW POWER LOW POWER. Send a crew member to fix it or switch to power cell power? ", 0, 0, (0,0,0))
            consoleKAI.output("Send a crew member to fix it", 0, 25, (0,0,255))
            consoleKAI.output("Switch to power cell power", 0, 50, (0,0,255))
            if decision == 7 and globalVariables.user_input == "crew":
                if random.random() < 0.5:
                    consoleKAI.output("The crew member fixes the issue.", 0, 75, (0,0,0))
                    globalVariables.broken_solar = False
                else:
                    consoleKAI.output("The crew member fails to fix the issue.", 0, 75, (0,0,0))
                    globalVariables.crew -= 1
            elif decision == 7 and globalVariables.user_input == "power cell":
                consoleKAI.output("You switch to power cell power.", 0, 75, (0,0,0))
                globalVariables.supplies -= 1
            globalVariables.decision += 1
        else:
            globalVariables.decision += 1

    elif decision == 8:
        consoleKAI.output("You arrive at the next system, hoping that you’re getting close to the probe. However, you are immediately aware of the giant black hole at the center of this system. Should we investigate the black hole or make the jump away? ", 0, 0, (0,0,0))
        consoleKAI.output("Investigate the black hole", 0, 25, (0,0,255))
        consoleKAI.output("Make the jump away", 0, 50, (0,0,255))
        if decision == 8 and globalVariables.user_input == "investigate":
            if random.random() < 0.3:
                consoleKAI.output("Your ship gets too close to the black hole and is destroyed.", 0, 75, (0,0,0))
                globalVariables.crew = 0
                globalVariables.supplies = 0
            else:
                consoleKAI.output("You successfully gather valuable data about the black hole.", 0, 75, (0,0,0))
        elif decision == 8 and globalVariables.user_input == "jump away":
            consoleKAI.output("You make the jump away from the black hole.", 0, 75, (0,0,0))
            globalVariables.decision += 1



if __name__ == "__main__":
    main()
