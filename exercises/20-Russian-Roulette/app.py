import random

bullet_position = 3

def spin_chamber():
	chamber_position = random.randint(1,6)
	return chamber_position

#  DON'T CHANGE THE CODE ABOVE
def fire_gun():
	# YOUR CODE HERE
    fire_position = random.randint(1,6)
    chamber=spin_chamber()
    if(bullet_position==chamber):
     return "You are dead!"
    else:
     return "Keep playing!"





print(fire_gun())