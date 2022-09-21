# CHEST WORKOUT
import random


your_chest_workout = []

mid_chest = ["Barbell benchpresses", "Dumbbell benchpresses", "Machine presses", "Smith-machine bench presses"]
upper_chest = ["Incline dumbbell presses", "Incline barbell presses", "Incline presses on machine", "Incline Smith-machine presses"]
lower_chest = ["Dips", "Cables for lower pecs"]
inner_chest = ["Cable flies", "Machine flies"]
short_head_triceps = ["Overhand bent-over cable pushdowns", "Barbell skull crushers", "Narrow grip Smith-machine bench presses"]
long_head_triceps = ["Neutral grip bent-over cable pushdowns", "Cable star triceps pushdowns", "Dumbbell skull crushers"]

your_chest_workout.append(random.choice(mid_chest))
your_chest_workout.append(random.choice(upper_chest))
your_chest_workout.append(random.choice(lower_chest))
your_chest_workout.append(random.choice(inner_chest))
your_chest_workout.append(random.choice(short_head_triceps))
your_chest_workout.append(random.choice(long_head_triceps))

print("Lets get ready to RUUUMBLE:")
print(your_chest_workout)