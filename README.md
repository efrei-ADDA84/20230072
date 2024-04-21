# Rapport TP4 :

## Liens et commande : 

### Contexte : 

Dans ce TP, nous avons appris à créer et déployer une machine virtuelle sur n'importe quel provider (en l'occurence azure pour nous) à travers la bibliothèque terraform et la microsft azure CLI.


## Technologie 

Dans ce TP, nous avons utilisé bibliothèque Terraform pour créer et déployer une machine virtuelle directement sur microsoft azure et ce à partir d'un fichier de configuration 'main.tf'
L'objectif était ensuite de s'entrainer à la création d'une machine virtuelle tout en la configurant avec des paramètres particuliers et ce sans passer par Azure ou par la azure CLI.
L'objectif était aussi de créer une clé SSH directement avec Terraform.

## Etapes 

- Installation de Terraform avec homebrew ou CURL et Azure CLI à travers des commandes disponibles dans la documentation
- Création du fichier de configuration de la machine virtuelle grçace à la documentation et aux paramètres spécifiés dans la consigne du TP
- Terraform init
- Terraform apply (la machine virtuelle se créée et se déploye)
- Terraform destroy (la machine virtuelle ainsi que les réseaux etc sont détruits)
- Test de connection à la machine virtuelle à travers le terminal avec la commande 
    ssh -i <clé_ssh> devops@<ADRESSE_IP> cat /etc/os-release 
    -> permet de tester la connection ssh et récupérer les informations sur l'OS de la VM

## Difficultés rencontrés

Je ne connaissais absolument pas la bibliothèque Terraform et j'ai donc eu besoin de prendre le temps de lire la documentation pour pouvoir l'utiliser au début. Des difficultés à comprendre ce qu'il fallait créer pour que la machine virtuelle soit fonctionnelle donc beaucoup de temps sur le fichier de configuration à tester avec des terraform apply si cela fonctionnait.

## Apports de Terraform par rapport à Azure CLI ou UI

Avoir une Infrastructure as a Code permet de gérer plus facilement la configuration des infrastructres que l'on veut déployer. De plus, cela permet l'automatisation et la plannification des déploiement. Enfin, je pense que cela est plus simple à maintenir et faire évoluer si besoin car accès direct aux variables.
