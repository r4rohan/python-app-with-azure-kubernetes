# FROM maven:3.6.0-jdk-11-slim AS build
# ENV APP_HOME=/home/app
# COPY src $APP_HOME/src
# COPY pom.xml $APP_HOME
# RUN mvn -f $APP_HOME/pom.xml clean package

# FROM openjdk:8
# COPY --from=build $APP_HOME/target/*.jar /usr/local/lib/app.jar
# CMD java ${JAVA_OPTS} -jar app.jar
 
FROM python:3.6
WORKDIR /app
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . /app
EXPOSE 5000
CMD [ "python", "test.py" ]