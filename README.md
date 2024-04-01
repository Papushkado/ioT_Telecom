# ioT_Telecom


##Commandes pour Thingsboard

Pour lancer rapidement Thingsboard en utilisant Docker

```sh

docker volume create mytb-data
docker volume create mytb-logs

docker-compose.yml

docker compose up -d
docker compose logs -f mytb

docker compose start mytb

```
Ensuite le serveur se lance sur : [http://localhost:9090](http://localhost:8080/home)

Credentials : tenant@thingsboard.org / tenant
