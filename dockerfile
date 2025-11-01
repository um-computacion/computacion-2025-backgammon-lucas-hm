# Stage 1: Use an official Python runtime as a parent image
# You may want to check your repo for the exact Python version it uses
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the dependency file(s) into the container
# Assuming your dependencies are in requirements.txt
COPY requirements.txt ./

# Install any dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application source code into the container
COPY . .

# Command to run the application when the container starts
# You will need to replace 'your_main_script.py' with the actual entry point of your game
CMD ["python", "main.py"]

# If your backgammon game is a web application or exposes a port,
# uncomment and adjust the EXPOSE line (e.g., EXPOSE 8080)
# EXPOSE 80