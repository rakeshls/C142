from flask import Flask,jsonify,request
import csv
from Demographic import output
from concentBased import get_recommendations
all_movies = []

with open('final.csv',encoding='utf8') as f:
    reader = csv.reader(f)
    data = list(reader)
    all_movies = data[1:]


liked_movies = []
unliked_movies = []
didNot_watch = []

app = Flask(__name__)

@app.route('/get-Movie')
def get_Movie():
    movie_data={
        "title": all_movies[0][19],
        "poster_link":all_movies[0][27],
        "release_date": all_movies[0][13],
        "duration": all_movies[0][15],
        "rating":all_movies[0][20],
        "overview":all_movies[0][9]
    }
    return jsonify({
        'data':movie_data,
        'status':'succes'
    })

@app.route('/liked-Movie',methods=['POST'])
def liked_Movie():
    movie=all_movies = [0]
    movie = all_movies[0]
    all_movies = all_movies[1:]
    liked_movies.append(movie)
    all_movies.pop(0)
    return jsonify({
        'status':'succes'
    }),201 

@app.route('/unliked-Movie',methods=['POST'])
def unliked_Movie():
    all_movies = [0]
    movie = all_movies[0]
    all_movies = all_movies[1:]
    unliked_movies.append(movie)
    all_movies.pop(0)
    return jsonify({
        'status':'succes'
    }),201

@app.route('/notWatched-Movie',methods=['POST'])
def notWatched_Movie():
    all_movies = [0]
    movie = all_movies[0]
    all_movies = all_movies[1:]
    didNot_watch.append(movie)
    all_movies.pop(0)
    return jsonify({
        'status':'succes'
    }),201

@app.route('/popular-Movie')
def popular_Movie():
    movie_data = []
    for movie in output:
        d = {
            "title":movie[0],
            "poster": movie[1],
            "release_date":movie[2],
            "duration":movie[3],
            "rating":movie[4],
            "overview":movie[5]
        }
        movie_data.append(d)
    return jsonify({
        "data": movie_data,
        "status":"succes"
    }),200
@app.route('/recommended-Movie')
def recommended_Movie():
    r = []
    for like_movie in liked_movies:
        output = get_recommendations(like_movie[19])
        for data in output:
            r.append(data)
        
    import itertools
    r.sort()
    r= list(r for r,_ in itertools.groupby(r))
    movie_data=[]
    for recommended in r:
        d={
            "title":recommended[1],
            "poster_link":recommended[2],
            "releaseDate":recommended[3],
            "duration":recommended[4],
            "rating":recommended[5],
            "overview":recommended[6] 
       }
    movie_data.append(d)
    return jsonify({
        "data": movie_data,
        "status":"succes"
    }),200

if __name__ == '__main__':
    app.run()