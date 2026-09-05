FROM node:latest AS storefront
WORKDIR /usr/src/atsea/app/react-app
COPY react-app .
RUN npm install
RUN npm run build


# CHANGED: Use Maven with Java 8 explicitly (maven:3.8-openjdk-8)
FROM maven:3.8-openjdk-8 AS appserver
WORKDIR /usr/src/atsea
COPY pom.xml .
# CHANGED: Added '-U' to force update, and 'clean' to clear corrupted cache
RUN mvn -B -U clean -f pom.xml -s /usr/share/maven/ref/settings-docker.xml dependency:resolve
COPY . .
# CHANGED: Added '-U' to force update dependencies during package phase
RUN mvn -B -U -s /usr/share/maven/ref/settings-docker.xml package -DskipTests

FROM eclipse-temurin:8-jdk-alpine
RUN adduser -Dh /home/gordon gordon
WORKDIR /static
COPY --from=storefront /usr/src/atsea/app/react-app/build/ .
WORKDIR /app
COPY --from=appserver /usr/src/atsea/target/AtSea-0.0.1-SNAPSHOT.jar .
ENTRYPOINT ["java", "-jar", "/app/AtSea-0.0.1-SNAPSHOT.jar"]
CMD ["--spring.profiles.active=postgres"]
