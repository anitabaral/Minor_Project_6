from pathlib import Path

import dask.dataframe as pd

def loadCsv(path):
    """
    Loads the csv file specified in the path and reads it as a dataframe.

        Parameters:
          path (str): Path of the csv file.

        Returns:
          metadata (object): The dataframe of the of the csv file.

    """

    csv_path = Path(path)
    if csv_path.exists():
        metadata = pd.read_csv(csv_path, dtype={'budget': 'object',
       'id': 'object',
       'popularity': 'object',
       'revenue': 'float64',
       'vote_count': 'float64'})
    else:
        raise ValueError("Error while reading the csv file.")

    return metadata
