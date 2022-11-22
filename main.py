MENU_PROMPT = "Enter 'a' to add a movie, 'l' to see your movies, 'f' to find your movies by title and 'q' to quit:"
movies = []



def add_movie():
    title = input("Enter the movie title:")
    director = input("Enter the movie director:")
    year = input("Enter the movie year:")

    movies.append({
        "title": title,
        "director": director,
        "year": year
    })


def show_movies():
    for movie in movies:
        print(movie)


def print_movies(movie):
    print(f"Title: {movie['title']}")
    print(f"Director: {movie['director']}")
    print(f"Year: {movie['year']}")


def find_movies():
    search = input("Enter the movie title you are looking for:")

    for movie in movies:
        if movie["title"] == search:
            print_movies(movie)


user_options = {
    "a": add_movie,
    "l": show_movies,
    "f": find_movies
}


def menu():
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection in user_options:
            selected_function = user_options[selection]
            selected_function()
        else:
            print('Unknown command. Please try again.')

        selection = input(MENU_PROMPT)


menu()
