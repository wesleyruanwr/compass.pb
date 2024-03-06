import boto3
import pandas as pd

AWS_ACCESS_KEY_ID=""
AWS_SECRET_ACCESS_KEY=""
AWS_SESSION_TOKEN =""  

s3_client = boto3.client('s3',
                         aws_access_key_id=AWS_ACCESS_KEY_ID,
                         aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                         aws_session_token=AWS_SESSION_TOKEN)

bucket_name = "desafiowr"
output_parquet_file = "tmdb_data_dt=2024-02-25.parquet"

df = pd.read_parquet(output_parquet_file)

json_data = df.to_json(orient='records')

s3_key = "Trusted/ArquivosTMDB/" + output_parquet_file

s3_client.put_object(
    Bucket=bucket_name,
    Key=s3_key,
    Body=json_data.encode('utf-8'), 
    ContentType='application/json' 
)

print(f"File {output_parquet_file} uploaded to bucket {bucket_name} with key {s3_key}")