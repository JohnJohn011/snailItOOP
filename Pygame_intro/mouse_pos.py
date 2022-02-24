# If you want it to collide with a certian thing

mouse_pos = pygame.mouse.get_pos()
if some_rectangle.collidepoint(mouse_pos):
    pygame.mouse.get_pressed()

# Its taking the mouse position and checking if it colliding with something,
# Then checking if its getting pressed (False, False, False) if nothing is get_pressed
# The layout is (left_click, middle_click, right_click)
# Need to figure out how to implement it for joystick and other buttons

while True:                                                      # While True loop actually implements it
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()                                        # You have to call this or it will try to loop and break unless you use this function
            exit()                                               # Have to use this to break the loop using sys tools
        if event.type == pygame.MOUSEMOTION:                     # Find mouse position (x,y)
        if event.type == pygame.MOUSEBUTTONDOWN:                 # Mouse button clicked
        if event.type == pygame.MOUSEBUTTONUP:                   # Mouse button released

        if event.type == pygame.MOUSEMOTION:
            if some_rect.collidepoint(event.pos): print('collition or whatever you want it to do')
