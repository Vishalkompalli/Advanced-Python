# The Dictionary Look-up

movies = {"Inception": 2010, "The Matrix": 1999, "Interstellar": 2014}
movies_lower = {key.lower(): value for key, value in movies.items()} #Dictionary Comprehension technique

while True:
    movie_name = input("Enter a movie name: ").lower()
    # movie_name_lower = movie_name.lower()

    try:
        result = movies_lower[movie_name]        

    except:
        KeyError
        print("No such movie exists in my data you dumbass, enter a valid one.")

    else:
        print(f"{movie_name.title()} was released in",movies_lower[movie_name])
        exit()

    finally:
        pass