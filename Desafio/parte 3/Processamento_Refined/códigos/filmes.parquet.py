#LEMBRANDO QUE FIZ PELO GOOGLE COLAB POR PROBLEMAS DE PERMISSÃO NA AWS
#COMENTEI LINHAS DE CÓDIGO QUE FICARIAM ERRADAS AQUI NO VSCODE APENAS APRA ORGANIZAÇÃO

#ESTA DIFERENTE DO PRINT PORQUE DURANTE O USO DO QUICKSIGHT PRECISEI FAZER MUDANCAS


#!pip install boto3 pandas pyarrow

import boto3
import pandas as pd
from io import BytesIO

AWS_ACCESS_KEY_ID = ""
AWS_SECRET_ACCESS_KEY = ""
AWS_SESSION_TOKEN = ""

s3_client = boto3.client('s3',
                         aws_access_key_id=AWS_ACCESS_KEY_ID,
                         aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                         aws_session_token=AWS_SESSION_TOKEN)

bucket_name = "desafiowr"
parquet_file_key = "Trusted/movies/movies_processed.parquet"

s3_object = s3_client.get_object(Bucket=bucket_name, Key=parquet_file_key)
parquet_data = s3_object['Body'].read()

df = pd.read_parquet(BytesIO(parquet_data))

colunas_remover = ["id", "tituloOriginal", "generoArtista", "personagem", "nomeArtista", "anoNascimento", "anoFalecimento", "profissao", "titulosMaisConhecidos"]
df = df.drop(columns=colunas_remover)

df.drop_duplicates(subset='tituloPrincipal', keep='first', inplace=True)

print(df.head())

s3_key = "s3/Refined/filmes/" 

buffer = BytesIO()
df.to_parquet(buffer)
buffer.seek(0)
s3_client.put_object(Body=buffer, Bucket=bucket_name, Key=s3_key)