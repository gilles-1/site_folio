# Utilisez l'image officielle Python depuis Docker Hub
FROM python:3.9

# Définissez le répertoire de travail dans le conteneur
WORKDIR /app

# Copiez le fichier requirements.txt dans le conteneur
COPY requirements.txt /app/

# Installez les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Copiez le reste des fichiers dans le conteneur
COPY . /app/

# Exposez le port sur lequel votre application Django s'exécute
EXPOSE 8000

# Démarrez votre application Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]