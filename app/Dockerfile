FROM python:3.9

RUN pip install poetry
COPY pyproject.toml .
RUN poetry install

COPY . .

CMD ["poetry", "run", "python", "main.py"]
