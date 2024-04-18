# Rapport TP2 :

## Liens et commande : 

Image du wrapper get weather sur dockerhub à cette adresse : 

[[https://hub.docker.com/r/hamzadgr/getweather_api]](https://hub.docker.com/repository/docker/hamzadgr/getweather_api/)(https://hub.docker.com/repository/docker/hamzadgr/getweather/general)


Commande pour executer le docker file :

Dans votre terminal : 

curl "http://devops-20230072.westeurope.azurecontainer.io/weather?LATTITUDE=5.902785&LONGITUDE=102.754175"

## Technologie 

Dans ce TP, nous avons utilisé python et la bibliothèque Flask pour créer une API qui à partir d'une longitude et latitude renvoie les données météo associées grâce à l'API Openweather.
L'objectif était ensuite de s'entrainer à la création d'un workflow github action qui permet d'executer des tâches à chaque comit sur le projet. 
D'une part de déployer automatiquement le projet dans une image docker sur docker hub. Puis de déployer cette image docker sur le cloud azure pour qu'elle soit disponible depuis nimporte quelle machine.

## Etapes 

- J'ai gardé le projet qui avait été développé précedemment 
- J'ai ensuite ajouté au docker-publish.yaml un job de publication de l'image docker sur azure en utilisant les secrets à disposition
- J'ai testé le bon fonctionnement de l'API à travers un terminal sur mon pc et un navigateur

## Difficultés rencontrés

Enormément de difficultés à configurer mon yaml en fonction de azure. Pas mal de problèmes car je n'avais pas remarqué que l'API Key n'était plus indiquée dans la ligne de commande. J'ai finalement réussi à corriger tous ces problèmes pour que ça soit fonctionnel.
