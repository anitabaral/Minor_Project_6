from sklearn.feature_extraction.text import TfidfVectorizer


def get_tfidf_matrix(metadata):
    """
    Constructs the tf-idf matrix on the metadata.

      Parameters:
        metadata (object): The data whose tf-idf matrix is to be calculated

      Returns:
        tfidf_matrix (): The matrix which represents the metada

    """

    tfidf = TfidfVectorizer(stop_words="english")
    metadata["overview"] = metadata["overview"].fillna("")
    tfidf_matrix = tfidf.fit_transform(metadata["overview"])

    return tfidf_matrix
