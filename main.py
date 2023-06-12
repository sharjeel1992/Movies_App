from movie_app import MovieApp
from storage_csv import StorageCsv
from storage_json import StorageJson


def main():
    """
    This is our main function.Two object variables created to store two different types
    of data.We will pass on whatever data we want to work
    """
    storage1 = StorageJson('data.json')
    storage2 = StorageCsv('data.csv')

    movie_app = MovieApp(storage2)
    movie_app.run()


if __name__ == "__main__":
    main()
