#in here is all the functions needed to call to run the adventure.
#each area will have a outside were you can chose to go in or return to start
#this will be a text adventure.
#all answeres will be one word only.
#the adventure will be about Jeff the shark.
#He will leave his house and look for gold.
#players will pick a direction, forward,left or right, (cheat is house)
#each direction will be a area to explore and find tools to use until
# you find gold

#order of locations. lib>ship>cave

#================================ship==============================================

#forward will bring Jeff to a ship reck. he will need to search the area
#Jeff will not enter the ship without some kind of deffence. there could be danger
#the danger will be a Huge Lobster. You will need to use hodoken to kill him

#inside the ship behind the lobster  will be a a glow fish you can save 
#he will follow you inside the cave once you save him

#===================================cave============================================

#left will be cave but it will be to dark to see. jeff will need something to see inside
#if you have the glow fish he will make the cave light up and looking around will
#find you the gold and win the game

#=================================Lib===========================================

#going right Jeff will find a abandoned libarry. Going inside you will find a
#book on the floor. reading the book will give you hadoken. Knolage is power.
#in here you will learn to to throw a hodoken (fire ball)
#being able to thow a hodoken will be deffence from anything in the ship

#=======================================House===============================
#by typeing home from the starting point you can enter jeffs house. 
#inside the house is messy. by typing clean jeff will start to clean up
#his house and find a pot of gold. winning the game.

#======================================start==========================


#=================location chart==================================
'''
0=start
1=out.cave
2=out.lib
3=out.ship

#=================================================

4=inside lib
5=learn (fireball=1) then center

#=======================================

6=inside ship
7=fight
8=save(fish = 1) then center
9= death

#===============================================

10=inside cave
11=winner

#==================================================

12=inside house
13=gold

14=center


'''
#================================================================================




def start():
    intro = (''' 
             This is my first text adventure. It is about Jeff the shark and his short adventure. 
    All inputs are one word and ALL LOWERCASE, 
    IMPORTANT!!!! You can TYPE HOME at ANY POINT to return to the FRONT of JEFFS HOUSE
                                                                                      ''')
    
    print (intro)
    
    text = ( '''=================================================================
            It's early morning. Jeff is outside of his house.
    With nothing to do today and lots of bills to pay Jeff plans on searching for gold.
                                                                                          ''')
    
    print(text)
    
    action= input('First thing\'s first. What way should Jeff go?(forward, left or right.)')

    
    return action
    
def center():
    text = ('''============================================================================
            Jeff returns to the front of his house again. That gold has to be out there somewhere!
                                                                                        ''')
    
    print(text)
    
    action = input('What should Jeff do now?')
    
    return action
    

def fail():
    error = ('Not a valid input. Remember all actions are one word with no capitals')
    
    print(error)
    
    #action = input('What should Jeff do?')
    
    #return action
    
def dead ():
    text = (''' ============================================================================
            After breaking the laws of physics Jeff is not in the mood to save some tiny fish.
    As he start to swim away the ship starts to collapse from the explosion. The falling wood hitting Jeff and killing him
    GAME OVER!
                                      ''')
    
    print(text)
#=================================outside lib=right===============================

def outside_lib():
    text = ('''=============================================================================
             Jeff never liked the library but knowledge is power after all
    and he's going to need all the power he can get to find gold.
    But this place looks a little run down. Who knows if there's anything worth wild in there
                              ''')
    print(text)    
    
    action = input('What should Jeff do?')
    
    return action


#=================================in lib= ======================================

def inside_lib():
    text = ('''========================================================================
            With a flick of his tail Jeff made his way to the library door
    and opened them. The door squeeking as it revealed the inside of
    the building. The library looks abandoned and dusty. There are some books scattered around. 
    Maybe one of them can help.
                                           ''')
    print(text)
    
    action = input('What should Jeff do in the library?')
    
    return action

