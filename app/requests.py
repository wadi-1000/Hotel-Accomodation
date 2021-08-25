import urllib.request,json

from .models import ExerciseInfo

exrcise_base_url = None

def cofigure_request(app):
    global exrcise_base_url
    exrcise_base_url = app.config["EXERCISE_API_BASE_URL"]

def get_exercises():
    '''
    Function that gets json response to our url request
    '''
    get_exercises_url = exrcise_base_url
    with urllib.request.urlopen(get_exercises_url) as url:
        get_exercises_data = url.read()
        get_exercises_response = json.loads(get_exercises_data)
     
        exercise_results = None

        if get_exercises_response['results']:
            exercise_results_list = get_exercises_response['results']
            exercise_results = process_exercises(exercise_results_list)

    return exercise_results
        


