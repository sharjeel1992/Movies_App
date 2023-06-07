from movie_app import MovieApp
from storage_csv import StorageCsv
from storage_json import StorageJson

storage1 = StorageJson('data.json')
storage2 = StorageCsv('data.csv')


def main():
    movie_app = MovieApp(storage2)
    movie_app.run()


if __name__ == "__main__":
    main()
