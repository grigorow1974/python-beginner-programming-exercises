import random

bullet_position = 3

def spin_chamber():
	chamber_position = random.randint(1,6)
	return chamber_position

# ❌ ⬆ DON'T CHANGE THE CODE ABOVE ⬆ ❌
def fire_gun():
	# ✅ ↓ your code here ↓ ✅
	if random.randint(1,6) == spin_chamber():
		return "You are Dead!"
	else:
		return "Keep playin!"
	


print(fire_gun())
