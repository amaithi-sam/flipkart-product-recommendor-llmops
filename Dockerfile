## Use Python 3.12 to match your pyproject.toml requirements
FROM python:3.12-slim

## Essential environment variables
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    # Poetry configuration
    POETRY_VERSION=2.0.0 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_CREATE=false

# This adds the poetry executable to the system path so you can use the 'poetry' command
ENV PATH="$POETRY_HOME/bin:$PATH"

## Work directory
WORKDIR /app

## Installing system dependencies and Poetry
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && curl -sSL https://install.python-poetry.org | python3 - \
    && rm -rf /var/lib/apt/lists/*

## Copy only dependency files first
COPY pyproject.toml poetry.lock* ./

## Install dependencies (This will now work because of the PATH above)
RUN poetry install --no-interaction --no-ansi --no-root --no-cache

## Copy the rest of your application code
COPY . .

# Used PORTS
EXPOSE 5000

# Run the app 
CMD ["python", "app.py"]