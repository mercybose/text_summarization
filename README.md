# text_summarization

Below steps must be followed to run this application in a Docker container

1) Ensure that Docker is installed on the system
2) Copy these files into a folder eg: test_docker that is accessible from the command line. 
NOTE: If using a Windows system, ensure WSL is installed and Docker is started and create a folder in the Linux sub system within Windows.

3) Navigate to this folder (if Windows, navigate using the Linux subsystem by typing \\wsl$ in the address bar)
4) Create a Docker image from the Dockerfile by using command:
docker build -t image_name .

5) Ensure that the image has been created by using commmand:
docker images

6) Publish the Docker Image by using command:
docker run --publish 5000:5000 image_name

7) Once the server is running, open a new terminal and send a request to the text summarization API
WINDOWS:

curl http://127.0.0.1:5000/summarize -d "{\"text_to_summarize\": \"On December 31, 2019, China announced the discovery of a cluster of pneumonia cases in Wuhan. The first American case was reported on January 20, and President Donald Trump declared the U.S. outbreak a public health emergency on January 31.\"}" -H "Content-Type: application/json"

MAC:

curl http://127.0.0.1:5000/summarize -d "{\"text_to_summarize\": \"On December 31, 2019, China announced the discovery of a cluster of pneumonia cases in Wuhan. The first American case was reported on January 20, and President Donald Trump declared the U.S. outbreak a public health emergency on January 31.\"}" -H "Content-Type: application/json"

8) Receive output as a json with keys - original_text  and summary (containing the summarized text)
