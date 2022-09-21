import random
your_shoulder_workout = []

front_delts = ["Arnold presses", "Landmine narrow presses", "Dumbbell presses", "Barbell presses", "Smith-machine presses", "Donkey balls cable raises for front delts"]
mid_delts = ["Cable lateral raises", "Dumbbell lateral raises"]
rear_delts = ["Cable face pulls", "Cable one arm rotations for rear delts", "Cable star for rear delts"]
triceps = ["Overhand bent-over cable pushdowns", "Neutral grip bent-over cable pushdowns", "Cable star triceps pushdowns", "Dumbbell skull crushers", "Barbell skull crushers"]

your_shoulder_workout.append(random.choice(front_delts))
your_shoulder_workout.append(random.choice(mid_delts))
your_shoulder_workout.append(random.choice(rear_delts))
your_shoulder_workout.append(random.choice(front_delts))
your_shoulder_workout.append(random.choice(mid_delts))
your_shoulder_workout.append(random.choice(triceps))
your_shoulder_workout.append(random.choice(triceps))

print("Here is a workout for 3D delts BROOO")
print(your_shoulder_workout)