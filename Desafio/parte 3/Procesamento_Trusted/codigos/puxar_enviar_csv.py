#LEMBRANDO QUE ESSE FOI O CODIGO USADO PARA FZER NO GOOGLE COLAB

#pip install boto3
#pip install pandas

import boto3
import pandas as pd
from io import StringIO

AWS_ACCESS_KEY_ID=""
AWS_SECRET_ACCESS_KEY=""
AWS_SESSION_TOKEN =""

s3_client = boto3.client('s3',
                         aws_access_key_id = AWS_ACCESS_KEY_ID,
                         aws_secret_access_key= AWS_SECRET_ACCESS_KEY,
                         aws_session_token = AWS_SESSION_TOKEN)

bucket_name = "desafiowr"
input_csv_key = "Raw/Local/CSV/Movies/2024/02/19/movies.csv"

s3_object = s3_client.get_object(Bucket=bucket_name, Key=input_csv_key)

df = pd.read_csv(s3_object['Body'], sep="|", encoding="utf-8")

csv_buffer = StringIO()
df.to_csv(csv_buffer, sep="|", encoding="utf-8", index=False)
csv_buffer.seek(0)


output_csv_key = "Trusted/ArquivosCSV/movies_processed.csv"
s3_client.put_object(Bucket=bucket_name, Key=output_csv_key, Body=csv_buffer.getvalue())

print("DataFrame successfully uploaded to S3.")