print(r'''
            ~  ~
              ( o )o)
             ( o )o )o)
           (o( ~~~~~~~~o
           ( )' ~~~~~~~'
           ( )|)       |-.
             o|     _  |-. \
             o| |_||_) |  \ \
              | | ||_) |   | |
             o|        |  / /
              |        |." "
              |        |- '
              .========.   mb
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You're at a cross road. Where do you want to go? ")
left_right = input('     Type "left" or "right" ')
if left_right == "left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    wait_swim = input('  Type "wait" to wait for a boat. Type "swim" to swim across.')
    if wait_swim == "wait":
        print('You arrive at the island unharmed. There is a house with 3 doors.')
        choose_color = input('One red, one Yellow and one blue. Which color do you choose?')
        if choose_color == "red":
            print("It's a room full of fire. Game Over.")
        elif choose_color == "yellow":
            print("You Found the Treasere! You Win!")
        elif choose_color == "blue":
            print("You Enter a room of Beasts. Game Over.")
    elif wait_swim == "swim":
        print("You get attacked by an angry trout. Game Over.")
elif left_right == "right":
    print("You fell into a hole. Game Over.")
