# BACK WORKOUT EXERCISES RANDOMIZER
import random
your_back_workout = []

vertical_exercises = ["lat pulldowns", "assisted pullups", "wide neutral grip lat pulldowns", "lat pulldowns on machine", "narrow neutral lat pulldowns"]
horizontal_upper_exercises = ["bent over machine rows", "wide grip rows with barbell", "wide grip rows on cable machine", "wide grip rows on machine", "wide grip dumbbell rows"]
horizontal_lower_exercises = ["neutral rows on machine", "neutral rows on cable machine", "neutral dumbbells rows", "narrow grip barbell rows"]
pullover_exercises = ["machine pullovers", "cable overhand pullovers", "cable underhand pullovers"]
biceps_exercises = ["cross-body curls", "arms supported barbell curls", "star curls on cables", "underhand dumbbells curls", "standing barbell curls", "neutral grip dumbbells curls"]

random_ver_exercise = random.choice(vertical_exercises)
your_back_workout.append(random_ver_exercise)

random_upper_hor_exercise = random.choice(horizontal_upper_exercises)
your_back_workout.append(random_upper_hor_exercise)

random_lower_hor_exercise = random.choice(horizontal_lower_exercises)
your_back_workout.append(random_lower_hor_exercise)

random_pullover_exercise = random.choice(pullover_exercises)
your_back_workout.append(random_pullover_exercise)

random_bi1_exercise = random.choice(biceps_exercises)
your_back_workout.append(random_bi1_exercise)

random_bi2_exercise = random.choice(biceps_exercises)
your_back_workout.append(random_bi2_exercise)

print(your_back_workout)