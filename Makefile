update-packages:
	sudo apt-get update
	sudo apt-get upgrade

app:
	uvicorn --factory main:create_app --reload --host 0.0.0.0 --port $(port)
 

