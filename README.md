# Rapport TP1 :

## Liens et commande : 

Code utilisé pour le dockerfile get weather à cette adresse : 

https://hub.docker.com/r/hamzadgr/getweather 

Commande pour executer le docker file :

docker run --env LAT="X.XX" --env LONG="Y.YY" --env API_KEY=votre_API_KEY 20230072/getweather:latest

## Technologie 

Dans ce TP, nous avons utilisé python pour créer un wrapper qui à partir d'une longitude et latitude renvoie les données météo associées grâce à l'API Openweather.
Nous avons ensuite créé une image docker qui est disponible sur dockerhub à l'adresse renseigée précedemment. 

## Difficultés rencontrés

Suite à un OS trop ancien pour docker, j'ai eu de grandes difficultés pour y avoir accsès. De ce fait, j'ai installé ubuntu sur un pc fixe ce qui m'a permis d'installer docker et de créer l'image de mon wrapper. 
Cela m'a permis de maitriser un nouvel OS et de travailler sur de la config.
