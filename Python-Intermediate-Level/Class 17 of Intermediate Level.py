#Movie Application
'''print("Welcome to Movie Info App\nTo use this app, enter information for a movie.")
print("Enter information of the movie below:")
class Movie:
    def __init__(self,name,language,release_date,user_opinion_of_movie):
        self.name=name
        self.language=language
        self.release_date=release_date
        self.user_opinion_of_movie=user_opinion_of_movie
    def display(self):
        print(f"Movie name: {self.name}")
        print(f"Movie language: {self.language}")
        print(f"Movie release date: {self.release_date}")
        print(f"Your opinion of the movie: {self.user_opinion_of_movie}")
        print()

user_inputed_movie=[]
while True:
    name=input("Enter the movie name here: ")
    language=input("Enter the language of the movie here: ")
    release_date=input("Enter the movie release date here: ")
    user_opinion_of_movie=input("Enter you opinion of the movie here: ")
    ob=Movie(name,language,release_date,user_opinion_of_movie)
    user_inputed_movie.append(ob)
    continue_exit=input("Do you wish to continue the app? If so, then enter 'c' below. If you want to exit the app, enter 'e' below.\n")
    if continue_exit=="e":
        print("The app has been closed.")
        break

for i in user_inputed_movie:
    print("Here is your information:\n")
    i.display()'''
#Set and List Typecast
'''s="Mammoth"
print(f"List: {list(s)}")
print(f"Set: {set(s)}")'''
#Union, Difference, and Intersection with Sets

#Union
'''set1={1,4,1,3,5}
set2={2,3,3,5,6}
print(f"Set 1: {set1}")
print(f"Set 2: {set2}")
print(f"Union of Set 1 and Set 2: {set1.union(set2)}")'''

#Difference
'''set1={1,4,1,3,5}
set2={2,3,3,5,6}
print(f"Set 1: {set1}")
print(f"Set 2: {set2}")
print(f"Difference of Set 1 to Set 2: {set1.difference(set2)}")
print(f"Difference of Set 2 to Set 1: {set2.difference(set1)}")'''

#Intersection
'''set1={1,4,1,3,5}
set2={2,3,3,5,6}
print(f"Set 1: {set1}")
print(f"Set 2: {set2}")
print(f"Intersection of Set 1 and Set 2: {set1.intersection(set2)}")'''