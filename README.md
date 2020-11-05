# Tor_Request
Make Anonymous Request with TorRequests and Python

Dans ce tutoriel, nous verrons comment effectuer des requêtes anonymes via le module TorRequests de Python

## Installation

Nous pouvons tout d'abord installer __Tor__:
```
sudo apt update
sudo apt install tor
```
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
Puis relancer le service Tor
```
sudo /etc/init.d/tor restart
```
## Configurer Tor
Nous allons tout d'abord générer un hash
```
tor --hash-password <your_password>
```
Nous avons ensuite besoin de configurer notre fichier __torrc__, fichier de configuration de Tor
```
sudo nano /etc/tor/torrc
```
Nous allons décommenter plusieurs ligne:
- SOCKSPort 9050
- HashedControlPassword <your_hash_password> ( coller ici le hash que vous avez généré )
- Cookie Authentication 1

Sauvegarder le fichier puis relancer le service Tor:
```
sudo /etc/init.d/tor restart
```
Tor est maintenant correctement configurer, nous allons pouvoir passer à la pratique.
##Èxécuter
Nous allons installer __torrequest__, module de Python qui nous permettra d'accèder à la config de Tor
```
pip install torrequest
```
Une fois l'installation terminée, nous allons créer un fichier __tor_request.py__:
```
nano tor_request.py
```
Nous commençons par importer le module torrequest
```
from torrequest import TorRequest
```
Puis nous pouvons éxécuter notre requête:
```
with TorRequest() as tr:
  tr.reset_identity()
  response = tr.get("http://ipecho.net/plain")
  print(response.text)
```
Nous requêtons vers __ipecho.net__ pour connaître notre IP au moment de notre requête
Vous pouvez maintenant sauvegarder votre fichier puis éxécuter le script:
```
python tor_request.py
```

Vous pouvez également retrouver le code dans le fichier (tor_request.py)[] du repo
