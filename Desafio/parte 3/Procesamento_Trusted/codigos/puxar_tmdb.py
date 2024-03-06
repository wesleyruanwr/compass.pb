import boto3
import pandas as pd
import json
from datetime import datetime

AWS_ACCESS_KEY_ID=""
AWS_SECRET_ACCESS_KEY=""
AWS_SESSION_TOKEN =""

s3_client = boto3.client('s3',
                         aws_access_key_id = AWS_ACCESS_KEY_ID,
                         aws_secret_access_key= AWS_SECRET_ACCESS_KEY,
                         aws_session_token = AWS_SESSION_TOKEN)

bucket_name = "desafiowr"
input_json_key = "Raw/tmdb/json/2024/02/25/data_(27, 53)-032147.json"

s3_object = s3_client.get_object(Bucket=bucket_name, Key=input_json_key)

json_data = json.loads(s3_object['Body'].read().decode('utf-8'))

df = pd.json_normalize(json_data)

file_path_parts = input_json_key.split("/")
date_str = file_path_parts[-4:-1]
date = "-".join(date_str)
date_formatted = datetime.strptime(date, "%Y-%m-%d").date()

parquet_file_name = f"tmdb_data_dt={date_formatted}.parquet"
df.to_parquet(parquet_file_name)

print(f"DataFrame saved to Parquet file: {parquet_file_name}")