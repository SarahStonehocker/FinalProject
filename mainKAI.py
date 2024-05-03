import random
import globalVariables
import SolandGraphics
import sys
import pygame
import consoleKAI

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
        SolandGraphics.spaceShip(0,0, (0.5,0.5), 0.1, 0)
        if (globalVariables.location == 0):
            SolandGraphics.spaceShip(0,0, (0.5,0.5), 0.1, 0)
        else:
            break
        # Draw text input
        consoleKAI.draw()


        if game_state == RUNNING:

            # Increment decision and handle it
            #handle_game_decisions(globalVariables.decision)
            globalVariables.decision += 1

            # Check if the game is over
            if globalVariables.supplies <= 0 or globalVariables.crew <= 0:
                consoleKAI.output("Game over!")
                break
            else:
                game_state = WAITING_FOR_DECISION


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
                    else:
                        consoleKAI.key_pressed(event.key)

        # Update display
        pygame.display.update()

def handle_game_decisions(decision):
    if decision == 1:
        globalVariables.location = 0
        consoleKAI.output("How shall we proceed? Fly straight away from Earth or slingshot around the moon? ")
    elif decision == 2:
        consoleKAI.output("Jump to hyperspace now? ")
    elif decision == 3:
        if globalVariables.broken_solar:
            consoleKAI.output("Solar panel is broken! Send a crew member or robot to fix it? ")
        else:
            globalVariables.decision += 1
    elif decision == 4:
        if not globalVariables.broken_solar:
            consoleKAI.output("Interspacial law dictates that all distress signals must be investigated. How many crew members should go down to investigate? ")
        else:
            globalVariables.decision += 1
    elif decision == 5:
        if globalVariables.broken_solar:
            consoleKAI.output("You successfully made the jump, but something seems off about the software of your ship. Should we investigate the planet? ")
        else:
            globalVariables.decision += 1
    elif decision == 6:
        if not globalVariables.broken_solar:
            consoleKAI.output("You arrive at another star system. There seems to be some sort of escape pod orbiting a nearby moon. Inspect it or leave it alone? ")
        else:
            globalVariables.decision += 1
    elif decision == 7:
        if globalVariables.broken_solar:
            consoleKAI.output("Arriving at the next star system, something is very wrong. Lights are flashing in the cabin and you hear an automated voice saying LOW POWER LOW POWER. Send a crew member to fix it or switch to power cell power? ")
        else:
            globalVariables.decision += 1
    elif decision == 8:
        consoleKAI.output("You arrive at the next system, hoping that you’re getting close to the probe. However, you are immediately aware of the giant black hole at the center of this system. Should we investigate the black hole or make the jump away? ")

if __name__ == "__main__":
    main()
