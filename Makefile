docker-folder = docker-file

AppEnviron = dockerAppEnviron.yaml
Portainer = portainer_agent.yaml
AppConf = dockerAppConf.yaml

update-packages:
	sudo apt-get update
	sudo apt-get upgrade

app:
	uvicorn --factory main:create_app --reload --host 0.0.0.0 --port $(port)


start-environment:
	sudo docker compose -f $(docker-folder)/$(AppEnviron) up -d

start-portainer:
	sudo docker compose -f $(docker-folder)/$(Portainer) up -d

start-fastapi:
	sudo docker compose -f $(docker-folder)/$(AppConf) up -d


start-environment-build:
	sudo docker compose -f $(docker-folder)/$(AppEnviron) up --build -d 

start-portainer-build:
	sudo docker compose -f $(docker-folder)/$(Portainer) up --build -d 

start-fastapi-build:
	sudo docker compose -f $(docker-folder)/$(AppConf) up --build -d 


start-environment-restart:
	sudo docker compose -f $(docker-folder)/$(AppEnviron) restart

start-portainer-restart:
	sudo docker compose -f $(docker-folder)/$(Portainer) restart 

start-fastapi-restart:
	sudo docker compose -f $(docker-folder)/$(AppConf) restart 


start-environment-kill:
	sudo docker compose -f $(docker-folder)/$(AppEnviron) kill

start-portainer-kill:
	sudo docker compose -f $(docker-folder)/$(Portainer) kill 

start-fastapi-kill:
	sudo docker compose -f $(docker-folder)/$(AppConf) kill 