def learn():
    text = ('''===============================================================
            He picks up a near by book titled 'The Will to Keep Winning'.
            Jeff was never much of a reader but he was entranced by book and continued to read until he was finsihed.
            Once he was done he felt some how...more powerful. With his new abilities Jeff swims home
                       ''')
    
    print(text)


#================================outside ship==forward==============================

def outside_ship():  
    text = ('''===================================================================
            As Jeff swims around he finds a sunken pirate ship. It's crusted
    over with sea life and it looks a dangerous. Who knows what could be in there?
                       ''')
    print(text)
    
    action = input('It looks spooky in there but what should Jeff do?')
    
    return action

def scary():
    text = ('''==================================================================
            That ship looks scary to go into without some kind of weapon.''')
    print(text)

#==============================in ship=================================


def inside_ship():
    text = ('''====================================================================
            With his new skill ready to go and his head held high Jeff made
    his way into the sunken ship. It's not lit very well and smells
    kind of fishy. As Jeff looks around he hears a low pitched growl.
    He turns around and see a huge angry lobster. 
                               ''')
    print(text)
    
    action = input('What\'s the plan?')
    
    return action

def bite():
    text = (''' Jeff swims up to the lobster and bites his face. The lobster hisses at Jeff and 
            smacks him away with his claw...looks like that did nothing''')
    
    print(text)

def fight():
    text= (''' ======================================================================
           With Diago Umeharas words in his mind he looks forward at the Lobster with no fear.
           He lungers he front fins forward and yells 'HADOUKEN!!!' as a large fireball makes it's way to the lobster.
           The Lobsters frozen in it's spot is stunned. Wondering how this shark got fire to stay lit under water.
           The fireball hits the Lobster in the chest. Killing him on contact. With the lobster out of the way Jeff
           can see a small glow fish in a cage.
                                       ''')
    print(text)
    
    action = input('Should Jeff save the tiny fish?')
    return action

def run():
    text=('''struck with fear Jeffs turns tail and starts to swim away. 
          Out of the corner of his eye he can see a small fish trapped in a cage behind the lobster. 
          He can't just leave that little guy behind''')
    print(text)

def save ():
    text = (''' ======================================================================
            Jeff always did the right thing. He swims over the to small fish and unlocks the cage.
            The small fish looks thankful and starts to follow Jeff like a Pilot fish. With a new friend Jeff swims home''')
    
    print(text)



#===============================outside cave===left================================

def outside_cave():
    text = ('''===================================================================
            On his way left jeff stumbbled on a big dark cave. Maybe there's
    gold in there, Maybe there's monster or maybe there nothing but rocks.
    Either way there's no way jeff could see in there on his own
                                    ''')
    print(text)
    
    action = input('Go in the dark cave or go back?')
    
    return action

def dark():
    text = ('''That cave looks to dark to go in as is. Maybe Jeff can find a flashlight or something... ''')
    
    print(text)
#==============================in cave======================================

def inside_cave():
    text = ('''====================================================================
            With the help of his new glow fish buddy Jeff swims his way into the cave.
    What was once a black dark cave quickly turned into a orange glowing wall of rocks with only a few dark corners.
    There was something spooky about this cave but He had no clue why.
                                         ''')
    print(text)
    
    action = input('What should Jeff do in the spooky cave')
    
    return action

#=============================winning text=================================

def winner():
    text = ('''====================================================================
            Congrats! Jeff has found some gold! Putting the gold under his fin he swims home. 
    No more bills to worry about...at lest for now''')

    print(text)
#=============================inside house=================================

def house():
    text = ('''=================================================================
            With a shrug Jeff turns around and head back into his house.
    Inside it's very messy. Shirts, towles and just about everything else is on the floor.''')
    
    print(text)
    
    action = input("Should Jeff go outside again or do something else?")
    
    return action
    
    
def gold():
    
    text = ('''==================================================================
            With a bit of sigh Jeff starts to clean his house. Slowly but with progress.
    After about an hour of cleaning he looks under his bed for more things to tidy up
    and finds gold. Who would of guessed. I guess he was richer then he thought''')
    print(text)




