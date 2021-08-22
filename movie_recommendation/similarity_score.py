from sklearn.metrics.pairwise import linear_kernel


def cosine_similarity(tfidf_matrix):
    """
    Calculates the cosine similarity between different movie overview

      Parameters:
        tfidf_matrix (): The matrix which represents the overview of metadata

      Returns:
        cosine_sim (): Matrix which consists of cosine similarity of each movie overview with every other movie overfiew.

    """
    cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

    return cosine_sim
