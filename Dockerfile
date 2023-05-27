# image base
FROM python:3-alpine

#Label docker image
LABEL version="0.1"
LABEL maintainer="Aviad Cohen"
LABEL release-date="2023-05-27"

# env variable
ENV USER=myuser
ENV APP_HOME=/app
ENV PATH="/home/$USER/.local/bin:${PATH}"

# Workind Directory
COPY . $APP_HOME
WORKDIR $APP_HOME

# Add User
RUN addgroup -S $USER && adduser -S $USER && chown $USER:$USER $APP_HOME -R && chmod 764 $APP_HOME -R
USER $USER

#install requirements
RUN pip install --disable-pip-version-check -r requirements.txt

# start process
CMD ["python","MainScore.py"]

