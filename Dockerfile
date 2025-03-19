# Gebruik de officiële Python 3.12 slim image als basis
FROM python:3.12-slim

# Installeer benodigde pakketten voor de installatie van Poetry
RUN apt-get update && apt-get install -y curl build-essential

# Stel de versie van Poetry in en installeer Poetry
ENV POETRY_VERSION=2.0.1
RUN curl -sSL https://install.python-poetry.org | python3 - --version $POETRY_VERSION

# Voeg Poetry toe aan de PATH
ENV PATH="/root/.local/bin:${PATH}"

# Stel de werkdirectory in
WORKDIR /app

# Kopieer de configuratiebestanden van Poetry
COPY pyproject.toml poetry.lock* /app/

# Installeer de dependencies met Poetry (gebruik --no-dev voor productie)
RUN poetry install --no-interaction --no-ansi

# Kopieer de rest van de applicatiecode
COPY . /app/

# Exposeer de poort waarop FastAPI draait (standaard 8000)
EXPOSE 8000

# Start de applicatie met uvicorn via Poetry
CMD ["poetry", "run", "uvicorn", "main:app", "--host", "127.0.0.1", "--port", "8000"]
