# -*- coding: utf-8 -*-
# Created by Jeffrey Appleton, Age 36
# Pygame Advanced 100 Lessons - Part 2 Course Generator
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib import colors
from datetime import datetime

# Create PDF
pdf_path = "Pygame_Advanced_100_Lessons_Part2.pdf"
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
story.append(Paragraph("[ADVANCED] PYGAME 100 LESSONS - PART 2", title_style))
story.append(Paragraph("Professional Game Development & Design", styles['Heading2']))
story.append(Spacer(1, 0.2*inch))
story.append(Paragraph("Master Advanced Movement, Graphics, AI, and Game Design<br/>Build Games Inspired by DOOM, Duke Nukem, Rollercoaster Tycoon, and Command and Conquer", body_style))
story.append(Spacer(1, 0.3*inch))
story.append(Paragraph(f"<b>Created:</b> {datetime.now().strftime('%B %d, %Y')}", body_style))
story.append(Paragraph("<b>Level:</b> Intermediate / Advanced", body_style))
story.append(Paragraph("<b>Prerequisites:</b> Complete Part 1 (100 Lessons)", body_style))
story.append(Paragraph("<b>Duration:</b> ~60-80 hours of learning", body_style))
story.append(PageBreak())

# Table of Contents
story.append(Paragraph("TABLE OF CONTENTS", heading_style))
story.append(Spacer(1, 0.1*inch))

toc_sections = [
    ("PART 1: ADVANCED MOVEMENT (Lessons 1-10)", "Smooth animations, acceleration, physics"),
    ("PART 2: 2.5D & PSEUDO-3D (Lessons 11-20)", "DOOM-style engine techniques"),
    ("PART 3: ISOMETRIC GRAPHICS (Lessons 21-30)", "Rollercoaster Tycoon perspective"),
    ("PART 4: ADVANCED GRAPHICS (Lessons 31-40)", "Sprite sheets, particles, shading"),
    ("PART 5: AI SYSTEMS (Lessons 41-50)", "NPC behavior, pathfinding, decision trees"),
    ("PART 6: CAMERA SYSTEMS (Lessons 51-60)", "Smooth scrolling, zoom, pan, follow"),
    ("PART 7: LEVEL DESIGN (Lessons 61-70)", "Map generation, tile systems, design patterns"),
    ("PART 8: STRATEGY MECHANICS (Lessons 71-80)", "RTS elements, resource management, UI"),
    ("PART 9: ADVANCED PHYSICS (Lessons 81-90)", "Gravity, momentum, advanced collisions"),
    ("PART 10: PROFESSIONAL ARCHITECTURE (Lessons 91-100)", "State machines, event systems, optimization"),
]

for section, desc in toc_sections:
    story.append(Paragraph(f"<b>{section}</b><br/><i>{desc}</i>", body_style))
    story.append(Spacer(1, 0.08*inch))

story.append(PageBreak())

