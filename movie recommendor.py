import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Step 1: Movie Data
movies = {
    'Title': [
        'The Matrix', 'Inception', 'Interstellar', 'The Dark Knight',
        'Avengers: Endgame', 'Titanic', 'The Godfather', 'Forrest Gump',
        'Joker', 'Iron Man'
    ],
    'Genre': [
        'sci-fi action',
        'sci-fi thriller',
        'sci-fi space drama',
        'superhero action',
        'superhero sci-fi action',
        'romance drama',
        'crime mafia drama',
        'biography drama',
        'thriller drama',
        'sci-fi action'
    ]
}

df = pd.DataFrame(movies)

# Step 2: Vectorize Genres
tfidf = TfidfVectorizer()
tfidf_matrix = tfidf.fit_transform(df['Genre'])

# Step 3: Similarity Score
cosine_sim = cosine_similarity(tfidf_matrix)

# Step 4: Recommendation Function
def recommend(title):
    title = title.lower()
    titles_lower = df['Title'].str.lower()

    if title not in titles_lower.values:
        print("❌ Movie not found. Try another title.")
        return

    index = titles_lower[titles_lower == title].index[0]
    sim_scores = list(enumerate(cosine_sim[index]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:6]

    print(f"\n🎬 Because you liked '{df.iloc[index]['Title']}', you may also like:\n")
    for i, _ in sim_scores:
        print("👉", df.iloc[i]['Title'])

# Step 5: Main
if __name__ == "__main__":
    print("🎥 Movie Recommendation System")
    print("Type a movie name (e.g., Inception, Joker, Iron Man)")
    print("Type 'exit' to stop.\n")

    while True:
        query = input("Enter movie name: ").strip()
        if query.lower() == 'exit':
            print("👋 Thank you for using MovieBot!")
            break
        recommend(query)
