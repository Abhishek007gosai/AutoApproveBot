# Use an official Python base image
FROM python:3.10-slim

# Set working directory inside the container
WORKDIR /app

# Copy all files into the container
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the bot
CMD ["python", "bot.py"]
