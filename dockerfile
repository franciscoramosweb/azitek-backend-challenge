# Use an official Python runtime as a parent image
FROM python:3

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the current directory contents into the container at /usr/src/app
COPY . .

# Install any needed dependencies specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Set API_KEY as an environment variable
ENV API_KEY="[API_KEY]"

# Run the Python script
CMD [ "python", "./tracking.py" ]