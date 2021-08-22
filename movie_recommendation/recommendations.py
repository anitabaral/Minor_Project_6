import pandas as pd

from .load_data import loadCsv
from .tfidf_matrix import get_tfidf_matrix
from .similarity_score import cosine_similarity


class Recommendation:
    def __init__(self, file_path):

        self.file_paths = file_path
        self.metadata = loadCsv(self.file_paths)

    def title_to_index(self):
        """
        Construct a reverse map of indices and moview titles

          Parameters:
            metadata (object): Dataframe of the movie dataset.

          Returns:
            indices (): Series having title as index and index  as the data of the series
        """

        indices = pd.Series(
            self.metadata.index, index=self.metadata["title"]
        ).drop_duplicates()

        return indices

    def get_recommendations(self, title):
        """
        Does the recommendation based of movies

        Parameters:
          title (str): Title of the movie like which other movies is to be recommended.

        Returns ():
          top_ranked_movies (): The titles corresponding to the indices of the top elements
        """

        indices = self.title_to_index()
        tfidf_matrix = get_tfidf_matrix(self.metadata)
        cosine_sim = cosine_similarity(tfidf_matrix)
        index = indices[title]
        sim_scores = list(enumerate(cosine_sim[idx]))
        sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
        sim_scores = sim_scores[1:11]
        movie_indices = [sim_score[0] for sim_score in sim_scores]
        top_ranked_movies = self.metadata["title"].iloc[movie_indices]

        return top_ranked_movies
