from abc import ABC, abstractmethod


class IStorage(ABC):
    """
    This is our abstract method for the list of the movies
    """
    @abstractmethod
    def list_movies(self):
        """
        Returns a dictionary of dictionaries that
        contains the movie information in the database.
        """
        pass

    @abstractmethod
    def add_movie(self, title, year, rating, poster):
        """
        Must get arguments from an API source and update the file passed as an object
        """
        pass

    @abstractmethod
    def delete_movie(self, title):
        """
        Must take a title as user input and look into the database for the title and delete
        the title with its values
        """
        pass

    @abstractmethod
    def update_movie(self, title, notes):
        """
        Must look for the title in the database and update the rating as provided by the user
        """
        pass
