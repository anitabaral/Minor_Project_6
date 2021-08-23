import yaml

from movie_recommendation import (
    Recommendation,
    cosine_similarity,
    get_tfidf_matrix,
    loadCsv,
)

with open("config.yaml", "r") as stream:
    file_paths = yaml.safe_load(stream)


if __name__ == "__main__":

    recommendation = Recommendation(file_paths["csv_loc"])
    query = input ('Enter your query: ')
    print(recommendation.get_recommendations(query))


