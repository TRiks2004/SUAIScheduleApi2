docker-folder = docker-file

AppEnviron = dockerAppEnviron.yaml
Portainer = portainer_agent.yaml
AppConf = dockerAppConf.yaml

# Дополнительные свойства для текта:
# \033[1m         	# жирный шрифт (интенсивный цвет)
# \033[2m        	# полу яркий цвет (тёмно-серый, независимо от цвета)
# \033[22m        	# установить нормальную интенсивность
# \033[4m     		# подчеркивание
# \033[4m  	  		# отменить подчеркивание
# \033[5m         	# мигающий
# \033[5m        	# отменить мигание
# \033[7m       	# реверсия (знаки приобретают цвет фона, а фон -- цвет знаков)
# \033[7m      		# отменить реверсию
# \033[m         	# все атрибуты по умолчанию
# \033[0m        	# все атрибуты по умолчанию

# Цвет текста:
#\033[0;30m     	# чёрный цвет знаков
#\033[0;31m       	# красный цвет знаков
#\033[0;32m     	# зелёный цвет знаков
#\033[0;33m     	# желтый цвет знаков
#\033[0;34m       	# синий цвет знаков
#\033[0;35m     	# фиолетовый цвет знаков
#\033[0;36m       	# цвет морской волны знаков
#\033[0;37m       	# серый цвет знаков

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


build-environment:
	sudo docker compose -f $(docker-folder)/$(AppEnviron) up --build -d 

build-portainer:
	sudo docker compose -f $(docker-folder)/$(Portainer) up --build -d 

build-fastapi:
	sudo docker compose -f $(docker-folder)/$(AppConf) up --build -d 


restart-environment:
	sudo docker compose -f $(docker-folder)/$(AppEnviron) restart

restart-portainer:
	sudo docker compose -f $(docker-folder)/$(Portainer) restart 

restart-fastapi:
	sudo docker compose -f $(docker-folder)/$(AppConf) restart 

restart-all: restart-environment restart-portainer restart-fastapi
	@echo "\033[1m\033[0;31mAll containers restarted\033[0m"


kill-environment:
	sudo docker compose -f $(docker-folder)/$(AppEnviron) kill

kill-portainer:
	sudo docker compose -f $(docker-folder)/$(Portainer) kill 

kill-fastapi:
	sudo docker compose -f $(docker-folder)/$(AppConf) kill 


pause-environment:
	sudo docker compose -f $(docker-folder)/$(AppEnviron) pause

pause-portainer:
	sudo docker compose -f $(docker-folder)/$(Portainer) pause 

pause-fastapi:
	sudo docker compose -f $(docker-folder)/$(AppConf) pause 

pause-all: pause-environment pause-portainer pause-fastapi
	@echo "\033[1m\033[0;32mAll containers paused\033[0m"


