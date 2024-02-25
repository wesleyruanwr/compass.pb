FROM python:3.12

RUN pip install requests pandas ipython

WORKDIR /app

COPY . .

ENV API_KEY="67f395bf0688fde6e615e6e8f44cb97a"

CMD ["python", "requisiçãoTMDB.py"]
