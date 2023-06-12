import requests
import statistics
import random


class MovieApp:
    """
    This class will fetch data and do all the actions regeadless of the fact what type of
    data we are working on.In our case its json and csv
    """
    API = 'http://www.omdbapi.com/?apikey=c61fc86&t='

    def __init__(self, storage):
        self._storage = storage

    def _command_list_movies(self):
        """
         This is a private function.It takes list of movies from storage_json class and prints
         name year and rating on the terminal
         """
        movies = self._storage.list_movies()
        for title in movies:
            print(f"{title} {movies[title]['Year']} {movies[title]['Rating']}")

    def _command_movie_add(self):
        """This is a private function.it's going to use api to get desired data and add that
        to our json file."""
        movies = self._storage.list_movies()
        try:
            movie_title = input("Enter new movie name: ")
            fetch_data = requests.get(self.API + movie_title)
            access_data = fetch_data.json()
            if movie_title in movies:
                print(f"movie {movie_title} already exist")
            else:
                title = access_data["Title"]
                year = access_data["Year"]
                rating = access_data["imdbRating"]
                poster = access_data["Poster"]
                self._storage.add_movie(title, year, rating, poster)
        except KeyError:
            print(f"movie not in database")

    def _command_movie_delete(self):
        """
        This is a private function.It will look for movies in the list and delete the
         movie based on user input. If the movie does not exist, it will inform user as well
         """
        movies = self._storage.list_movies()
        movie_name = input("Enter movie name to delete: ")
        for name in movies:
            if name == movie_name:
                self._storage.delete_movie(movie_name)
                print(f"{movie_name} successfully deleted")
                break
        else:
            print(f"{movie_name} does not exist")

    def _command_update_rating(self):
        """
         THis is a private function.It's going to ask user to give the name of the movie, and if movie exists,
         it will ask user to provide updated rating and will update rating in our json file
         """
        movies = self._storage.list_movies()
        movie_name = input("Enter movie name:")
        for name in movies:
            if movie_name in name:
                update_rating = float(input("Enter new rating:"))
                self._storage.update_movie(movie_name, update_rating)
                print(f"movie {movie_name} successfully updated")
                break
        else:
            print(f"movie {movie_name} doesn't exist")

    def _command_movie_stats(self):
        """
        This is a private function.It will show user the stats of our json file on terminal
        """
        movies = self._storage.list_movies()
        rating_list = []
        for names in movies:
            rating_list.append(movies[names]["Rating"])
        average_rating = (sum(rating_list) / len(movies))
        median_rating = statistics.median(rating_list)
        print(f"Average rating: {average_rating}")
        print(f"Median rating: {median_rating}")
        print(f"Best movie rating: {max(rating_list)}")
        print(f"Worst movie rating:{min(rating_list)}")

    def _command_search_movie(self):
        """
        This is a private function.It will search for the movie based on user input
        """
        movies = self._storage.list_movies()
        movie_search = input("Enter part of movie name:")
        for key, val in movies.items():
            if movie_search.lower() in key.lower():
                print(key, val["Rating"], val["Year"])
            else:
                print("No movie found")

    def _command_rating_sorted(self):
        """
        This is a private function.It will sort the movies on ratings
        and print them on terminal
        """
        movies = self._storage.list_movies()
        sorted_dict = sorted(movies.items(), key=lambda x: x[1]['Rating'], reverse=True)
        for names in sorted_dict:
            print(names[0], names[1]["Rating"])

    def _random_movie(self):
        """
        This function will choose a random movie from the movie list
        """
        movies = self._storage.list_movies()
        random_movie = random.choice(list(movies.keys()))
        print(f"Random movie: {random_movie}")

    def _generate_website(self):
        """
            This function takes data stored in json file and convert the data
           to html format
        """
        movies = self._storage.list_movies()
        func_output = ''
        for name in movies:
            func_output += '<li>'
            func_output += '<div class="movie">'
            func_output += f'<img class="movie-poster" src= "{movies[name]["Poster Image URL"]}">'
            func_output += f'<div class="movie-title">{name}</div>'
            func_output += f'<div class="movie-year">{movies[name]["Year"]}</div>'
            func_output += f'<div class="movie-year">{movies[name]["Rating"]}</div>'
            func_output += '</div>'
            func_output += '</li>'
        return func_output

    def run(self):
        """
        This function will print list for the user to choose from and based on user input
        and using while loop it will keep asking user for input and will do required actions,
        until user chooses to quit.Exception thrown for non integeral values
        """
        print("\n** ** ** ** ** My Movies Database ** ** ** ** **")
        while True:
            print("""\nMenu:
0.Exit
1.List movies
2.Add movie
3.Delete movie
4.Update movie
5.Stats
6.Search movie
7.Movie sorted by rating
8.Random movie
9.Generate Website\n""")
            try:
                user_choice = int(input("Enter choice (0-9): "))
                if user_choice == 0:
                    print("BYE!")
                    break
                elif user_choice == 1:
                    self._command_list_movies()
                elif user_choice == 2:
                    self._command_movie_add()
                elif user_choice == 3:
                    self._command_movie_delete()
                elif user_choice == 4:
                    self._command_update_rating()
                elif user_choice == 5:
                    self._command_movie_stats()
                elif user_choice == 6:
                    self._command_search_movie()
                elif user_choice == 7:
                    self._command_rating_sorted()
                elif user_choice == 8:
                    self._random_movie()
                elif user_choice == 9:
                    with open("index_template.html", "r") as html_template:
                        file_reader = html_template.read()
                        desired_output = file_reader.replace("__TEMPLATE_MOVIE_GRID__", self._generate_website())

                    with open("my_movies.html", "w") as html_file:
                        html_file.write(desired_output)

                    break
                else:
                    print("Invalid choice")
            except ValueError:
                print("Please enter numeric values from the menu")
