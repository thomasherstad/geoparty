FROM python:3.12.7-bookworm

COPY ./requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV OPENAI_API_KEY=$OPENAI_API_KEY

ENTRYPOINT ["python3", "app.py"] 