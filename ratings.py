"""Restaurant rating lister."""


# put your code here
def read_ratings():

    ratings_txt = open('scores.txt')

    ratings = {}
    
    for line in ratings_txt:
        line = line.rstrip()
        restaurant, rating = line.split(':')
        ratings[restaurant] = int(rating)

    return ratings


def print_sorted_ratings(ratings):

    for restaurant, rating in sorted(ratings.items()):
        print(f'{restaurant} is rated at {rating}')

def add_restaurant(ratings):

    print("\nInput a rating for a new restaurant")
    restaurant = input('Restaurant name: ')
    rating = input('Rating: ')

    ratings[restaurant] = int(rating)

ratings = read_ratings()

add_restaurant(ratings)

print_sorted_ratings(ratings)
