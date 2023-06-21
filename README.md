# GIS-project

# Quick Start  
-git clone https://github.com/favju/GIS-project.git  
-cd .\GIS-project\  
-New-Item ".\Backend\secrets.json" -ItemType File -Value '{"DB_PASSWORD": "yourPassword"}'  
## change the password with the password you received from us  
-notepad.exe .\Backend\secrets.json  
-docker-compose build  
-docker-compose up  

# Getting started  

- Clone the repository
- Create a secrets.json at Backend/secrets.json  
```json
{
  "DB_PASSWORD": "yourPassword"
}
```
- Send an email to julien.favre1@students.hevs.ch or david.gianadda@students.hevs.ch to get the password and replace it in the secrets.json
- install and launch docker

## Launch docker

- Open a terminal at the root of the project

### Command

- docker-compose build
- docker-compose up

## Backend access

- localhost:8000/api
- localhost:8000/admin

## Frontend access

- localhost:8080/
