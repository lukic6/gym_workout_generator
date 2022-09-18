#select body par workout randomizer
select_body_part = input("Which body part would you like to exercise today?")

import random
from turtle import back
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

if select_body_part=="back":
    print("Your exercises for V shap back workout are:")
    print(your_back_workout)
elif select_body_part=="legs":
    print("Are you stupid, skip legs and do chest!? Anyway here is a solution for your chicken legs:")
elif select_body_part=="chest":
    print("YEAAAAH BEAST here is your chest workout:")
elif select_body_part=="shoulders":
    print("Here is your workout for 3D boulder shoudlers:")
else:
    print("Please insert either chest, back, shoulders or legs as an input :)")
