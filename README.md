# <h1 style="text-align:center">Bienvenue dans ce repo de DevOps</h1>

<div style="text-align:center">
<img src="img/cloud-service.gif" alt="drawing" style="width:400px; height:400px"/>

</div>


Nous avons mis en place un ensemble d'outils permettant la gestion d'une entreprise.Nous les listerons et vous indiquerons le nom de chaque dossier ou fichier contenant l'information dont on vous parlera.Nous avons 4 dossiers dans ce repo, un dossier:

- Applications
- Database
- Monitoring
- Proxy

  > `Rappelons que toutes les technos que nous utiliserons ici seront créés à par un "docker-compose" car notre objectif et d'apprendre et d'utiliser docker`

## Applications

Il contient les dossiers qui contiennent nos applications, dedans vous trouverez:

- Ghost: <img src="img/ghost.png" alt="drawing" style="width:30px; height:30px"/>Une plateforme de blogs gratuite et open source écrite en JavaScript <a style="text-decoration: underline; color:black"  href="https://hub.docker.com/_/ghost"> liens vers docker-hub</a>

- Gitea: <img src="img/tea.png" alt="drawing" style="width:30px; height:30px"/>Un service git en local que vous hebergez et manipulez comme une tasse de thé, <a style="text-decoration: underline; color:black"  href="https://docs.gitea.io/en-us/install-with-docker/"> documentation</a>

- Portainer: Un container qui monitor des conteneurs je vous mets le liens vers la doc 👉 <a style="text-decoration: underline; color:black" href="https://docs.portainer.io/v/ce-2.11/start/install/agent/docker/linux#deployment"> ici</a>

## Database

Dans ce dossier nous avons tou(e)s les serveurs et bases de données.

- MySQL: J'ai écris un article sur lui voici 👉 <a style="text-decoration: underline; color:black" href="https://soowcode.github.io/docker-mysql/"> le lien</a>
- Postgresql: À noté que dans 👉 <a style="text-decoration: underline; color:black" href="https://hub.docker.com/_/postgres"> docker hub </a> ils utilise adminer, mais moi j'utilise pgadmin4

- SQLSERVER: tutorial en cours mais je vous mets le lien vers 👉 <a style="text-decoration: underline; color:black" href="https://hub.docker.com/_/microsoft-mssql-server"> docker hub </a> ou le site de 👉 <a style="text-decoration: underline; color:black" href="https://docs.microsoft.com/en-us/sql/linux/quickstart-install-connect-docker?view=sql-server-ver15&pivots=cs1-bash"> microsoft</a>

## Monitoring

Dans ce dossier nous avons tout ce qu'il nous faut pour monitorer nos applications.
Pour le moment il contient prometheus, grafana, node-exporter, cadvisor.

- prometheus
- grafana
- node-exporter
- cadvisor

## Proxy

Dans le proxy nous avons mis: jwilder et nginx-proxy

.... to continue later....
