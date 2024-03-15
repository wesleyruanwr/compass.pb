import json
import boto3
import requests
from datetime import datetime

def lambda_handler(event, context):
    
    cod_genre = 27, 53
    api_tmdb_key = '' 
    url_tmdb = f"https://api.themoviedb.org/3/discover/movie?api_key={api_tmdb_key}&with_genres={cod_genre}"
    
    bucket_name = "desafiowr"
    date = datetime.now().strftime('%Y/%m/%d')
    hours = datetime.now().strftime('%H%M%S')
    aws_file_key = f"Raw/tmdb/json/{date}/data_{cod_genre}-{hours}.json"

    response = requests.get(url_tmdb)
    data_tmdb = response.json()
    json_data_tmdb = json.dumps(data_tmdb, indent=4)
    
    s3 = boto3.resource('s3', 
                            aws_access_key_id = '',
                            aws_secret_access_key = '',
                            aws_session_token = '')
    
    if response.status_code == 200:
        print('arquivo enviado')
        s3.Object(bucket_name, aws_file_key).put(Body=json_data_tmdb)
    
    else:
        print('Falha!', response.status_code)