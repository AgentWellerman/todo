ya nachal s api


{
  "title": "s1",
  "description": "s2",
  "completed": false
}



"""""version: "3.9"

services:
  mongo:
    image: mongo:7.0
    container_name: mongodb
    ports:
      - "27017:27017"
    healthcheck: 
      test: "echo 'db.runCommand({ ping: 1 })' | mongo --quiet"
      interval: 10s
      timeout: 5s
      retries: 5
    volumes:
      - mongo_data:/data/db

  app:
    build: .
    container_name: fastapi_app
    ports:
      - "8000:8000"
    depends_on:
      - mongo
    environment:
      - MONGO_URI=mongodb://mongo:27017
    volumes:
      - .:/app
    command:  >
      sh -c "
        until mongosh mongodb://mongo:27017 --eval 'db.adminCommand(\"ping\")'; do
          echo 'Waiting for MongoDB...';
          sleep 2;
        done;
        uvicorn main:app --host 0.0.0.0 --port 8000
      "

volumes:
  mongo_data:
""""

"