answer_A = ["A", "a"]
answer_B = ["B", "b"]

gold_coins = 0
health = 0


def beginning(health, gold_coins):
    health = 0
    gold_coins = 0
    print("Welcome to Dragon Island!  This beautiful land is populated by beautiful and kind dragons.  \nYou found a baby dragon alone on the side of the road and, because you are a kind stranger, you decide to bring it back to its nest.  \nLet's go!")
    print("\nYou start your travels with 50 gold coins and a small pouch of food, giving you 100 health points.")
    gold_coins += 50
    health += 100

    choice = input(
        "Do you want to travel through the valley or the forest?  \nChoose A for the valley or choose B for the forest: ")
    if choice in answer_A:
        valley(health, gold_coins)

    elif choice in answer_B:
        forest(health, gold_coins)

    else:
        print("\n\nPlease choose option A or B.  Let's keep the adventure going!\n\n")
        beginning(health, gold_coins)


def forest(health, gold_coins):
    print("\nYou have entered an old growth forest.  One step at a time, you travel further into the trees and shadows. \nSuddenly up ahead, you see a forest witch working in their garden.")
    print("Will you go to their gate and say 'hi' or will you hide in the roots of the tree?")

    choice = input(
        "\nChoose A for approaching the gate or choose B for hiding in the tree roots: ")
    if choice in answer_A:
        print("You approach the gate, baby dragon held close.  \nThe forest witch is so moved by your kindness to help the baby dragon that she offers you \na protection spell, a hot meal and some gold to get more food!")
        print("You added 75 to your health and earned 50 gold coins!")
        # gain points and health equation here
        health += 75
        gold_coins += 50
        print("You now have ", str(health), "health points and ",
              str(gold_coins), "gold coins!\n")
        print("You made it through the forest, finding the road once again.  The dragon has eaten all your food, so you head to the nearest town to resupply.")
        town(health, gold_coins)

    elif choice in answer_B:
        print("\nYou hide in the tree roots, waiting for the forest witch to go back into their cottage, so that you can slip past.  \nThey spend the evening in their garden and you fall asleep.")
        print("You wake in the middle of the night to find the baby dragon has eaten your food.  \nYou sneak past the witch's cottage, stumbling around in the dark to get out of the forest.")
        print("You make it out of the forest by sunrise, hungry and scratched.  Lose 25 health points.")
        # lose 25 health points
        health -= 25
        print("\nYou now have", str(health), "health points left.")
        print("You head to the nearest town to resupply.")

        town(health, gold_coins)

    else:
        print("\n\nPlease choose option A or B.  Let's keep the adventure going!\n\n")
        forest(health, gold_coins)


def valley(health, gold_coins):
    print("\nYou have entered a grassy valley.  One step at a time, you travel further through the tall grass.  \nSuddenly up ahead, you see a Maned Wolf standing as still as a statue.")
    print("Will you approach the wolf to check on it or will you hide in the grass til it passes?")

    choice = input(
        "\nChoose A for approaching the Maned Wolf or choose B for Hiding in the Grass: ")
    if choice in answer_A:
        print("\nYou approach the Maned Wolf cautiously.  When you draw close, you noticed that their paw is stuck with a nail.  \nThe Maned Wolf has been sitting for a couple of days and has grown quite hungry.\n")
        print("You give it some leftover bread from your supply and help get the nail out of their paw.  The baby dragon seals the wound with a hot lick.  \nThe Maned Wolf is so thankful that they share from their stash of gold coins and tell you a shortcut through the valley.\n")
        print("You added 75 to your health and earned 50 gold coins.")

        # gain points and health equation here
        health += 75
        gold_coins += 50
        print("You now have", str(health), "health points and ",
              str(gold_coins), "gold coins!\n")
        print("You make it through the valley and head to the nearest town to resupply for the journey.")
        town(health, gold_coins)

    elif choice in answer_B:
        print("\nYou are fearful of the Maned Wolf and hide, hoping they will move on soon.  \nAfter a night and a day, they start to hobble away in the other direction.")
        print("While you wait, you feed the baby dragon the last of your rations to keep it quiet. \nYou are now mostly out of food and quite hungry.  Lose 25 health points.\n")
        # lose 25 health points
        health -= 25
        print("You now have", str(health), "points left")
        print("You head to the nearest town to get more food.")
        town(health, gold_coins)

    else:
        print("\n\nPlease choose option A or B.  Let's keep the adventure going!\n\n")
        valley(health, gold_coins)


