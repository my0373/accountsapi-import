#
FROM python:3.12
#
WORKDIR /code
#
COPY ./requirements.txt /code/requirements.txt
#
RUN pip install "fastapi[standard]"
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
#
COPY ./src /code/src
#
CMD ["fastapi", "run", "src/accountsapi.py", "--port", "80"]