# Lessons structure
lessons = [
    # PART 1: Advanced Movement
    ("1", "Acceleration vs Speed", "Speed is constant movement. Acceleration makes objects gradually go faster. Use velocity variables to track momentum."),
    ("2", "Smooth Animation Curves", "Instead of linear movement, use easing functions. Objects accelerate then decelerate like real physics."),
    ("3", "Velocity Vectors", "Use (velocity_x, velocity_y) to move diagonally. Combine them for smooth movement in any direction."),
    ("4", "Deceleration and Friction", "Add friction to slow down objects. Each frame: velocity *= 0.95 creates natural drag effect."),
    ("5", "Inertial Movement", "When key is released, object continues moving then stops. Don't stop instantly - add momentum decay."),
    ("6", "Diagonal Running Animation", "Play different animation frames based on direction. Running animation has 4-8 frames per direction."),
    ("7", "Multiple Animation States", "Idle, Running, Jumping, Falling. Switch states based on input and physics state."),
    ("8", "Smooth Jumping Physics", "Jump height = initial_velocity / (2 * gravity). Peak at 50% duration. Feels responsive like Mario."),
    ("9", "Air Control During Jump", "Allow limited movement mid-air. Real games let you steer while jumping for skill-based movement."),
    ("10", "Dash and Momentum Mechanics", "Quick burst movement with cooldown. Used in Duke Nukem style action games for advanced play."),
    
    # PART 2: 2.5D & Pseudo-3D
    ("11", "Understanding Raycasting", "DOOM used raycasting to create 3D illusion. Draw vertical lines at different heights."),
    ("12", "Simple 2.5D Technique", "Draw walls taller based on distance. Closer = taller, farther = shorter. No real 3D calculations needed."),
    ("13", "Texture Mapping Basics", "Apply 2D images to walls. Different textures for top, middle, bottom of walls."),
    ("14", "First-Person Perspective", "Create a 3D-like view from player's eyes. Calculate what's visible from camera position."),
    ("15", "Wall Rendering in 2.5D", "Draw vertical slices of the game world. Each slice represents a ray's distance to wall."),
    ("16", "Sprite Scaling in 3D", "Enemies appear bigger when close, smaller when far. Scale sprite based on distance: sprite_size = original_size / distance"),
    ("17", "Depth Sorting Objects", "Draw far objects first, close objects last. This creates proper depth layering."),
    ("18", "Parallax Effect", "Background moves slower than foreground. Creates depth illusion. Used in Command and Conquer."),
    ("19", "Billboards in 3D Space", "2D sprites always face camera. Used for trees, enemies, objects in 3D games."),
    ("20", "Simple Overhead Map System", "Display minimap showing game world. Helps player navigation in large levels."),
    
    # PART 3: Isometric Graphics
    ("21", "Isometric Projection Math", "3D coordinate to 2D screen: screen_x = (x - y), screen_y = (x + y) * 0.5"),
    ("22", "Isometric Tile Grid", "Build world from grid of tiles. Each tile is diamond-shaped in isometric view."),
    ("23", "Isometric Sprite Orientation", "Sprites face one of 8 directions in isometric view. Match sprite angle to world orientation."),
    ("24", "Drawing Order in Isometric", "Sort by depth: draw tiles top-left to bottom-right. Prevents sprites from drawing incorrectly."),
    ("25", "Elevation in Isometric", "Add height to tiles. Higher tiles drawn above lower tiles. Creates layered map."),
    ("26", "Isometric Building System", "Rollercoaster Tycoon allows building structures. Check collision and elevation before placing."),
    ("27", "Isometric Camera Panning", "Move camera smoothly across isometric map. Keep screen centered on player or selection."),
    ("28", "Isometric Pathfinding", "Find path from point A to B on grid. Account for diagonal movement and elevation."),
    ("29", "Isometric UI Elements", "Draw menus and buttons in isometric game. Keep UI readable despite perspective."),
    ("30", "Rotating Isometric View", "Some games rotate the isometric grid. Recalculate all positions when view rotates."),
    
    # PART 4: Advanced Graphics
    ("31", "Sprite Sheet Animation", "Store multiple animation frames in single image. Use rect clipping to display frame by frame."),
    ("32", "Frame-Based Animation", "Update animation frame every N ticks. Control animation speed independently of game speed."),
    ("33", "Particle Systems", "Create many small sprites (particles) for effects. Explosions, fire, rain, smoke."),
    ("34", "Trail Effects", "Draw line behind moving object. Reduces alpha each frame. Creates motion blur effect."),
    ("35", "Screen Shake Effect", "Add small random offset to camera. Intensify on explosions or impacts."),
    ("36", "Color Shifting and Filters", "Apply color overlay to sprites. Darken for shadows, tint for status effects."),
    ("37", "Lighting Systems", "Darken sprites based on light distance. Create dynamic shadows and lit areas."),
    ("38", "Multiple Layers", "Draw game in layers: background, terrain, objects, effects, UI. Control depth."),
    ("39", "Sprite Flipping and Mirroring", "Flip sprites horizontally to face different directions. Saves memory vs storing separate images."),
    ("40", "Anti-Aliasing and Smoothing", "Smooth edges on scaled sprites. Use pygame.transform.smoothscale() for better quality."),
    
    # PART 5: AI Systems
    ("41", "Simple AI Behavior States", "Idle, Patrol, Chase, Attack. Switch states based on conditions."),
    ("42", "State Machine Pattern", "Formalize AI with explicit states and transitions. Clean code structure for complex behavior."),
    ("43", "Decision Trees for AI", "If-then-else logic for NPC decisions. 'If player near? Chase. If tired? Rest.'"),
    ("44", "Behavior Trees (Advanced)", "Hierarchical AI system. Better than state machines for complex behavior."),
    ("45", "Line of Sight Detection", "Can NPC see player? Cast ray from NPC to player. Check for obstacles."),
    ("46", "Pathfinding: A* Algorithm", "Find optimal path from A to B. Account for obstacles. Core of strategy game AI."),
    ("47", "Tile-Based Pathfinding", "Simplified A* on grid. Used in Rollercoaster Tycoon and Command and Conquer."),
    ("48", "Flocking and Group Behavior", "Multiple NPCs coordinate movement. Create army units that move together naturally."),
    ("49", "Personality and Variation", "Each NPC has slightly different stats. Speed, aggression, intelligence vary per unit."),
    ("50", "NPC Interaction Systems", "NPCs talk to each other. Create dialogue trees and interaction prompts."),
    
    # PART 6: Camera Systems
    ("51", "Follow Camera Basics", "Camera center on player. Smooth follow vs snap-to-center."),
    ("52", "Bounded Camera", "Keep camera within map bounds. Prevent showing outside world."),
    ("53", "Camera Smoothing", "Lerp camera position for smooth motion. Don't snap instantly."),
    ("54", "Zoom and Unzoom", "Allow player to zoom in/out. Smooth zoom transitions."),
    ("55", "Pan and Scroll", "Drag camera with mouse. Used in strategy games like Command and Conquer."),
    ("56", "Focus Multiple Objects", "Keep multiple objects in view. Calculate bounding box that includes all."),
    ("57", "Screen Edge Scrolling", "Move camera when cursor near screen edge. Classic RTS game mechanic."),
    ("58", "Parallax Scrolling", "Different layers scroll at different speeds. Background moves slower than foreground."),
    ("59", "Camera Shake Timing", "Smooth screen shake that decays. More intense initially then settles."),
    ("60", "Cinematic Camera Paths", "Define camera path points. Create cutscene camera movements."),
    
    # PART 7: Level Design
    ("61", "Tile-Based Map System", "Divide world into grid of tiles. Each tile has type: grass, wall, water."),
    ("62", "Tile Collision Map", "Separate data structure showing which tiles are walkable."),
    ("63", "Multi-Layer Terrain", "Different tile layers: ground, decoration, overhead. Create depth."),
    ("64", "Procedural Map Generation", "Create random maps algorithmically. Used in roguelike games."),
    ("65", "Perlin Noise for Terrain", "Smooth random terrain generation. Mountains, valleys, plateaus."),
    ("66", "Dungeon Generation Algorithms", "Create maze-like dungeons procedurally. Binary space partitioning."),
    ("67", "Tile Placement Rules", "Ensure map is navigable. Check connectivity between tiles."),
    ("68", "Object Spawning Zones", "Mark areas for enemies, items, NPCs. Spawn procedurally or from data."),
    ("69", "Level Editor Tools", "Create custom levels easily. Visual tile placement interface."),
    ("70", "Saving and Loading Levels", "Store level data to file. Load and recreate level from data."),
    
    # PART 8: Strategy Mechanics
    ("71", "Resource Management System", "Track resources: gold, wood, energy. Gain resources over time."),
    ("72", "Building Construction", "Place buildings that cost resources. Buildings produce resources or unlock abilities."),
    ("73", "Unit Training and Spawning", "Build units from buildings. Queue units for production like in RTS games."),
    ("74", "Fog of War System", "Areas not visible are hidden. Reveals when units explore. Classic RTS mechanic."),
    ("75", "Unit Selection and Groups", "Select single unit or group. Issue commands to selection."),
    ("76", "RTS-Style Command System", "Right-click to move, attack, build. Left-click to select."),
    ("77", "Minimap with Visibility", "Show terrain and units on minimap. Respect fog of war."),
    ("78", "Base Management", "Track buildings, units, resources. Show status in UI. Like Rollercoaster Tycoon management."),
    ("79", "Research and Upgrades", "Spend resources to unlock new abilities or improve units."),
    ("80", "Terrain Deformation", "Terrain changes as you build. Dig paths, flatten land, create water features."),
    
    # PART 9: Advanced Physics
    ("81", "Gravity Implementation", "Apply downward force each frame. velocity_y += gravity. Objects fall naturally."),
    ("82", "Terminal Velocity", "Maximum falling speed. velocity_y = min(velocity_y, max_fall_speed)."),
    ("83", "Bounciness and Elasticity", "Objects bounce on collision. velocity *= -bounce_factor. Different materials bounce differently."),
    ("84", "Rotation Physics", "Objects spin based on angular velocity. Update rotation each frame."),
    ("85", "Friction Between Objects", "Sliding friction opposes motion. Different surface types have different friction."),
    ("86", "Momentum Conservation", "When objects collide, exchange momentum. Realistic collision physics."),
    ("87", "Force and Impulse Application", "Apply instantaneous force on collision. Impulse = mass * velocity_change."),
    ("88", "Rigid Body Dynamics", "Full physics: position, velocity, acceleration, rotation, angular velocity."),
    ("89", "Continuous Collision Detection", "Detect collisions at intermediate frames. Prevent fast objects passing through walls."),
    ("90", "Soft Body Physics", "Objects deform on impact. Cloth, jelly, flexible structures."),
    
    # PART 10: Professional Architecture
    ("91", "Game Architecture Patterns", "Separate logic, rendering, input. Clean code organization."),
    ("92", "Entity Component System", "Objects have components. Flexibility in behavior and data organization."),
    ("93", "Event System", "Objects communicate via events. Decoupled communication between systems."),
    ("94", "Resource Manager", "Load and cache resources (images, sounds, fonts). Avoid redundant loading."),
    ("95", "Game State Management", "Handle game states: MENU, PLAYING, PAUSED, GAME_OVER. Clean transitions."),
    ("96", "Configuration Files", "Store game settings in file. Easy tweaking without recompile."),
    ("97", "Debug Mode and Logging", "Add debug overlay showing FPS, coordinates, collisions. Save logs for troubleshooting."),
    ("98", "Performance Optimization", "Reduce draw calls, use object pooling, cull off-screen objects. Optimize hot paths."),
    ("99", "Cross-Platform Compatibility", "Ensure game works on Windows, Mac, Linux. Test on each platform."),
    ("100", "Publishing Your Game", "Build executable, create installer, distribute on itch.io or Steam. Share your work!"),
]