def town(health, gold_coins):
    print("\nYou make it to a small town by evening and you are famished!  \nThis late in the day, only two restaurants are open - A Taco Shack and a Tiny Pub.")
    print("Will you head to the Taco Shack or follow the dragon's nose to the Tiny Pub?\n")

    choice = input(
        "Choose A for eating at the Taco Shack or Choose B for going to the Tiny Pub: ")
    if choice in answer_A:
        print(
            "\nYou are so hungry after your travels and order a huge order of spicy tacos!")
        print("You aren't sure about feeding the baby dragon tacos, but what could it hurt!?!?\n\n")
        print("Turns out that when dragons eat spicy tacos, they tend to sneeze and cough fire balls!  \nThe Taco Shack quickly catches on fire, everyone running out as quickly as possible\n")
        print("Lose 50 health points as you barely make it out of the fire!")
        # lose 50 health points
        health -= 50
        print("You now have", str(health), "health points left.")
        print("Let's keep moving along!")
        fork_in_the_road(health, gold_coins)

    elif choice in answer_B:
        print("You followed the dragon's nose to the Tiny Pub.")
        print("You ordered a platter of fish and potatoes, the baby dragon's favorite.  After a full belly nap, the baby dragon sniffs something under the bench.  \nYou investigate and find a pouch of gold coins!\n")
        print("Before you leave the town, you are able to buy more food for your travels.  You earn 50 health points and 15 additional gold coins")
        # gain 50 health points and 15 gold coins
        health += 50
        gold_coins += 15
        print("You now have", str(health), "health points and",
              str(gold_coins), "gold coins!")
        print("Let's keep moving along!")
        fork_in_the_road(health, gold_coins)

    else:
        print("\n\nPlease choose option A or B.  Let's keep the adventure going!\n\n")
        town(health, gold_coins)


def fork_in_the_road(health, gold_coins):
    print("\nSuddenly the road splits and you need to choose which path will lead to the dragon's home.")
    print("Dragons can live in the cave below the mountain or on an outcropping on the mountainside.")
    print("\nWhich way will you go - into the Cave or up the Mountain?")

    choice = input("Choose A for Cave or Choose B for Mountain: ")
    if choice in answer_A:
        print("\nYou travel along a narrow path and eventually find the entrance to the cave.\n")
        cave(health, gold_coins)

    elif choice in answer_B:
        print("\nYou travel up a steep path towards a distinct outcropping on the side of the mountain.")
        mountain(health, gold_coins)

    else:
        print("\n\nPlease choose option A or B.  Let's keep the adventure going!\n\n")
        fork_in_the_road(health, gold_coins)


def cave(health, gold_coins):
    print("You step into the darkness of the cave, and when your eyes adjust, you notice a faint glow ahead.  \nThe baby dragon slips out of your grasp and gallops ahead.  You follow along and enter a great cavern filled with dragons!\n")
    print("The dragons are so grateful for returning their baby and share gifts with you for your troubles.")
    print("You leave the cave with a full purse of gold coins and a healing salve!")
    print("You gain 75 health points and 100 gold coins!")
    # gain 75 health and 100 gold coins
    health += 75
    gold_coins += 100
    print("You now have", str(health), "health points and",
          str(gold_coins), "gold coins!\n")

    choice = input(
        "Would you like to start over or exit?  Choose A for start over or Choose B to exit: ")
    if choice in answer_A:
        print("\nLet's start this adventure over again!")
        beginning(health, gold_coins)

    elif choice in answer_B:
        print("Thanks for adventuring along!")
        exit()

    else:
        print("\n\nPlease choose option A or B.  Will you keep adventuring?\n\n")
        cave(health, gold_coins)


def mountain(health, gold_coins):
    print("You reach the outcropping, finally making it up the side of the mountain!  You are greeted by a hippogriff family.  \nYou bow and wait to see if they will welcome you to their home.\n")
    print("The Hippogriff family recoginizes the baby dragon and are kind enough to carry the dragon the rest of the way home.")
    print("\nYou travel back down the mountain and unfortunately find yourself in the middle of a snow storm.  \nYou stumbled through the thickening snow, losing traction a few times and spilling out your leftover food and some of your gold coins.")
    # lose 20 health points and 25 gold coins
    health -= 20
    gold_coins -= 25
    print("You now have", str(health), "health points and",
          str(gold_coins), "gold coins left.")

    choice = input(
        "\nWould you like to start over or exit?  Choose A for start over or Choose B to exit: ")
    if choice in answer_A:
        print("Let's start this adventure over again!\n\n")
        beginning(health, gold_coins)

    elif choice in answer_B:
        print("Thanks for adventuring along!\n\n")
        exit()

    else:
        print("\n\nPlease choose option A or B.  Will you keep adventuring?\n\n")
        mountain(health, gold_coins)


print("\nLet's go on an adventure!  Come Along!\n")
beginning(health, gold_coins)
