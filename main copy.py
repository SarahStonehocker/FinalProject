import random
from SolandGraphics import char1Idle
from SolandGraphics import setup
from SolandGraphics import drawBackground
from SolandGraphics import index
import SolandGraphics

import pygame
import time

def main():
    #----------Screen Set up
    pygame.init()
    SolandGraphics.setup()
    #Start Game
    run = True
    while run:
        #update background
        SolandGraphics.drawBackground()
        
        SolandGraphics.char1Idle(300,-100, (0.5,0.5), 0.2, 0) #position , size, time Between frames, type of animation (0 = idle), index

        #even handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        pygame.display.update()

    pygame.quit()
    #--------End

    #region Text Game
    supplies = 10
    crew = 3
    broken_solar = False

    print("Welcome aboard captain!")
    name = input("Please enter your name: ")
    print(f"Welcome aboard, Captain {name}!")

    while True:
        print("\nCurrent Supplies:", supplies)
        print("Current Crew Members:", crew)

        # Decision 1: Choose exit strategy from solar system
        exit_strategy = input("How shall we proceed? Fly straight away from Earth or slingshot around the moon? ")
        if exit_strategy.lower() == "fly":
            supplies -= 2
        elif exit_strategy.lower() == "slingshot":
            supplies -= 1
        else:
            print("Invalid input, please try again.")
            continue

        print("\nCurrent Supplies:", supplies)
        print("Current Crew Members:", crew)

        # Decision 2: Attempt hyperspace jump
        hyperspace_jump = input("Jump to hyperspace now? ")
        if hyperspace_jump.lower() in ["jump", "ready", "go"]:
            hyperdrive_breakdown = random.random() < 0.3
            if hyperdrive_breakdown:
                print("Hyperdrive broken! We need to fix it.")
                repair_hyperdrive = input("Repair the hyperdrive? ")
                if repair_hyperdrive.lower() == "hyperdrive":
                    print("Hyperdrive repaired! Jump successful.")
                    supplies -= 2
                else:
                    print("Hyperdrive not repaired. Jump aborted.")
                    continue
            else:
                print("Jump successful!")
                supplies -= 1
        else:
            print("Invalid input, please try again.")
            continue

        print("\nCurrent Supplies:", supplies)
        print("Current Crew Members:", crew)
        
        broken_solar = random.random() < 0.5
        # Decision 3: Fix solar panel
        if broken_solar:
            while True:
                print("Solar panel is broken!")
                fix_solar_panel = input("Send a crew member or robot to fix it? ")
                if fix_solar_panel.lower() == "crew":
                    repair_success = random.random() < 0.6
                    if repair_success:
                        print("Solar panel repaired!")
                        broken_solar = False
                        break
                    else:
                        print("Crew member lost while fixing the solar panel.")
                        crew -= 1
                        break
                elif fix_solar_panel.lower() == "robot":
                    print("Sending a robot to fix the solar panel...")
                    # Redirect to Decision 3
                    continue
                else:
                    print("Invalid input, please try again.")
                    continue

        print("\nCurrent Supplies:", supplies)
        print("Current Crew Members:", crew)

        # Decision 4: Investigate distress signal
        if not broken_solar:
            while True:
                print("Interspacial law dictates that all distress signals must be investigated.")
                crew_to_send = int(input("How many crew members should go down to investigate? "))
                hostile_intelligence = random.random() < 0.3
                if hostile_intelligence and crew_to_send == 1:
                    print("Crew member never heard from again.")
                    crew -= 1
                    break
                elif hostile_intelligence and crew_to_send == 2:
                    print("Crew members fought off the enemies and escaped.")
                    crew -= 2
                    break
                elif not hostile_intelligence:
                    print("Crew returns empty handed.")
                    supplies -= 1
                    break
                else:
                    print("Invalid input, please try again.")
                    continue

        print("\nCurrent Supplies:", supplies)
        print("Current Crew Members:", crew)

        # Decision 5: Next actions
        if broken_solar:
            while True:
                print("You successfully made the jump, but something seems off about the software of your ship.")
                planet_discovery = input("Should we investigate the planet? ")
                if planet_discovery.lower() == "yes":
                    print("Investigating the planet...")
                    crew -= 1  # Loss of one crew member
                    break
                elif planet_discovery.lower() == "no":
                    print("Moving on...")
                    supplies -= 1  # Loss of one supply
                    break
                else:
                    print("Invalid input, please try again.")
                    continue

        print("\nCurrent Supplies:", supplies)
        print("Current Crew Members:", crew)

        # Decision 6: Investigate escape pod
        if not broken_solar:
            while True:
                print("You arrive at another star system. There seems to be some sort of escape pod orbiting a nearby moon.")
                investigate_pod = input("Inspect it or leave it alone? ")
                if investigate_pod.lower() == "inspect":
                    print("Inspecting the escape pod...")
                    # Implement the outcome of inspecting the escape pod
                    print("You find a small alien inside. He agrees to join you in return for rescuing him.")
                    crew += 1  # Gain one crew member
                    break
                elif investigate_pod.lower() == "leave":
                    print("Leaving the escape pod alone...")
                    supplies -= 1  # Loss of one supply for making the jump to hyperspace
                    break
                else:
                    print("Invalid input, please try again.")
                    continue

        print("\nCurrent Supplies:", supplies)
        print("Current Crew Members:", crew)

        # Decision 7: Resolve power issue
        if broken_solar:
            while True:
                print("Arriving at the next star system, something is very wrong. Lights are flashing in the cabin and you hear an automated voice saying LOW POWER LOW POWER.")
                fix_power_issue = input("Send a crew member to fix it or switch to power cell power? ")
                if fix_power_issue.lower() == "crew":
                    print("Sending a crew member to fix the power issue...")
                    crew_survival = random.random() < 0.1  # 1/10 chance crew member is killed
                    if crew_survival:
                        print("Crew member successfully fixes the power issue.")
                        broken_solar = False
                        break
                    else:
                        print("Tragically, the crew member is killed while attempting to fix the power issue.")
                        crew -= 1
                        continue
                elif fix_power_issue.lower() == "power cell":
                    print("Switching to power cell power...")
                    supplies = 2  # Limited supplies, only 2 jumps left
                    break
                else:
                    print("Invalid input, please try again.")
                    continue

        # Decision 8: Investigate black hole
        while True:
            print("You arrive at the next system, hoping that you’re getting close to the probe. However, you are immediately aware of the giant black hole at the center of this system.")
            investigate_black_hole = input("Should we investigate the black hole or make the jump away? ")
            if investigate_black_hole.lower() == "investigate":
                print("You fly closer to the black hole. As you do, alarms start blaring. It seems you’re nearing the event horizon.")
                print("You go to turn around but feel the tug of gravity on your ship. You eventually escape, making the jump as fast as possible.")
                supplies -= 2
                break
                
            elif investigate_black_hole.lower() == "make the jump away":
                print("You jump to hyperspace.")
                supplies -= 1
                break
            else:
                print("Invalid input, please try again.")
                continue

        # End condition
        if supplies <= 0 or crew <= 0:
            print("Game over!")
            break
        else:
            print("Congratulations! You win!")
            break

        #endregion

if __name__ == "__main__":
    main()
