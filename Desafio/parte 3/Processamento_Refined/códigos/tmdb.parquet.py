#LEMBRANDO QUE FIZ PELO GOOGLE COLAB POR PROBLEMAS DE PERMISSÃO NA AWS

import boto3

AWS_ACCESS_KEY_ID=''
AWS_SECRET_ACCESS_KEY=''
AWS_SESSION_TOKEN=''

s3 = boto3.client('s3', 
                  aws_access_key_id = AWS_ACCESS_KEY_ID, 
                  aws_secret_access_key = AWS_SECRET_ACCESS_KEY,
                  aws_session_token = AWS_SESSION_TOKEN)

bucket_name = 'desafiowr'
arquivo_parquet = 'Trusted/ArquivosTMDB/tmdb_data_dt=2024-03-07.parquet'
novo_caminho = 'Refined/tmdb_data_dt=2024-03-07.parquet'

s3.copy_object(
    Bucket=bucket_name,
    Key=novo_caminho,
    CopySource={'Bucket': bucket_name, 'Key': arquivo_parquet}
)