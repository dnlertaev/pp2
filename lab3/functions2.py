#1
def is_highly_rated(movie):
    
    return movie["imdb"] > 5.5



#2
def get_highly_rated_movies(movies):
    
    return [movie for movie in movies if is_highly_rated(movie)]



#3
def get_movies_by_category(movies, category):
    
    return [movie for movie in movies if movie["category"] == category]



#4
def average_imdb_score(movies):
    
    if not movies:
        
        return 0
    
    total_score = sum(movie["imdb"] for movie in movies)
    
    return total_score / len(movies)



#5
def average_imdb_score_by_category(movies, category):
    
    category_movies = get_movies_by_category(movies, category)
    
    return average_imdb_score(category_movies)

