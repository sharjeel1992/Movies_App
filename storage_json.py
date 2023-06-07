from Movies_App.istorage import IStorage
import json


class StorageJson(IStorage):
    def __init__(self, file_path):
        self.file_path = file_path
        open_data = open(self.file_path)
        self.file_path = json.load(open_data)

    def list_movies(self):
        """This function iterates through json file and return the name,rating and year of all the
          movies in the file
          """
        return self.file_path

    def add_movie(self, title, year, rating, poster):
        """
        This function takes four arguments and adds them to json data file
        """
        self.file_path.update({title: {"Rating": float(rating),
                                       "Year": year,
                                       "Poster Image URL": poster}})
        with open("data.json", "w") as update_file:
            json.dump(self.file_path, update_file, indent=4)
            print(f"{title} successfully added to database")

    def delete_movie(self, title):
        """
        This function will delete the movie based on argument passed to it and
        will update the json file
        """
        self.file_path.pop(title)
        with open("data.json", "w") as update_file:
            json.dump(self.file_path, update_file, indent=4)

    def update_movie(self, title, notes):
        """
         This function takes two arguments one as title of the movie and rating that
         need be updated and then updates the json file
         """
        self.file_path[title]["Rating"] = float(notes)
        with open("data.json", "w") as update_file:
            json.dump(self.file_path, update_file, indent=4)

