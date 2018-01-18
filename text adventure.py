import af

death = 0
win = 0
fish = 0
fireball = 0
location = 0
action = ''


while location == 0:
    action = (af.start())

    if action == 'left': #leding to cave  
        location = 1
    
        
    elif action == 'right': #leading to lib
        location = 2
    
    
    elif action == 'forward': #leading to ship
        location = 3
    
        
    else:                 #fail input
        print(af.fail())

while win !=1: 
    
    while location == 1: # outside cave
        action =(af.outside_cave())
        
        if action == 'enter' or action =='go':
            if fish == 1:
                location = 10
            else:
                print(af.dark())
        elif action == 'home':
            location = 14
        
        elif action == '?':
            print('type home to get back to jeffs house. there could be a light source somewhere else')
            
        else:
            action =(af.fail())
       
    while location == 2: # outside lib
        action =(af.outside_lib())
        if action == 'enter' or action =='go':
            location = 4
        elif action == 'home':
            location = 14
            
        elif action == '?':
            print('type home to get to jeffs house. inside the building could be interesting things')
            
        else:
            action =(af.fail())
        
        
    while location == 3: # outside ship
        action =(af.outside_ship())
        if action == 'enter' or action =='go':
            if fireball == 1:
                location = 6
            else:
                print(af.scary())
        elif action == 'home':
            location = 14
            
        elif action == '?':
            print('')
            
        else:
            action =(af.fail())
        
        
    while location == 4: # inside lib
        action =(af.inside_lib())
        if action == 'read' or action =='study':
            location = 5
        
        elif action == 'home':
            location = 14
            
        else:
            action =(af.fail())
        
        
        
    while location == 5: # learn then return to center(14)
        action =(af.learn())
        fireball=1
        location = 14
        
    while location == 6: # inside ship
        action =(af.inside_ship())
        if action == 'attack' or action =='fight':
            location = 7
            
        elif action == 'bite':
            print(af.bite())
            
        elif action == 'run':
            print(af.run())
        
        else:
            action =(af.fail())
        
        
    while location == 7: # fight
        action =(af.fight())
        if action == 'save' or action =='yes':
            location = 8
        elif action =='leave' or action =='no':
            location = 9
        else:
           action =(af.fail())
        
    while location == 8: # save fish then center(14)
        action = (af.save())
        fish = 1
        location = 14
    
    while location == 9: # death location = 99 (not real) win =1 death =1. should end game
        print(af.dead())
        win = 1
        death = 1
        location = 99
        
    while location == 10: # inside cave
        action = (af.inside_cave())
        if action == 'search':
            location = 11
        elif action == 'home':
            location == 14
        else:
            action = (af.fail())
        
    while location == 11: #winner
        action = (af.winner())
        location = 99
        win = 1
        
    while location == 12: # inside house
        action = (af.house())
        if action == 'clean':
            location = 13
        elif action == 'exit':
            location = 14
        else:
            action = (af.fail())
            
        
    while location == 13: # house gold
        action =(af.gold())
        location = 99
        win = 1
    
    while location == 14: # center house=12,  #cave 1 left , lib  2right, ship 3 forward
        action = (af.center())
        if action == 'left':
            location = 1
        elif action == 'right':
            location = 2
        elif action == 'forward':
            location = 3
        elif action == 'house':
            location = 12
        else:
            action = (af.fail())
            
        
    
    


if death == 1:
    print('You found the bad ending. Try again for the good ending')
    
    
else:
    print('Good job! you have finished Jeffs adventure. There are a few easter eggs to find tho')

    
















