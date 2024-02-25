import json
import boto3
import requests
from datetime import datetime

def lambda_handler(event, context):
    
    cod_genre = 27, 53
    api_tmdb_key = '67f395bf0688fde6e615e6e8f44cb97a' 
    url_tmdb = f"https://api.themoviedb.org/3/discover/movie?api_key={api_tmdb_key}&with_genres={cod_genre}"
    
    bucket_name = "desafiowr"
    date = datetime.now().strftime('%Y/%m/%d')
    hours = datetime.now().strftime('%H%M%S')
    aws_file_key = f"Raw/tmdb/json/{date}/data_{cod_genre}-{hours}.json"

    response = requests.get(url_tmdb)
    data_tmdb = response.json()
    json_data_tmdb = json.dumps(data_tmdb, indent=4)
    
    s3_resource = boto3.resource('s3', 
                            aws_access_key_id = 'ASIAX4IGHEAE63YFQ5XJ',
                            aws_secret_access_key = 'uEoTYcfHT6F5xzjBHd75HGUMVEF+g1tmT+Q6VUiN',
                            aws_session_token = 'IQoJb3JpZ2luX2VjELP//////////wEaCXVzLWVhc3QtMSJHMEUCIQDQvOBF2PJg9NY7ZlNauoWqZ5aB4ab2PXVFyDSMr+rYKgIgHlUv2KO4yy3lnsoimUR7Bi1oUKezm1asvQ7xFylhPloqpAMInP//////////ARAAGgw1NDE3MTU4MDAwNzMiDPEpwhECIrIMGwBtfSr4AuHiwDjfPx/e2Vl71Cd+oOaefhInD6m0GXpA8cBSDZCbwzmMsF2s27CtfWIExnkW2LKVJi3UzOc56GXf6VEPiGpqdjpfwSXUz6tS0xFflhLciTQraWP0Fb+Rc06++kJqtHNLK2hy/syeqR3SYLBKcdqsU+l6pI8yRsaN1MX9JKEpVI4S2NjsjJD9xrRfm4fnFNOcPvhK08QNvxDyxVv2Rcal8lbygZqEBPJqrh8aOsmu3FR8BdWrwO0/rR86J6BnKkkNwqmIn5pTY6Qet7CAX3g28lY83Jy9LsKpNjO6BeWrpjhlaZ8AOrEGenHg2Z3sNO6JsuF2T8bmdKFvicBNY3RfLdXVR5hMI8nvd+bpll92p8dt/eVyxEaUaZIjlB1rju54vxXgbJJpMHZihTEc0/evd6jNAoYH4FLMKxRRjuh3gAH1ujVrYaxZV+xqfJ1l67beu+9XrtJHFiGVi+tD9B/Ksj0s8oUq5KxQvNlqRkU3ZUYOgCGhOgww2drqrgY6pgFY17bQGE28Mmc9O/D7nst01MMHJDnU6HwNgm1Lszfmb/Yr5JLhdcWnhZUJ3WtNnraivipfoDLc+0bkrZhq9aqOAutulVR4c3875wmfi8bvniwZXMbjeKxv3Iv2ymg5J17oxz0CO6I08xmZs//UgZndmYuLocqBwNi+Z94gLWCNlLvH5aRrzKhac0FtDefjrUSdsvzxkxeYXdi/1SWNt970c8KQZSak')
    
    if response.status_code == 200:
        print('arquivo enviado')
        s3_resource.Object(bucket_name, aws_file_key).put(Body=json_data_tmdb)
    
    else:
        print('Falha!', response.status_code)