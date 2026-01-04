data = [
    {
        "name": "Cristiano Ronaldo",
        "follower_count": 670_000_000,
        "description": "Footballer",
        "country": "Portugal",
        "gender": "Male"
    },
    {
        "name": "Lionel Messi",
        "follower_count": 510_000_000,
        "description": "Footballer",
        "country": "Argentina",
        "gender": "Male"
    },
    {
        "name": "Selena Gomez",
        "follower_count": 424_000_000,
        "description": "Singer & Actress",
        "country": "United States",
        "gender": "Female"
    },
    {
        "name": "Ariana Grande",
        "follower_count": 376_000_000,
        "description": "Singer & Actress",
        "country": "United States",
        "gender": "Female"
    },
    {
        "name": "Dwayne Johnson",
        "follower_count": 395_000_000,
        "description": "Actor & Entertainer",
        "country": "United States",
        "gender": "Male"
    },
    {
        "name": "Beyoncé",
        "follower_count": 316_000_000,
        "description": "Singer & Performer",
        "country": "United States",
        "gender": "Female"
    },
    {
        "name": "Justin Bieber",
        "follower_count": 294_000_000,
        "description": "Singer",
        "country": "Canada",
        "gender": "Male"
    },
    {
        "name": "Kylie Jenner",
        "follower_count": 396_000_000,
        "description": "Media Personality",
        "country": "United States",
        "gender": "Female"
    },
    {
        "name": "Kim Kardashian",
        "follower_count": 360_000_000,
        "description": "Media Personality",
        "country": "United States",
        "gender": "Female"
    },
    {
        "name": "Khloé Kardashian",
        "follower_count": 306_000_000,
        "description": "Media Personality",
        "country": "United States",
        "gender": "Female"
    },
    {
        "name": "Neymar Jr",
        "follower_count": 231_000_000,
        "description": "Footballer",
        "country": "Brazil",
        "gender": "Male"
    },
    {
        "name": "Taylor Swift",
        "follower_count": 281_000_000,
        "description": "Singer",
        "country": "United States",
        "gender": "Female"
    }
]

import random

person1 = random.choice(data)
person2 = random.choice(data)
chances = 5
score = 0
while True :
    if chances > 0 :

        print(f"Compare A: {person1['name']}, a {person1['description']}, from {person1['country']}.")
        print("VS")
        print(f"Compare B: {person2['name']}, a {person2['description']}, from {person2['country']}.")
        
        guess = input("Who has more followers? Type 'A' or 'B': ").upper()
        
        if person1['follower_count'] > person2['follower_count']:
            correct_answer = 'A'
        else:
            correct_answer = 'B'
        
        if guess == correct_answer:
            chances -= 1
            print(f"You're right! Current Chances: {chances}. \n")
            score += 1
            person1 = random.choice(data)
            person2 = random.choice(data)
        else:
            chances -= 1
            print(f"Sorry, that's wrong. Current Chances: {chances}. \n")

    else:
        print(f"Game over! Your final score is: {score}.")
        break