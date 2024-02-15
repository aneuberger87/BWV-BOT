FROM maven:3.9.6-eclipse-temurin-17 AS build
WORKDIR /app
COPY pom.xml .
COPY src ./src
RUN mvn clean package
FROM eclipse-temurin:17-jdk
WORKDIR /app
#ENTRYPOINT ["java", "-jar", "target/datamanagement-service-0.1.0-SNAPSHOT.jar"]
COPY --from=build /app/target/datamanagement-service-0.1.0-SNAPSHOT.jar .
# Set the command to run the application
CMD ["java", "-jar", "datamanagement-service-0.1.0-SNAPSHOT.jar"]
