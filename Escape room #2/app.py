        current_text += char

@@ -47,14 +27,23 @@ def slow_print(text, delay=0.1):
        time.sleep(delay)

def main():
    intro_text = (
        "Welcome to the Neon Nexus, a sprawling megacity where neon lights flicker against the backdrop of rain-soaked streets."
        " You and your team are a group of underground hackers who have stumbled upon a corporation's dark secrets."
        " The megacorp has caught wind of your investigation and has locked you inside their secure facility."
        " Your mission is to escape from three high-security rooms before the corporate enforcers arrive to silence you permanently."
        " Time to get started!")

    slow_print(intro_text, 0.1)
    quotes = [
        "Welcome to the Neon Nexus, a sprawling megacity where neon lights flicker against",
        "the backdrop of rain-soaked streets.",
        "You and your team are a group of underground hackers who have stumbled upon a",
        "corporation's dark secrets.",
        "The megacorp has caught wind of your investigation and has locked you inside",
        "their secure facility.",
        "Your mission is to escape from three high-security rooms before",
        "the corporate enforcers arrive to silence you permanently.",
        "Time to get started!"
    ]

    for quote in quotes:
        slow_print(quote, 0.05)  # Print each quote slowly
        time.sleep(1)  # Wait for 3 seconds before clearing the screen
        screen.blit(background_image, (0, 0))  # Clear the text by redrawing the background
        pygame.display.flip()  # Update the display

    running = True
    while running:

@@ -62,6 +51,9 @@ def main():
            if event.type == pygame.QUIT:
                running = False

    import first_room
    first_room.main()

    pygame.quit()
    sys.exit()