# Add all lessons to PDF
for lesson_num, lesson_title, lesson_content in lessons:
    part = (int(lesson_num) - 1) // 10 + 1
    
    # Add lesson title
    story.append(Paragraph(f"<b>LESSON {lesson_num}:</b> {lesson_title}", lesson_style))
    
    # Add lesson content
    story.append(Paragraph(lesson_content, body_style))
    
    # Add code examples for select lessons
    tip_text = ""
    if int(lesson_num) in [4, 12, 21, 31, 41, 51, 61, 71, 81, 91]:
        if lesson_num == "4":
            tip_text = "CODE EXAMPLE:<br/>velocity_x *= 0.95<br/>velocity_y *= 0.95"
        elif lesson_num == "12":
            tip_text = "CODE EXAMPLE:<br/>wall_height = base_height / distance<br/>draw_wall(x, y, width, wall_height)"
        elif lesson_num == "21":
            tip_text = "CODE EXAMPLE:<br/>screen_x = iso_x - iso_y<br/>screen_y = (iso_x + iso_y) * 0.5"
        elif lesson_num == "31":
            tip_text = "CODE EXAMPLE:<br/>frame = current_time // frame_duration<br/>rect = (frame * width, 0, width, height)"
        elif lesson_num == "41":
            tip_text = "CODE EXAMPLE:<br/>if player_near: state = CHASE<br/>elif at_patrol_end: state = IDLE"
        elif lesson_num == "51":
            tip_text = "CODE EXAMPLE:<br/>camera_x = lerp(camera_x, player_x, 0.1)<br/>camera_y = lerp(camera_y, player_y, 0.1)"
        elif lesson_num == "61":
            tip_text = "CODE EXAMPLE:<br/>tile_type = tile_map[y // tile_size][x // tile_size]<br/>draw_tile(x, y, tile_type)"
        elif lesson_num == "71":
            tip_text = "CODE EXAMPLE:<br/>gold += gold_per_second / 60<br/>if gold >= building_cost: can_build = True"
        elif lesson_num == "81":
            tip_text = "CODE EXAMPLE:<br/>velocity_y += gravity<br/>position_y += velocity_y"
        elif lesson_num == "91":
            tip_text = "CODE EXAMPLE:<br/>class Game:<br/>    def update(self): ...<br/>    def render(self): ..."
    
    if tip_text:
        story.append(Paragraph(tip_text, code_style))
    
    # Add section breaks
    story.append(Spacer(1, 0.05*inch))
    
    if int(lesson_num) % 10 == 0:
        story.append(Paragraph(f"[COMPLETE] PART {part} FINISHED! You've mastered advanced concepts for this area.", body_style))
        story.append(PageBreak())
    elif int(lesson_num) % 5 == 0:
        story.append(Spacer(1, 0.08*inch))
    else:
        story.append(Spacer(1, 0.06*inch))

