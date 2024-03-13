import requests
import random
import matplotlib.pyplot as plt
import os

TMDB_API_KEY = 'REPLACE_With YOUR API_KEY'


def get_movie_recommendations(genre):
    
    base_url = 'https://api.themoviedb.org/3'
    discover_url = f'{base_url}/discover/movie'
    params = {
        'api_key': TMDB_API_KEY,
        'language': 'en-US',
        'sort_by': 'popularity.desc',  # Sort by popularity
        'include_adult': 'false',
        'with_genres': get_genre_id(genre),
    }

    response = requests.get(discover_url, params=params)
    if response.status_code == 200:
        data = response.json()
        recommendations = [movie['title'] for movie in data['results']]
        return recommendations[:10]  # Return the top 5 recommendations
    else:
        print("Error fetching recommendations from TMDb.")
        return []


def get_genre_id(genre):
    genre_mapping = {
        'romantic': 10749,
        'horror': 27,
        'drama': 18,
        'comedy': 35,
    }
    return genre_mapping.get(genre, 18)  # Default to 'Drama' if genre not found

# Function to generate random viewing counts for movie recommendations (mockup)
def generate_viewing_counts(recommendations):
    viewing_counts = {movie: random.randint(1, 100) for movie in recommendations}
    return viewing_counts

# Function to create a pie chart of movie viewing counts
def create_pie_chart(viewing_counts):
    labels = viewing_counts.keys()
    counts = viewing_counts.values()
    
    plt.figure(figsize=(12, 5))
    plt.subplot(121)
    plt.pie(counts, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title("Movie Viewing Counts (Pie Chart)")

# Function to create a bar graph of movie viewing counts
def create_bar_graph(viewing_counts):
    movie_titles = list(viewing_counts.keys())
    counts = list(viewing_counts.values())
    
    plt.subplot(122)
    plt.barh(movie_titles, counts)
    plt.xlabel('Viewing Counts')
    plt.ylabel('Movie Titles')
    plt.title("Movie Viewing Counts (Bar Graph)")

# Main function
def main():
    print("Movie Recommendation System")
    print("Genres: Romantic, Horror, Drama, Comedy")
    user_genre = input("Enter your preferred genre: ").strip().lower()

    if user_genre in ["romantic", "horror", "drama", "comedy"]:
        recommendations = get_movie_recommendations(user_genre)
        if recommendations:
            print(f"Here are some {user_genre} movie recommendations:")
            for i, recommendation in enumerate(recommendations, start=1):
                print(f"{i}. {recommendation}")

            viewing_counts = generate_viewing_counts(recommendations)

            create_pie_chart(viewing_counts)
            create_bar_graph(viewing_counts)

            # Ask the user for their name
            user_name = input("Enter your name: ").strip()

            # Create the "images" directory if it doesn't exist
            image_directory = "images"
            if not os.path.exists(image_directory):
                os.makedirs(image_directory)

            # Save the pie chart and bar graph as image files in the "images" directory
            filename = f"{user_name}_pie_chart_Bar_graph.png"
            file_path = os.path.join(image_directory, filename)
            plt.savefig(file_path)

            plt.tight_layout()
            plt.show()

            print(f"Visualizations saved in the 'images' directory as {filename}")
        else:
            print("No recommendations found.")
    else:
        print("Invalid genre. Please select from the given options.")

if __name__ == "__main__":
    main()
