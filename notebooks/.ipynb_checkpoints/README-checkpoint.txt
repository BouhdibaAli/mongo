Ali Bouhdiba
Projet noSQL Redis : Acteurs et Films
Ce projet utilise Redis avec Python et Docker pour explorer un dataset d'acteurs et de films.

Objectif

- Charger les données Redis avec Docker
- Interroger Redis depuis Jupyter Notebook
- Automatiser certaines analyses via un script Python

LE script automatise 3 tâches:

- Nombre d'acteurs dont le nom commence par P -> LIKE 'P%' sur last_name
- Films après 2010 avec > 100k votes -> WHERE release_year > 2010 AND votes > 100000
- Top 1 film par genre -> Pour chaque genre, selection du rating le plus eleve, stocke dans une hash top_movies_by_genre

