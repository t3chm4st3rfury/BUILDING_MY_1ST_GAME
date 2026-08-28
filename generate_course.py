# -*- coding: utf-8 -*-
# Created by Jeffrey Appleton, Age 36
# Pygame 100 Lessons - Beginner Course Generator
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib import colors
from datetime import datetime

# Create PDF
pdf_path = "Pygame_100_Lessons_Beginner_Course.pdf"
doc = SimpleDocTemplate(pdf_path, pagesize=letter,
                        rightMargin=0.5*inch, leftMargin=0.5*inch,
                        topMargin=0.75*inch, bottomMargin=0.75*inch)

# Container for PDF elements
story = []

# Define styles
styles = getSampleStyleSheet()
title_style = ParagraphStyle(
    'CustomTitle',
    parent=styles['Heading1'],
    fontSize=24,
    textColor=colors.HexColor('#1f77b4'),
    spaceAfter=12,
    alignment=1  # center
)

heading_style = ParagraphStyle(
    'CustomHeading',
    parent=styles['Heading2'],
    fontSize=14,
    textColor=colors.HexColor('#2ca02c'),
    spaceAfter=8,
    spaceBefore=12
)

lesson_style = ParagraphStyle(
    'LessonTitle',
    parent=styles['Heading3'],
    fontSize=12,
    textColor=colors.HexColor('#d62728'),
    spaceAfter=6,
    spaceBefore=10
)

body_style = ParagraphStyle(
    'CustomBody',
    parent=styles['BodyText'],
    fontSize=10,
    spaceAfter=6,
    leading=14
)

code_style = ParagraphStyle(
    'Code',
    parent=styles['BodyText'],
    fontSize=8,
    fontName='Courier',
    leftIndent=20,
    rightIndent=10,
    textColor=colors.HexColor('#333333'),
    backColor=colors.HexColor('#f0f0f0'),
    spaceAfter=6,
    borderPadding=6
)

# Title Page
story.append(Spacer(1, 0.5*inch))
story.append(Paragraph("[GAME] PYGAME 100 LESSONS", title_style))
story.append(Paragraph("Complete Beginner's Guide to Game Development", styles['Heading2']))
story.append(Spacer(1, 0.2*inch))
story.append(Paragraph("Learn Python Game Programming Step-by-Step<br/>With Code Examples and Clear Instructions", body_style))
story.append(Spacer(1, 0.3*inch))
story.append(Paragraph(f"<b>Created:</b> {datetime.now().strftime('%B %d, %Y')}", body_style))
story.append(Paragraph("<b>Level:</b> Beginner / Novice", body_style))
story.append(Paragraph("<b>Duration:</b> ~40-50 hours of learning", body_style))
story.append(PageBreak())

# Table of Contents
story.append(Paragraph("TABLE OF CONTENTS", heading_style))
story.append(Spacer(1, 0.1*inch))

toc_sections = [
    ("PART 1: SETUP AND BASICS (Lessons 1-10)", "Getting Python, Pygame, and your first program"),
    ("PART 2: DRAWING SHAPES (Lessons 11-20)", "Lines, circles, rectangles, and colors"),
    ("PART 3: KEYBOARD INPUT (Lessons 21-30)", "Making things move with the keyboard"),
    ("PART 4: MOUSE INPUT (Lessons 31-40)", "Click, drag, and detect mouse position"),
    ("PART 5: SPRITES AND OBJECTS (Lessons 41-50)", "Creating game objects and animations"),
    ("PART 6: COLLISIONS (Lessons 51-60)", "Detecting when objects touch"),
    ("PART 7: SOUNDS AND MUSIC (Lessons 61-70)", "Adding audio to your games"),
    ("PART 8: SCORE AND TEXT (Lessons 71-80)", "Displaying text, scores, and game info"),
    ("PART 9: GAME MECHANICS (Lessons 81-90)", "Timers, spawning, and game loops"),
    ("PART 10: COMPLETE GAME (Lessons 91-100)", "Build a full game from scratch"),
]

