<h3> Movie recommendation based on user's query.</h3>

<h4> Recommend users movie based on their query. </h4>

  <h5> Implementation and componentt details: </h5>

  > Load the movies dataset: load_data.py 

  > Get features vectors using tf-idf: tfidf_matrix.py

  > Calculating cosine similarities: similarity_score.py 

  > Recommending movies: recommendations.py 

  <h4> Steps to run the repo </h4>

- git clone

<h5>1. pipenv setup </h5>

 - Install dependencies: pipenv install --skip-lock

<h5>2. Dataset </h5>
  - Get the dataset from the link https://drive.google.com/file/d/1nuGxtaz5pPuChyPTj3O34XhnMD2vscVd/view?usp=sharing
  
  - save it in a dataset folder  

<h5>4. To run the code </h5>
  - python app.py

<h4>Output: </h4>
Top 10 recommendation of the movies based on the title provided by the user.