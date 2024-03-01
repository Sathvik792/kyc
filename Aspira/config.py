import os
from dotenv import load_dotenv
import sys

load_dotenv()


# AWS credentials
AWS_ACCESS_KEY_ID = os.environ["AWS_ACCESS_KEY_ID"]
AWS_SECRET_ACCESS_KEY = os.environ["AWS_SECRET_ACCESS_KEY"]
AWS_REGION = os.environ["AWS_REGION"]
AWS_S3_BUCKET_NAME = os.environ["AWS_S3_BUCKET_NAME"]


# SMTP Service credentials
SMTP_SERVER = os.environ["SMTP_SERVER"]
SMTP_PORT = os.environ["SMTP_PORT"]
SMTP_USERNAME = os.environ["SMTP_USERNAME"]
SMTP_PASSWORD = os.environ["SMTP_PASSWORD"]
EMAIL_FROM = os.environ["EMAIL_FROM"]

# Bot login credentials
BOT_EMAIL_ID = os.environ["BOT_EMAIL_ID"]
BOT_PASSWORSD = os.environ["BOT_PASSWORSD"]

# mongodb credentials
MONGODB_HOST = os.environ["MONGODB_HOST"]
MONGODB_PORT = os.environ["MONGODB_PORT"]
MONGODB_DATABASE_NAME = os.environ["MONGODB_DATABASE_NAME"]
MONGODB_JOBOPENINGS_COLLECTION = os.environ["MONGODB_JOBOPENINGS_COLLECTION"]
MONGODB_INTERVIEWSCHEDUILES_COLLECTION = os.environ[
    "MONGODB_INTERVIEWSCHEDUILES_COLLECTION"
]


# postgres credentials
POSTGRES_HOST = os.environ["POSTGRES_HOST"]
POSTGRES_DATABASE = os.environ["POSTGRES_DATABASE"]
POSTGRES_USER = os.environ["POSTGRES_USER"]
POSTGRES_PASSWORD = os.environ["POSTGRES_PASSWORD"]
POSTGRES_PORT = os.environ["POSTGRES_PORT"]


OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
ASPIRA_MONGODB_CONN = os.environ["ASPIRA_MONGODB_CONN"]
