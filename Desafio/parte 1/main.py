import boto3
from datetime import datetime

BUCKET_NAME = 'desafiowr'
DATE = datetime.now().strftime('%Y/%m/%d')

LOCAL_FILE_NAME_MOVIES = "movies.csv"
LOCAL_FILE_NAME_SERIES = "series.csv"

AWS_FILE_KEY_MOVIES = f"Ram/Local/CSV/Movies/{DATE}/movies.csv"
AWS_FILE_KEY_SERIES = f"Ram/Local/CSV/Series/{DATE}/series.csv"

def main(): 
    client = boto3.client('s3', 
                            aws_access_key_id = '',
                            aws_secret_access_key = '',
                            aws_session_token = ''
    )
    
    try:
        client.put_object(Bucket=BUCKET_NAME, Key=AWS_FILE_KEY_MOVIES, Body=LOCAL_FILE_NAME_MOVIES)
        client.put_object(Bucket=BUCKET_NAME, Key=AWS_FILE_KEY_SERIES, Body=LOCAL_FILE_NAME_SERIES)
        print(f"Enviados")
    except Exception as e:
        print(f"Erro durante o upload: {e}")

if __name__ == '_main_':
    main()