for section, desc in toc_sections:
    story.append(Paragraph(f"<b>{section}</b><br/><i>{desc}</i>", body_style))
    story.append(Spacer(1, 0.08*inch))

story.append(PageBreak())

# Lessons structure
lessons = [
    # PART 1: Setup & Basics
    ("1", "What is Pygame?", "Pygame is a Python library that helps you make games. It gives you tools to draw pictures, handle keyboard clicks, and make sounds. Think of it like LEGO for games!"),
    ("2", "Install Python on Windows", "Go to python.org, download Python 3.11 or newer, and run the installer. Make sure to check 'Add Python to PATH' during installation."),
    ("3", "Install Python on Mac", "Download Python from python.org or use Homebrew: brew install python3. Then verify with: python3 --version"),
    ("4", "Install Python on Linux", "Use your package manager: sudo apt install python3 python3-pip (Ubuntu/Debian) or sudo dnf install python3 (Fedora)"),
    ("5", "Create Your First Folder", "Make a new folder called 'pygame_games' on your desktop. This is where all your game code will live."),
    ("6", "Install Pygame Library", "Open Command Prompt (Windows) or Terminal (Mac/Linux) and type: pip install pygame"),
    ("7", "Your First Program", "Create a file called game.py with code that prints 'Hello Pygame!'. Run it with: python game.py"),
    ("8", "Understanding the Game Loop", "A game loop runs your code over and over (60 times per second). This makes animations smooth and responsive."),
    ("9", "Creating a Game Window", "Write code that opens a 500x500 pixel window. Windows stay open using pygame.display.update()"),
    ("10", "Your First Pygame Project", "Combine everything: create a window, run a game loop, and close it when you press the X button."),
    
    # PART 2: Drawing Shapes
    ("11", "Understanding Colors", "Colors are made with 3 numbers (R, G, B) from 0-255. Red = (255,0,0), Green = (0,255,0), Blue = (0,0,255)"),
    ("12", "Draw a Rectangle", "Use pygame.draw.rect() to draw boxes. Rectangle needs: screen, color, and (x, y, width, height)"),
    ("13", "Draw a Circle", "Use pygame.draw.circle() with: screen, color, (center_x, center_y), radius"),
    ("14", "Draw a Line", "Use pygame.draw.line() with: screen, color, (start_x, start_y), (end_x, end_y), thickness"),
    ("15", "Draw Polygons", "Use pygame.draw.polygon() to draw triangles and other shapes with multiple points"),
    ("16", "Mix Colors Together", "Create custom colors by mixing R, G, B values. Try (255, 128, 0) for orange!"),
    ("17", "Fill the Background", "Use screen.fill(color) at the start of your game loop to clear the screen"),
    ("18", "Draw Multiple Shapes", "Draw many shapes in one loop. Order matters - shapes drawn last appear on top"),
    ("19", "Create a Simple Scene", "Draw a background, sun, ground, and tree to practice shape drawing"),
    ("20", "Add Animation to Shapes", "Move shapes by changing their position every frame. Increase x each loop to move right."),
    
    # PART 3: Keyboard Input
    ("21", "Detect Key Presses", "Use pygame.key.get_pressed() to check if any key is held down"),
    ("22", "Move Left with Arrow Keys", "Check if LEFT arrow is pressed, then decrease the object's x position"),
    ("23", "Move Right with Arrow Keys", "Check if RIGHT arrow is pressed, then increase the object's x position"),
    ("24", "Move Up with Arrow Keys", "Check if UP arrow is pressed, then decrease the object's y position"),
    ("25", "Move Down with Arrow Keys", "Check if DOWN arrow is pressed, then increase the object's y position"),
    ("26", "Move in All 4 Directions", "Combine all 4 arrow keys so your object moves smoothly in any direction"),
    ("27", "Use WASD Keys Instead", "W=Up, A=Left, S=Down, D=Right. Check pygame.K_w, pygame.K_a, etc."),
    ("28", "Control Speed of Movement", "Instead of moving 1 pixel, move 5 pixels. Create a variable called speed = 5"),
    ("29", "Bounce Off Screen Edges", "When x < 0, set x = 0. When x > screen_width, set x = screen_width-size"),
    ("30", "Wrap Around Screen", "When object leaves right side, appear on left side. Creates a cool effect!"),
    
    # PART 4: Mouse Input
    ("31", "Get Mouse Position", "Use pygame.mouse.get_pos() to get (x, y) of mouse. Store in a variable."),
    ("32", "Draw at Mouse Position", "Draw a circle where your mouse is. The circle follows your cursor!"),
    ("33", "Detect Mouse Clicks", "Check pygame.mouse.get_pressed() to see which mouse buttons are clicked"),
    ("34", "Left Click Detection", "Check if mouse[0] is True to detect left click"),
    ("35", "Right Click Detection", "Check if mouse[2] is True to detect right click"),
    ("36", "Create Clickable Areas", "Draw rectangles and check if mouse is inside using rect.collidepoint(mouse_pos)"),
    ("37", "Change Color on Click", "When a shape is clicked, change its color. Create a variable to track state."),
    ("38", "Draw When Dragging", "While mouse button is held, draw shapes at mouse position. Releases when button lets go."),
    ("39", "Create a Paint Program", "Combine drawing and mouse - create a simple program where you paint by clicking"),
    ("40", "Detect Mouse Entering Shapes", "Check if mouse position is inside a rectangle or circle. Highlight when hovered."),
    
    # PART 5: Sprites & Objects
    ("41", "What are Sprites?", "Sprites are images in your game. They're small pictures of characters, enemies, or objects."),
    ("42", "Load an Image File", "Use pygame.image.load('filename.png') to load an image. Store it in a variable."),
    ("43", "Display an Image", "Use screen.blit(image, (x, y)) to draw the image on screen at position x, y"),
    ("44", "Scale an Image", "Use pygame.transform.scale(image, (width, height)) to make images bigger or smaller"),
    ("45", "Rotate an Image", "Use pygame.transform.rotate(image, angle) to spin images. Angle 90 = 90 degrees"),
    ("46", "Create a Player Class", "Make a class called Player with x, y, image. This organizes your code better."),
    ("47", "Move a Player Sprite", "Add movement code to your Player class. Update x and y in a method."),
    ("48", "Create Multiple Sprites", "Make a list of sprites: enemies = [Enemy(), Enemy(), Enemy()]. Store many in one list."),
    ("49", "Draw All Sprites", "Loop through your sprite list and draw each one. Use a for loop: for sprite in list:"),
    ("50", "Update All Sprites", "Call an update() method on each sprite each frame. This moves them and animates them."),
    
    # PART 6: Collisions
    ("51", "Collision Detection Basics", "Collisions happen when two things touch. We use rectangles.colliderect() to check."),
    ("52", "Get Rectangle from Image", "Every image has a rect. Use image.get_rect() to get a rectangle for collision checking."),
    ("53", "Detect Collisions with Rect", "Use rect1.colliderect(rect2) - returns True if they overlap, False otherwise"),
    ("54", "Check Player and Enemy Collision", "In your game loop, check if player.rect.colliderect(enemy.rect)"),
    ("55", "Remove Objects on Collision", "When something is hit, remove it from the list: enemies.remove(enemy)"),
    ("56", "Lose Health on Collision", "Create a health variable. When hit, health -= 1. Game over when health == 0"),
    ("57", "Bounce Off Objects", "When collision happens, reverse direction: velocity_x = -velocity_x"),
    ("58", "Collect Items", "Create coins or items. When player touches them, add points and remove the item."),
    ("59", "Check Circle Collisions", "Use math to check if circles touch. Distance between centers < sum of radii means collision."),
    ("60", "Collision Groups and Lists", "Organize collisions: check all bullets vs all enemies in a loop"),
    
    # PART 7: Sounds & Music
    ("61", "Load a Sound Effect", "Use pygame.mixer.Sound('sound.wav') to load a sound file"),
    ("62", "Play a Sound Once", "Call sound.play() to play a sound effect one time"),
    ("63", "Load Background Music", "Use pygame.mixer.music.load('song.mp3') to load music"),
    ("64", "Play Music in a Loop", "Use pygame.mixer.music.play(-1) - the -1 means loop forever"),
    ("65", "Stop Music", "Use pygame.mixer.music.stop() to stop the music"),
    ("66", "Control Volume", "Use sound.set_volume(0.5) to make sound 50% loud. 1.0 = full volume, 0.0 = silent"),
    ("67", "Play Sound on Event", "When something happens (collision, click), play a sound effect"),
    ("68", "Multiple Sound Channels", "Play many sounds at once using pygame.mixer.get_channel()"),
    ("69", "Fade Out Music", "Use pygame.mixer.music.fadeout(milliseconds) to fade music out slowly"),
    ("70", "Fade In Music", "Use set_volume(0) then gradually increase it each frame for fade-in effect"),
    
    # PART 8: Score & Text
    ("71", "Create a Font", "Use pygame.font.Font('arial.ttf', size) to create text with a specific font and size"),
    ("72", "Render Text", "Use font.render(text, True, color) to convert text to an image you can draw"),
    ("73", "Display Text on Screen", "Use screen.blit(text_image, (x, y)) to draw text just like an image"),
    ("74", "Create a Score Variable", "Make a variable score = 0. Increase it when player collects items."),
    ("75", "Display Score", "Show the score on screen: 'Score: ' + str(score)"),
    ("76", "Create a Game Over Screen", "Display text when the game ends. Fill screen with color, show message, wait."),
    ("77", "Display Lives Remaining", "Show how many lives left: 'Lives: ' + str(lives)"),
    ("78", "Display Health Bar", "Draw a rectangle that gets smaller as health decreases"),
    ("79", "Display Frames Per Second", "Calculate FPS = 1 / delta_time. Show it on screen for debugging."),
    ("80", "Show Tutorial Text", "Display instructions at game start. Wait 3 seconds, then hide."),
    
    # PART 9: Game Mechanics
    ("81", "Create a Timer", "Make timer = 0, increase every frame: timer += 1. Reset when timer > target."),
    ("82", "Spawn Enemies Every 2 Seconds", "Use timer to spawn: if timer > 120 (2 seconds): enemies.append(Enemy())"),
    ("83", "Create a Level System", "When score reaches certain points, increase level and make game harder"),
    ("84", "Increase Difficulty", "Make enemies faster, add more enemies, or reduce player speed as game progresses"),
    ("85", "Create Power-ups", "Add special items that give temporary advantages: faster speed, invincible, etc."),
    ("86", "Countdown Timer", "Start with time_left = 60. Decrease each frame. Game ends when time_left == 0"),
    ("87", "Waves of Enemies", "Spawn enemies in groups. When wave is cleared, start next wave with harder enemies"),
    ("88", "Game States", "Create states: MENU, PLAYING, GAME_OVER. Change state based on events."),
    ("89", "Pause Menu", "When P is pressed, pause the game. Draw menu, wait for button press to unpause."),
    ("90", "High Score Saving", "When game ends, check if new_score > high_score. Save high score to a file."),
    
    # PART 10: Complete Game
    ("91", "Plan Your Game", "Decide: What does player do? What are enemies? How to win/lose? Write it down!"),
    ("92", "Choose Game Type", "Simple options: Dodge enemies, Collect items, Shoot enemies, Simple puzzle"),
    ("93", "Create Main Game Loop", "Setup pygame, create window, run game loop, handle quit"),
    ("94", "Add Player Movement", "Let player move with arrow keys or WASD. Keep player on screen."),
    ("95", "Add Enemies/Obstacles", "Spawn enemies that move. Make them disappear at screen edges."),
    ("96", "Add Collision Logic", "Check collisions between player and enemies. Decrease health or collect points."),
    ("97", "Add Score and Display", "Create score variable, increase on actions, display on screen"),
    ("98", "Add Game Over Condition", "When health = 0 or time runs out, show game over screen"),
    ("99", "Add Sound Effects", "Add sounds for: movement, collision, score increase, game over"),
    ("100", "Finish Your Game!", "Test everything, fix bugs, celebrate! Share your game with friends!"),
]

