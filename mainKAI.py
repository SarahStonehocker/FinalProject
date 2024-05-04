import random
import globalVariables
import solandgraphics
import sys
import pygame
import console

# Define game states
RUNNING = 0
WAITING_FOR_DECISION = 1

globalVariables.decision = 1
runGame = True

def main():
    # Set up Pygame
    solandgraphics.setup()

    # Set up text input
    console.init()

    # Start Game
    game_state = RUNNING
    while runGame:

        # Update background
        if globalVariables.decision == 1:
            solandgraphics.earthLocation(0, 0, (0.5, 0.5), 0.1, 0)
        elif globalVariables.decision == 2:
            solandgraphics.spaceLocation(0, 0, (0.5, 0.5), 0.1, 0)

        solandgraphics.spaceShip(0, 0, (0.5, 0.5), 0.1, 0)

        # Draw text input
        console.draw()

        # Handle Pygame events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if game_state == WAITING_FOR_DECISION:
                    if event.key == pygame.K_RETURN:
                        console.enter_pressed()
                        game_state = RUNNING
                        #globalVariables.decision += 1  # Increment decision
                        console.user_input()
                        
                    else:
                        console.key_pressed(event.key)

        # Update display
        pygame.display.update()

        # Handle game decisions
        handle_game_decisions(globalVariables.decision)

        # Check if the game is over
        if globalVariables.supplies <= 0 or globalVariables.crew <= 0:
            console.output("Game over!", 0, 0, (0,0,0))
            pygame.time.wait(4000)
            break
        if globalVariables.victory == True:
            break

