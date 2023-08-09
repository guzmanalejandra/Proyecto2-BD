import requests
import json
import databaseQuerys as dbQ
listaPeliculas = ['matrix','indiana+jones','transformers','seven','megamind',
                  'metal+lords','avatar','after+we+fell','encanto','hulk',
                  'shazam','harry+potter','pixels','Big+mouth','baki',
                  'morbius','turning+red','uncharted','fantastic+four','gravity',
                  'war+room','courageous','joker','tenet','top+gun',
                  'aquaman','jurassic+world','charlatan','the+fallout','jexi',
                  'pitch+perfect','five+feet+apart','passengers','eternals','ghost+rider',
                  'black+panther','la+la+land','dune','jungle+cruise','red+notice',
                  'caroline','1917','dunkirk','fury','wonder+woman',
                  'the+wolverine','black+widow','justice+league','the+iron+giant','nobody']
def getMovies():
    responses = []
    for i in range(len(listaPeliculas)):

        url = f"http://www.omdbapi.com/?apikey=482161e2&t={listaPeliculas[i]}"



        response = requests.request("GET", url)
        data = json.loads(response.text)
        dbQ.saveMovie(data['Released'],data['Director'],data['Awards'],data['Title'],data['imdbID'],data['Poster'])
        # responses.append(response.text)


def saveActors():
    
    responses = []
    for i in range(len(listaPeliculas)):

        url = f"http://www.omdbapi.com/?apikey=482161e2&t={listaPeliculas[i]}"



        response = requests.request("GET", url)
        data = json.loads(response.text)
        actores = data['Actors']
        listaA = actores.split(', ')
        if "Lupita Nyong'o" in listaA:
            listaA.remove("Lupita Nyong'o")
            listaA.append("Lupita Nyong o")
        id = data['imdbID']
        dbQ.saveActors(listaA, id)




getMovies()
saveActors()