# Final page
story.append(PageBreak())
story.append(Paragraph("YOU'RE NOW A GAME DEVELOPER!", title_style))
story.append(Spacer(1, 0.2*inch))
story.append(Paragraph("You have completed all 200 lessons (Part 1 + Part 2)! You now have professional-level game development skills.", body_style))
story.append(Spacer(1, 0.2*inch))
story.append(Paragraph("<b>What You Can Build Now:</b>", lesson_style))
story.append(Paragraph("Action Games (like Duke Nukem, DOOM)<br/>Strategy Games (like Command and Conquer, Rollercoaster Tycoon)<br/>Complex Simulations<br/>Isometric RPGs<br/>Real-Time Management Games<br/>Indie Games for Distribution", body_style))
story.append(Spacer(1, 0.2*inch))
story.append(Paragraph("<b>Recommended Next Steps:</b>", lesson_style))
story.append(Paragraph("1. Study professional game engines (Godot, Unity)<br/>2. Join game dev communities and forums<br/>3. Play classic games you learned from - study their design<br/>4. Create your own original game concept<br/>5. Contribute to open-source game projects<br/>6. Consider a career in game development!<br/>7. Keep learning and iterating on your skills", body_style))
story.append(Spacer(1, 0.2*inch))
story.append(Paragraph("<b>Happy Game Making!</b> - Your journey as a game developer is just beginning.", body_style))

# Build PDF
doc.build(story)
print("PDF Created: Pygame_Advanced_100_Lessons_Part2.pdf")
print("Total Pages: Approximately 50-60")
print("Build advanced games inspired by classic PC titles!")
