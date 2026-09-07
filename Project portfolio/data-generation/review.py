import pandas as pd 
import numpy as np  

np.random.seed (45)

total_reviews = 500

review_id = [f'REV_{i:05d}' for i in range (1, total_reviews + 1)]
raw_product = np.random.randint(1, 51, size = total_reviews)
product_id = [f"PROD_{i:03d}" for i in raw_product]
ratings = np.random.choice([1,2,3,4,5], size = total_reviews, 
                           p = [0.05, 0.05, 0.10, 0.30, 0.50])

motivations = [
    "I bought this for an upcoming trip.",
    "Needed a replacement for my old one.",
    "Saw an ad and decided to treat myself.",
    "Got this as a gift.",
    "Been looking for something like this for weeks."
]

anxieties_resolved = [
    "I was worried about the sizing, but it fits perfectly.",
    "Hesitant about the material, but it feels premium.",
    "Thought it might arrive late, but shipping was fast.",
    "Wasn't sure if it would match the photos, but it looks exactly the same."
]

anxieties_realized = [
    "I was worried about the sizing, and unfortunately it runs way too small.",
    "Hesitant about the material, and it does feel a bit cheap.",
    "Thought it might arrive late, and it actually got delayed by a week.",
    "Wasn't sure if it would match the photos, and the color is definitely off."
]

values_positive = [
    "Absolutely worth the money.",
    "Highly recommend it to anyone.",
    "Great value for the price.",
    "Exceeded my expectations."
]

values_negative = [
    "Not worth the price tag.",
    "I'll be returning it.",
    "Very disappointed overall.",
    "Wouldn't recommend wasting your money."
]

review_texts = []
for star in ratings:
    mot = np.random.choice(motivations)
    if star >= 4:
        anx = np.random.choice(anxieties_resolved)
        val = np.random.choice(values_positive)
    elif star <= 2:
        anx = np.random.choice(anxieties_realized)
        val = np.random.choice(values_negative)
    else:
        anx = np.random.choice(anxieties_resolved) if np.random.rand() > 0.5 else np.random.choice(anxieties_realized)
        # 1. FIXED: Indented to only apply to 3-star reviews
        val = "It's just okay, nothing special." 

    review_texts.append(f"{mot} {anx} {val}")

# 2. FIXED: Unindented so the DataFrame is built only once, after the loop finishes
reviews_df = pd.DataFrame({
    'review_id': review_id,
    'product_id': product_id,
    'review_texts': review_texts,
    'ratings' : ratings
})

print(reviews_df.head(10))