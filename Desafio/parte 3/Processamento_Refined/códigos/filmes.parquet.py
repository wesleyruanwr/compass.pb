#LEMBRANDO QUE FIZ PELO GOOGLE COLAB POR PROBLEMAS DE PERMISSÃO NA AWS
#COMENTEI LINHAS DE CÓDIGO QUE FICARIAM ERRADAS AQUI NO VSCODE APENAS APRA ORGANIZAÇÃO


#!pip install boto3 pandas pyarrow

import boto3
import pandas as pd
#import pyarrow as pa
#import pyarrow.parquet as pq
from io import BytesIO, StringIO

AWS_ACCESS_KEY_ID=''
AWS_SECRET_ACCESS_KEY=''
AWS_SESSION_TOKEN=''

s3 = boto3.client('s3',
                  aws_access_key_id = AWS_ACCESS_KEY_ID,
                  aws_secret_access_key = AWS_SECRET_ACCESS_KEY,
                  aws_session_token = AWS_SESSION_TOKEN
)

bucket_name = 'desafiowr'
file_key = 'Trusted/ArquivosCSV/movies_processed.csv'

response = s3.get_object(Bucket=bucket_name, Key=file_key)
csv_str = response['Body'].read().decode('utf-8')

df = pd.read_csv(StringIO(csv_str), sep='|')

colunas_ficam = ['id', 'tituloPincipal', 'anoLancamento', 'tempoMinutos', 'genero', 'notaMedia', 'numeroVotos']

df = df[colunas_ficam]

df['anoLancamento'] = pd.to_numeric(df['anoLancamento'], errors='coerce')

parquet_buffer = BytesIO()
#table = pa.Table.from_pandas(df)
#pq.write_table(table, parquet_buffer)

novo_parquet = 'Refined/arquivo.parquet'

parquet_buffer.seek(0)
s3.put_object(Bucket=bucket_name, Key=novo_parquet, Body=parquet_buffer.getvalue())