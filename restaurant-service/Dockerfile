# Image de base Python
FROM python:3.11

# Dossier de travail
WORKDIR /app

# Copier et installer les dépendances
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copier tout le code
COPY . .

# Appliquer les migrations automatiquement
RUN python manage.py migrate

# Charger les données initiales
RUN python manage.py loaddata tables/fixtures/tables.json

# Exposer le port
EXPOSE 8082

# Lancer le serveur
CMD ["python", "manage.py", "runserver", "0.0.0.0:8082"]