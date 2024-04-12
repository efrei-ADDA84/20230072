# Rapport TP2 :

## Liens et commande : 

Image du wrapper get weather sur dockerhub à cette adresse : 

[[https://hub.docker.com/r/hamzadgr/getweather ]](https://hub.docker.com/repository/docker/hamzadgr/getweather_api/)(https://hub.docker.com/repository/docker/hamzadgr/getweather/general)


Commande pour executer le docker file :

docker run --network host --env API_KEY=**** hamzadgr/getweather_api:latest
puis dans un autre terminal : curl "http://localhost:8081/?lat=5.902785&lon=102.754175"

## Technologie 

Dans ce TP, nous avons utilisé python et la bibliothèque Flask pour créer une API qui à partir d'une longitude et latitude renvoie les données météo associées grâce à l'API Openweather.
L'objectif était ensuite de s'initier à la création d'un workflow github action qui permet d'executer des tâches à chaque comit sur le projet. 

## Etapes 

- J'ai dans un premier temps codé l'API avec la bibliothèque Flask
- J'ai ensuite créée le docker-publish.yaml pour configurer le workflow
- Dès que le workflow était fonctionnel et après avoir testé l'API à travers l'image docker, j'ai ajouté hadolint qui m'a permis de détécter des éléments deprecated dans mon code

## Difficultés rencontrés

J'ai eu énormément de diffcultés à me connecter à dockerhub depuis github directement. Je ne savais pas que le username était sensible à la casse. De plus, les versions des commandes comme actions/checkout@v4 étaient obselètes et la documentation n'est pas très claire. J'ai eu pas mal de difficulté à trouver des docs officielles sur les github actions et notamment les versions les plus à jour. En revanche une fois les problèmes de connection, l'ajout d'hadolint a été plutot simple et m'a permis de mettre à jour certaines commandes.
