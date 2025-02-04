
# 🚀 Guide d'Installation et d'Utilisation de Nexus Docker Registry et Proxy

Ce guide explique comment configurer et utiliser **Nexus Repository Manager** en tant que **Docker Registry** et **Docker Proxy**, permettant de stocker et de récupérer des images Docker à la fois depuis un repository privé et depuis Docker Hub via un proxy.

---

## Prérequis

- **Docker** et **Docker Compose** installés sur votre machine (Ubuntu ou macOS).

---

## 🔧 Étape 1 : Lancer Nexus avec Docker Compose

1. **Démarrer Nexus**

   Dans le répertoire où vous avez créé le fichier `docker-compose.yml`, exécutez la commande suivante pour démarrer Nexus en arrière-plan :

   ```sh
   docker-compose up -d
   ```

   Vous pouvez vérifier que le conteneur fonctionne avec :

   ```sh
   docker ps
   ```

---

## 🌐 Étape 2 : Accéder à l'Interface Web de Nexus

1. **Accédez à Nexus** via votre navigateur à l'URL suivante :

   ```
   http://localhost:8081
   ```

2. **Connectez-vous** avec les identifiants par défaut :

   - **Username :** `admin`
   - **Password :** Le mot de passe se trouve dans le fichier `/nexus-data/admin.password` du conteneur Nexus. Pour le récupérer, exécutez la commande suivante :

     ```sh
     docker exec -it <container_id> cat /nexus-data/admin.password
     ```

   Remplacez `<container_id>` par l'ID de votre conteneur Nexus. Vous pouvez obtenir l'ID avec :

   ```sh
   docker ps
   ```

---

## 🛠️ Étape 3 : Configurer Nexus en tant que Docker Proxy pour Docker Hub

1. Dans **Nexus Web UI**, allez dans **"Repositories"** sous **"Repository"** dans le menu de gauche.
2. Cliquez sur **"Create repository"** en haut à droite.
3. Sélectionnez **"Docker (proxy)"**.
4. Configurez le repository comme suit :
   - **Name :** `docker-hub-proxy`
   - **HTTP Port :** `8083` (port pour accéder au Docker Hub via Nexus).
   - **Remote URL :** `https://registry.hub.docker.com`
   - Cochez **"Allow anonymous pull"** pour permettre l'accès en lecture sans authentification.
   - Cliquez sur **Save**.

---

## 🛠️ Étape 4 : Créer un Repository Docker Hosted

1. Accédez à **Nexus Web UI** sur `http://localhost:8081` et connectez-vous avec le mot de passe `admin`.
2. Allez dans **"Repositories"** sous **"Repository"** dans le menu de gauche.
3. Cliquez sur **"Create repository"** en haut à droite.
4. Sélectionnez **"Docker (hosted)"**.
5. Configurez le repository comme suit :
   - **Name :** `docker-private`
   - **HTTP Port :** `8082` (port pour accéder au Docker registry).
   - Cochez **"Allow anonymous pull"** (pour permettre l'accès en lecture sans authentification).
   - Cliquez sur **Save**.

---

## 🔒 Étape 5 : Ajouter les "Realms" pour Authentification

1. Allez dans **Administration** → **Security** → **Realms** dans Nexus UI.
2. Assurez-vous que le **"Docker Bearer Token Realm"** est activé pour gérer les jetons d'authentification Docker.

---

## 🚪 Étape 6 : Configurer Docker pour un Registre Insecure

Pour permettre à Docker de se connecter à Nexus via HTTP sur le port `8082`, vous devez ajouter ce port dans les registres non sécurisés (insecure registries).

### Sur Ubuntu ou macOS :

1. **Créer ou modifier** le fichier `/etc/docker/daemon.json` :

   ```json
   {
     "insecure-registries": ["localhost:8082", "localhost:8083"]
   }
   ```

2. **Redémarrer Docker** :

   - **Sur Ubuntu :**
     ```sh
     sudo systemctl restart docker
     ```

   - **Sur macOS :** Redémarrez Docker via l'interface graphique.

---

## 💻 Étape 7 : Se connecter au Docker Registry

Exécutez la commande suivante pour vous connecter à Nexus via Docker :

```sh
docker login -u admin localhost:8082
```

Entrez le mot de passe crée précédemment pour vous connecter à Nexus.

---

## 🚀 Étape 8 : Tagger et Pousser une Image Docker vers Nexus

1. **Taguer une image** Docker avec la commande:

   ```sh
   docker tag alpine:3.21.2 localhost:8082/my-custom-alpine:3.21.2
   ```

2. **Pousser l'image vers Nexus** :

   ```sh
   docker push localhost:8082/my-custom-alpine:3.21.2
   ```

3. **Vérifier l'image dans Nexus** : Accédez à **http://localhost:8081** et allez dans **Repositories** → **docker-private** pour voir l'image poussée.

---

## 🔄 Étape 9 : Télécharger une Image depuis Nexus ou Docker Hub

### Pour télécharger une image depuis Docker Hub (via Nexus Proxy) :

```sh
docker pull localhost:8083/library/alpine:latest
```

### Pour télécharger une image depuis Nexus Docker Registry privé :

Avant de faire un **pull**, supprimez l'image localement pour tester :

```sh
docker rmi localhost:8082/my-custom-alpine:3.21.2
```

Pour télécharger l'image depuis Nexus :

```sh
docker pull localhost:8082/my-custom-alpine:3.21.2
```

Assurez-vous que le repository `docker-private` accepte les `pulls` anonymes.

---

## 🛠️ Troubleshooting

### 1. **Erreur 401 Unauthorized lors du login**

- Assurez-vous que le **"Docker Bearer Token Realm"** est activé dans les paramètres de sécurité de Nexus.
- Vérifiez que vous utilisez la bonne adresse `http://localhost:8082` et le bon mot de passe :

  ```sh
  docker login -u admin -p <mot_de_passe> http://localhost:8082
  ```

- Ajoutez `localhost:8082` et `localhost:8083` dans `daemon.json` comme "insecure registries" et redémarrez Docker.

### 2. **Erreur `denied: requested access to the resource is denied` lors du push**

- Assurez-vous que l'image est correctement taguée :

  ```sh
  docker tag <image_id> localhost:8082/my-custom-alpine:3.21.2
  ```

- Vérifiez que le repository Nexus accepte les `pushes`.

### 3. **Erreur lors du pull depuis Docker Hub Proxy**

- Assurez-vous que le proxy pour Docker Hub est bien configuré et que le tag est correct. Si nécessaire, utilisez `docker pull localhost:8083/library/alpine:latest`.

---

## 📋 Conclusion

Vous avez maintenant un Nexus Repository Manager configuré à la fois en tant que **Docker Registry privé** et **Proxy Docker Hub**, accessible via les ports `8082` et `8083`. Vous pouvez gérer vos images Docker en les **poussant** et **téléchargeant** depuis le repository Nexus, tout en accédant également aux images depuis Docker Hub via un proxy.

🎉 Profitez de votre gestion des images Docker avec Nexus ! 🎉
