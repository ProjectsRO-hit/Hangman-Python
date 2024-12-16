import random

def get_chosen_word():
    word_lists = [
        "apple", "banana", "orange", "grape", "cherry", "peach", "pear",
        "lemon", "melon", "berry", "carrot", "potato", "onion", "garlic",
        "tomato", "pizza", "burger", "pasta", "salad", "sugar", "honey",
        "bread", "butter", "cheese", "chicken", "bottle", "pencil",
        "paper", "laptop", "mobile", "window", "garden", "ocean", "river",
        "island", "desert", "school", "teacher", "doctor", "family",
        "animal", "tiger", "zebra", "monkey", "camel", "giraffe", "parrot",
        "eagle", "forest", "planet", "galaxy", "cloud", "mountain", "bridge",
        "castle", "friend", "travel", "advice", "guitar", "pillow", "mirror"
    ]
    return random.choice(word_lists)
