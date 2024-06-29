# Use the official Python image from the Docker Hub
FROM python:3.11-slim

# Install python3-venv and other dependencies
RUN apt-get update && \
    apt-get install -y python3-venv && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /app

# Install Poetry
RUN pip install poetry==1.8.2

# Copy the pyproject.toml and poetry.lock files
COPY pyproject.toml poetry.lock /app/

# Install the dependencies using Poetry
RUN poetry install --no-dev 

# Copy the rest of the application code
COPY . /app

# Set environment variables
# The .env file will be read by python-dotenv within the application
ENV BOT_ENV=production

# Expose the port (if your bot runs a web server)
# EXPOSE 8000

# Command to run the bot
CMD ["poetry", "run", "python", "bot.py"]
