# start by pulling the python image
FROM python:latest
 
# switch working directory
WORKDIR /app

COPY requirements.txt /app/requirements.txt
# install the dependencies and packages in the requirements file
RUN pip install -r requirements.txt

ENTRYPOINT [ "bash" ]