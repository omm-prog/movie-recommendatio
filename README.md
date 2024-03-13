# Movie Recommendation System

This is a Python script that provides movie recommendations based on user's preferred genre and generates visualizations of viewing counts for the recommended movies.

## Prerequisites

Before running the script, you need to obtain an API key from [The Movie Database (TMDB)](https://www.themoviedb.org/documentation/api) to access movie data. Once you have your API key, replace the placeholder `'REPLACE_With YOUR API_KEY'` in the script with your actual API key.

You also need to have Python installed on your system along with the following libraries:

- requests
- matplotlib

You can install these libraries using pip:

pip install requests matplotlib


## Usage

1. Run the script by executing the Python file `movie_recommendations.py`.
2. You will be prompted to enter your preferred genre (Options: Romantic, Horror, Drama, Comedy).
3. After entering your preferred genre, the script fetches movie recommendations and displays them along with their viewing counts.
4. It generates visualizations (pie chart and bar graph) showing the viewing counts of the recommended movies.
5. You will be asked to enter your name.
6. The visualizations are saved as image files in the 'images' directory.

Insert ![Screenshot 2024-03-14 023811](https://github.com/omm-prog/movie-recommendatio/assets/161586309/bb3ffd94-20d0-484a-9dd4-b06b6f639469)

![Screenshot 2024-03-14 023834](https://github.com/omm-prog/movie-recommendatio/assets/161586309/8520dbc2-d72b-4351-a2ca-db9b3ff61c67)

![Screenshot 2024-03-14 023855](https://github.com/omm-prog/movie-recommendatio/assets/161586309/3431e49c-49ef-497b-a31f-9dbac1678809)


## Directory Structure

- movie_recommendations.py
- images/
  - [user_name]_pie_chart_Bar_graph.png
 
## Usage Rights

Feel free to use and modify this script for your own purposes. You are welcome to adapt it to suit your needs or integrate it into your projects. If you find it helpful, consider giving credit or a mention, but it's not required.






## Note

- If the 'images' directory doesn't exist, the script will create it before saving the visualizations.
- The script uses mockup data for generating viewing counts.
- Make sure to replace the placeholder API key with your actual TMDB API key before running the script.
