import yaml

from movie_recommendation import (
    Recommendation,
    cosine_similarity,
    get_tfidf_matrix,
    loadCsv,
)

with open("config.yaml", "r") as stream:
    file_paths = yaml.safe_load(stream)


def main():

    recommendation = Recommendation(file_paths["csv_loc"])
    print(recommendation.get_recommendations("A thriller movie that is fun."))


main()
