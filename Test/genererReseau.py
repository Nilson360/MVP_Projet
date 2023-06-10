import yaml

def generate_compose_file(num_computers):
    # Crée un dictionnaire vide pour stocker les services
    services = {}

    # Pour chaque ordinateur de 1 à num_computers
    for i in range(1, num_computers + 1):
        # Crée un service pour chaque ordinateur avec les paramètres spécifiés
        services[f'pc{i}'] = {
            'build': '.',  # Utilise le Dockerfile présent dans le répertoire actuel
            'networks': ['backend']  # Connecte le service au réseau "backend"
        }

    # Crée un dictionnaire pour le fichier docker-compose.yml
    compose_dict = {
        'version': '3',  # Version du format du fichier
        'services': services,  # Ajoute les services au dictionnaire
        'networks': {
            'backend': None  # Crée le réseau "backend"
        }
    }

    # Ouvre le fichier docker-compose.yml en mode écriture
    with open('docker-compose.yml', 'w') as f:
        # Écrit le dictionnaire dans le fichier YAML
        yaml.dump(compose_dict, f)

# Demande à l'utilisateur de saisir le nombre d'ordinateurs à simuler
num_computers = int(input('Entrez le nombre d\'ordinateurs à simuler: '))

# Génère le fichier docker-compose.yml en utilisant le nombre d'ordinateurs spécifié
generate_compose_file(num_computers)
