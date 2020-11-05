# Tor_Request
Make Anonymous Request with TorRequests and Python

Dans ce tutoriel, nous verrons comment effectuer des requêtes anonymes via le module TorRequests de Python

## Installation

Création d'un environnement virtuel
```
virtualenv env
```
Si vous ne disposez pas de __virtualenv__, vous pouvez l'installer via __PIP__:
```
python -m pip install virtualenv
```
Activez notre environnement virtuel
```
source env/bin/activate
```
Nous pouvons ensuite installer __Tor__:
```
sudo apt update
sudo apt install tor
```
Puis relancer le service
```
sudo /etc/init.d/tor restart
```
