import random
your_leg_workout = []

quads = ["Hex machine squats", "Barbell squats", "Leg extensions", "Leg presses"]
hamstrings = ["Sitting leg curls", "Nordic curls", "Lying leg curls", "Romanian deadlifts", "Deadlifts", "Sumo deadlifts"]
calves = ["Hex machine calf raises", "Sitting calf raises", "Calf raises on machine"]
glutes = ["Hip thrust", "Hip thrust machine"]

your_leg_workout.append(random.choice(hamstrings))
your_leg_workout.append(random.choice(quads))
your_leg_workout.append(random.choice(calves))
your_leg_workout.append(random.choice(hamstrings))
your_leg_workout.append(random.choice(quads))
your_leg_workout.append(random.choice(glutes))

print("Here is a solution for your chicken legs! YOU GO GYMBRO!!!<33")
print(your_leg_workout)