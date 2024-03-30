# Workshop QR Code Generator

Ce projet est un atelier pour construire un générateur de codes QR fonctionnel. Il est conçu pour aider les participants à comprendre les principes de base de la génération de codes QR et à acquérir une expérience pratique de la programmation.

## Comment lancer le projet

1. Clonez le dépôt sur votre machine locale.

2. Naviguez jusqu'au dossier du projet avec `cd workshop-qrcode-generator`.

3. Créez un environnement virtuel et installez les dépendances
    
    ```bash
    python -m venv venv
    ```
    ```bash
    source venv/bin/activate
    ```
    ```bash
    pip install -r requirements.txt
    ```

4. Faites les migrations et lancez le serveur
    
    ```bash
    python manage.py migrate
    ```
    ```bash
    python manage.py runserver
    ```

## Comment contribuer

Nous accueillons les contributions de tous. Voici comment vous pouvez aider :

1. Fork le projet sur GitHub.

2. Clonez votre fork sur votre machine locale.

3. Créez une nouvelle branche pour votre fonctionnalité ou correction de bug.

4. Faites vos modifications dans cette branche.

5. Soumettez une pull request à partir de cette branche vers le dépôt original.

Nous examinerons et fusionnerons votre pull request dès que possible. Merci de contribuer à ce projet !