def handle_game_decisions(decision):
    friendlies = 0
    if decision == 1:
        console.output("How shall we proceed?", 0, 0, (0,0,0))
        console.output("Fly straight away from Earth?", 0,25, (0,0,255))
        console.output("Slingshot around the moon? ", 0, 50, (0,0,255))
        if decision == 1 and globalVariables.user_input == "fly":
            globalVariables.decision += 1
            globalVariables.supplies -= 2
        elif decision == 1 and globalVariables.user_input == "slingshot":
            globalVariables.decision += 1
            globalVariables.supplies -= 1
        #globalVariables.user_input = ""
            
    elif decision == 2:
        console.output("Jump to hyperspace now? (y/n) ", 0, 0, (0,0,0))
        if random.random() < 0.4:
            globalVariables.broken_solar = True
        else:
            globalVariables.broken_solar = False
        if decision == 2 and globalVariables.user_input == "y":
            globalVariables.decision += 1
            globalVariables.supplies -= 1
        
    elif decision == 3:
        if globalVariables.broken_solar:
            console.output("Solar panel is broken!", 0, 0, (0,0,0))
            console.output("Send a crew member", 0, 25, (0,0,255))
            console.output("Send robot to fix it? ", 0, 50, (0,0,255))
            if decision == 3 and globalVariables.user_input == "crew":
                if random.random() < 0.6:
                    globalVariables.crew -= 1
                    console.output("Crew member lost!", 0, 100, (0,0,0))
                else:
                    globalVariables.broken_solar = False
                    console.output("Solar panel is fixed! ", 0, 100, (0,0,0))
                    pygame.time.wait(2000)
            elif decision == 3 and globalVariables.user_input == "robot":
                console.output("The robot is destroyed by gamma rays.", 0, 75, (0,0,0))
                pygame.time.wait(2000)
        else:
            globalVariables.decision += 1
    elif decision == 4:
        if not globalVariables.broken_solar:
            console.output("Distress signals must be investigated! ", 0, 0, (0,0,0))
            console.output("How many crew members should ", 0, 25, (0,0,0))
            console.output("investigate? ", 0, 50, (0,0,0))
            if random.random() < 0.3:
                friendlies = 0
            elif 0.3 < random.random() < 0.6:
                friendlies = 2
            elif 0.6 < random.random():
                friendlies = 1
            if decision == 4 and globalVariables.user_input == "1":
                if friendlies == 0:
                    console.output("Your crew member never returns.", 0, 75, (0,0,0))
                    globalVariables.crew -= 1
                    pygame.time.wait(2000)
                    globalVariables.decision += 1
                elif friendlies == 1:
                        console.output("Your crew member returns well fed.", 0, 75, (0,0,0))
                        pygame.time.wait(2000)
                        globalVariables.decision += 1
                elif friendlies == 2:
                    console.output("The crew returns empty handed.", 0, 75, (0,0,0))
                    globalVariables.supplies -= 1
                    pygame.time.wait(2000)
                    globalVariables.decision += 1
            elif decision == 4 and globalVariables.user_input == "2":
                if friendlies == 0:
                    console.output("Your crew was able to escape the planet.", 0,75 ,(0,0,0))
                    pygame.time.wait(2000)
                    globalVariables.decision += 1
                elif friendlies == 1:
                    console.output("Your crew members return well fed.", 0, 75, (0,0,0))
                    globalVariables.decision += 1
                elif friendlies == 2:
                    console.output("The crew returns empty handed.", 0, 75, (0,0,0))
                    globalVariables.supplies -= 1
                    pygame.time.wait(2000)
                    globalVariables.decision += 1
                    
            elif decision == 4 and globalVariables.user_input == "3":
                if friendlies == 0:
                    console.output("Your crew was able to escape the planet.", 0,75 ,(0,0,0))
                    pygame.time.wait(2000)
                    globalVariables.decision += 1
                elif friendlies == 1:
                    console.output("Your crew members return well fed.", 0, 75, (0,0,0))
                    pygame.time.wait(2000)
                    globalVariables.decision += 1
                elif friendlies == 2:
                    console.output("You sent all crew members.", 0, 75, (0,0,0))
                    console.output("There's no way back to the ship!", 0, 100, (0,0,0))
                    globalVariables.decision += 1
                    globalVariables.crew = 0
        else:
            globalVariables.decision += 1
    elif decision == 5:
        if globalVariables.broken_solar:
            console.output("You successfully made the jump, but something seems off about the software of your ship." , 0, 0, (0,0,0))
        else:
            globalVariables.decision += 1
    elif decision == 6:
        
        console.output("You arrive at another star system.", 0, 0, (0,0,0))
        console.output("Inspect strange escape pod", 0, 25, (0,0,255))
        console.output("Leave it alone", 0, 50, (0,0,255))
        if decision == 6 and globalVariables.user_input == "inspect":
            if random.random() < 0.3:
                console.output("The escape pod is empty.", 0, 75, (0,0,0))
                globalVariables.supplies -= 1
            else:
                console.output("You found some supplies", 0, 75, (0,0,0))
                globalVariables.supplies += 2
            pygame.time.wait(2000)
            globalVariables.decision += 1
        

    elif decision == 7:
        if globalVariables.broken_solar:
            console.output("LOW POWER LOW POWER." , 0, 0, (0,0,0))
            console.output("Send a crew member to fix it", 0, 25, (0,0,255))
            console.output("Switch to power cell power", 0, 50, (0,0,255))
            if decision == 7 and globalVariables.user_input == "crew":
                if random.random() < 0.5:
                    console.output("The crew member fixes the issue.", 0, 75, (0,0,0))
                    globalVariables.broken_solar = False
                else:
                    console.output("The crew member fails to fix the issue.", 0, 75, (0,0,0))
                    globalVariables.crew -= 1
            elif decision == 7 and globalVariables.user_input == "power cell":
                console.output("You switch to power cell power.", 0, 75, (0,0,0))
                globalVariables.supplies -= 1
            globalVariables.decision += 1
        else:
            globalVariables.decision += 1

    elif decision == 8:
        console.output("You arrive at the next system.", 0, 0, (0,0,0))
        console.output("There is a huge black hole!", 0, 25, (0,0,0))
        console.output("Investigate the black hole", 0, 50, (0,0,255))
        console.output("Make the jump away", 0, 75, (0,0,255))
        if decision == 8 and globalVariables.user_input == "investigate":
            if random.random() < 0.3:
                console.output("Your ship gets too close to the black hole and is destroyed.", 0, 75, (0,0,0))
                globalVariables.crew = 0
                globalVariables.supplies = 0
            else:
                console.output("You successfully gather valuable data about the black hole.", 0, 75, (0,0,0))
        elif decision == 8 and globalVariables.user_input == "jump":
            console.output("You make the jump away.", 0, 100, (0,0,0))
            pygame.time.wait(2000)
            globalVariables.decision += 1
    elif decision == 9:
        console.output("YOU WIN!",0 ,0, (0,0,0))
        console.output("You have found the probe!",0 ,25, (0,0,0))
        pygame.time.wait(4000)
        globalVariables.victory = True

if __name__ == "__main__":
    main()