# Add all lessons to PDF
for lesson_num, lesson_title, lesson_content in lessons:
    part = (int(lesson_num) - 1) // 10 + 1
    
    # Add lesson title
    story.append(Paragraph(f"<b>LESSON {lesson_num}:</b> {lesson_title}", lesson_style))
    
    # Add lesson content
    story.append(Paragraph(lesson_content, body_style))
    
    # Add beginner-friendly tip box
    tip_text = ""
    if int(lesson_num) in [7, 15, 26, 40, 58, 75, 99]:  # Add code examples for select lessons
        if lesson_num == "7":
            tip_text = "HINT - Try It:<br/>print('Hello Pygame!')"
        elif lesson_num == "15":
            tip_text = "HINT - Try It:<br/>pygame.draw.polygon(screen, (255,0,0), [(100,50), (150,100), (50,100)])"
        elif lesson_num == "26":
            tip_text = "HINT - Try It:<br/>keys = pygame.key.get_pressed()<br/>if keys[pygame.K_LEFT]: x -= 5"
        elif lesson_num == "40":
            tip_text = "HINT - Try It:<br/>mouse_pos = pygame.mouse.get_pos()<br/>if rect.collidepoint(mouse_pos):"
        elif lesson_num == "58":
            tip_text = "HINT - Try It:<br/>for coin in coins:<br/>    if player.rect.colliderect(coin.rect): score += 10"
        elif lesson_num == "75":
            tip_text = "HINT - Try It:<br/>font = pygame.font.Font(None, 36)<br/>text = font.render('Score: ' + str(score), True, (255,255,255))"
        elif lesson_num == "99":
            tip_text = "HINT - Try It:<br/>import pygame.mixer<br/>sound = pygame.mixer.Sound('jump.wav')<br/>sound.play()"
    
    if tip_text:
        story.append(Paragraph(tip_text, code_style))
    
    # Add key concept box
    story.append(Spacer(1, 0.05*inch))
    
    if int(lesson_num) % 10 == 0:  # End of each part
        story.append(Paragraph(f"[COMPLETE] PART {part} FINISHED! You have learned key concepts. Practice before moving forward!", body_style))
        story.append(PageBreak())
    elif int(lesson_num) % 5 == 0:
        story.append(Spacer(1, 0.08*inch))
    else:
        story.append(Spacer(1, 0.06*inch))

# Final page
story.append(PageBreak())
story.append(Paragraph("CONGRATULATIONS!", title_style))
story.append(Spacer(1, 0.2*inch))
story.append(Paragraph("You have completed all 100 lessons! You now have the skills to create your own games with Pygame.", body_style))
story.append(Spacer(1, 0.2*inch))
story.append(Paragraph("<b>Next Steps:</b>", lesson_style))
story.append(Paragraph("1. Review lessons you found challenging<br/>2. Create your own original game<br/>3. Add new features to existing games<br/>4. Join a game development community<br/>5. Share your games with others!", body_style))
story.append(Spacer(1, 0.2*inch))
story.append(Paragraph("Happy Game Making!", body_style))

# Build PDF
doc.build(story)
print("PDF Created: Pygame_100_Lessons_Beginner_Course.pdf")
print("Total Pages: Approximately 50-60")
print("Start with Lesson 1 and work through all 100 lessons!")
