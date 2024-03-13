# Instructions

This Markdown file provides clear instructions for both running the script locally and in a Docker container.

This script retrieves and processes data from the Azitek tracking system API and generates a graph based on the data.

## Running Locally

To run the script locally, follow these steps:

1. **Install Python 3**: If you haven't already, install Python 3 from [here](https://www.python.org/downloads/).

2. **Install Dependencies**: Install the required dependencies using pip:

pip install -r requirements.txt


3. **Set API Key**: Set the API_KEY environment variable:
- **On Windows**:
  ```
  set API_KEY=your_api_key
  ```
- **On Linux/macOS**:
  ```
  export API_KEY=your_api_key
  ```

4. **Run Script**: Execute the script:

python tracking.py


## Running in a Container

To run the script in a container using Docker, follow these steps:

1. **Install Docker**: If you haven't already, install Docker from [here](https://www.docker.com/products/docker-desktop).

2. **Build Docker Image**: Build the Docker image:

docker build -t my-python-app .


3. **Set API Key**: Set the API_KEY environment variable in the Docker run command:
- **On Windows**:
  ```
  docker run -e API_KEY=your_api_key my-python-app
  ```
- **On Linux/macOS**:
  ```
  docker run -e API_KEY=your_api_key my-python-app
  ```

This will run the script inside a Docker container and output the graph image.

Replace your_api_key with your actual API key. 






