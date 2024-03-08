# Stage 1: Build the application
FROM maven:3.9.6-eclipse-temurin-17 AS build
WORKDIR /app
COPY pom.xml .
COPY src ./src
RUN mvn clean package -DskipTests

# Stage 2: Set up the runtime environment
FROM eclipse-temurin:17-jdk-alpine
WORKDIR /app

COPY --from=build /app/src/main/resources/* .
# Copy the built application from the build stage
COPY --from=build /app/target/datamanagement-service-0.2.0-SNAPSHOT.jar .

# Install Python and pip, then set up a virtual environment
RUN apk update && \
    apk add --no-cache python3 py3-pip && \
    python3 -m venv /app/venv

# Activate the virtual environment and install Python dependencies
ENV PATH="/app/venv/bin:$PATH"
RUN pip install --no-cache-dir requests

# Expose the port the app runs on
EXPOSE 8080

# Set the command to run the application
CMD ["java", "-jar", "datamanagement-service-0.2.0-SNAPSHOT.jar"]
