
FROM python:3.12-slim


RUN apt-get update && apt-get install -y curl build-essential


ENV POETRY_VERSION=2.0.1
RUN curl -sSL https://install.python-poetry.org | python3 - --version $POETRY_VERSION


ENV PATH="/root/.local/bin:${PATH}"

# Current workdir
WORKDIR /app

# copy only the dependencies definition files
COPY pyproject.toml poetry.lock* /app/


RUN poetry install --no-interaction --no-ansi


COPY . /app/

# Expose the port that the app runs on
EXPOSE 3000

# Serve the app
CMD ["poetry", "run", "uvicorn", "main:app", "--host", "127.0.0.1", "--port", "3000"]
