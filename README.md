# Rapport TP1 :

## Liens et commande : 

Image du wrapper get weather sur dockerhub à cette adresse : 

[https://hub.docker.com/r/hamzadgr/getweather ](https://hub.docker.com/repository/docker/hamzadgr/getweather/general)


Commande pour executer le docker file :

docker run --env LAT="X.XX" --env LONG="Y.YY" --env API_KEY=votre_API_KEY 20230072/getweather:latest

## Technologie 

Dans ce TP, nous avons utilisé python pour créer un wrapper qui à partir d'une longitude et latitude renvoie les données météo associées grâce à l'API Openweather.
Nous avons ensuite créé une image docker qui est disponible sur dockerhub à l'adresse renseigée précedemment. 

## Difficultés rencontrés

Suite à un MacOS trop ancien pour installer docker sur ma machine, j'ai eu de grandes difficultés pour y avoir accsès. De ce fait, j'ai installé la dernière version d'ubuntu sur un pc fixe ce qui m'a permis d'installer docker et de faire le TP. 
Cela m'a permis de maitriser un nouvel OS et de travailler sur de la config (clé boutable, installation, configuration de linux etc).
