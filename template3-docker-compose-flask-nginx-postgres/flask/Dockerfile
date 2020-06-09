
# FROM python:alpine
# Use the Python3.7.2 image
# 指定一個 image 來源
FROM python:3.7.2-stretch

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app 
# ADD：將檔案加到 images 內
ADD . /app

# Install the dependencies
# build 時使用，會執行此命令
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# run the command to start uWSGI
# run container 時要執行的命令
CMD ["uwsgi", "app.ini"]


# ENV：環境變數設定