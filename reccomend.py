titles = [
    'The Matrix', 'John Wick', 'Inception',
    'The Notebook', 'Titanic', 'Interstellar'
]

descriptions = [
    'A hacker discovers reality is a simulation',
    'A retired hitman seeks vengeance',
    'A thief steals secrets through dream sharing',
    'A romantic story set in the 1940s',
    'A love story on the ill fated Titanic',
    'Explorers travel through a wormhole in space'
]

def compute_similarity(desc1, desc2):
    words1 = set(desc1.lower().split())
    words2 = set(desc2.lower().split())
    return len(words1 & words2)  

def recommend(movie_title, num_recommendations=3):
    if movie_title not in titles:
        print(f" Movie '{movie_title}' not found.")
        return

    idx = titles.index(movie_title)
    target_desc = descriptions[idx]

    scores = []
    for i, desc in enumerate(descriptions):
        if i == idx:
            continue
        similarity = compute_similarity(target_desc, desc)
        scores.append((i, similarity))

    scores.sort(key=lambda x: x[1], reverse=True)

    print(f"\n Recommended movies similar to '{movie_title}':")
    for i, score in scores[:num_recommendations]:
        print(f" - {titles[i]}")

recommend("Inception")
