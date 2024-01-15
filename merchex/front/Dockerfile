# Utilisez l'image officielle Node.js LTS (Long Term Support) depuis Docker Hub
FROM node:lts

# Définissez le répertoire de travail dans le conteneur
WORKDIR /app

# Copiez le fichier package.json et le fichier package-lock.json dans le conteneur
COPY package*.json ./

# Installez les dépendances
RUN npm install

# Copiez le reste des fichiers dans le conteneur
COPY . .

# Exposez le port sur lequel votre application Vue.js s'exécute (généralement le port 8080)
EXPOSE 8080

# Démarrez votre application Vue.js
CMD ["npm", "run", "serve"]