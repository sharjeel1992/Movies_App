from istorage import IStorage
import csv


class StorageCsv(IStorage):
    """
    This class will implement our abstract methods and process only csv type data
    """
    def __init__(self, file_path):
        self.file_path = file_path

    def list_movies(self):
        """
        This function opens the csv file,appends it to dictionary and return the dictionary as required
        in abstract method
        """
        movies_dict = {}
        with open(self.file_path, "r") as file:
            reader = csv.reader(file)
            next(reader)
            for names in reader:
                movies_dict.update(({names[0]: {"Rating": float(names[1]), "Year": int(names[2]),
                                                "Poster Image URL": names[3]}}))
            return movies_dict

    def add_movie(self, title, year, rating, poster):
        """
        This function will add a new row to our current csv file based on values passed
        """
        add_row = [title, rating, year, poster]
        with open(self.file_path, "a") as file:
            writer = csv.writer(file)
            writer.writerow(add_row)
            print(f"{title} successfully added to csv database")

    def delete_movie(self, title):
        """
         This function will first read the file and will write to csv file,making sure that the value
         passed is deleted from our csv file
         """
        with open(self.file_path, "r") as file:
            reader = csv.reader(file)
            rows = list(reader)
        with open(self.file_path, "w", newline='') as file:
            writer = csv.writer(file)
            for column in rows:
                if column[0] != title:
                    writer.writerow(column)

    def update_movie(self, title, notes):
        """
        This function will read the csv file and will change the value based on the title of
        the movie and new rating.
        """
        with open(self.file_path, 'r') as file:
            reader = csv.DictReader(file)
            rows = list(reader)
        for row in rows:
            if row['title'] == title:
                row['Rating'] = str(notes)
        with open(self.file_path, 'w') as file:
            fieldnames = ['title', 'Rating', 'Year', 'Poster Image URL']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(rows)
