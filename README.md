## GetOutside Django Backend, Nextjs Project
Projekt WiSe 2022/2023
Gruppe: Cherrytomaten

## Table of Contents
1. [Ziele des Projekts](#ziele-des-projekts)
2. [Autoren](#autoren)
3. [Installation](#installation)
4. [Start](#start-des-projekts)
5. [Abhängigkeiten](#abhängigkeiten)
6. [Tools](#tools)


## Ziele des Projekts
Web-Applikation zum Thema (Outdoor)-Sport
Funktionen:
   • Markierung von Orten auf einer Map
   • Finden von neuen Mitspielern (durch Chat/ Kommentarfunktion)
   • (Live tracking, ob der Ort voll ist)
   • (Verbesserung durch Videoanalyse)
zusätzliche Funktionen können, wenn die Zeit reicht, noch hinzugefügt werden

## Autoren
Lilian Alice Drabinski, Josefine Hoppe, Emilia Dörschmann, Adham Elgendy, Marlon Kerth, Leon Pester

## Installation
A little intro about the installation.

> `git clone https://github.com/Cherrytomaten/getOutside_backend.git`
> `cd ../path/to/the/file`

## Start des Projekts


1. Virtual Environment. Einen Ordner für virtual Environment anlegen. 
Entweder per Console:  
> `python -m venv venv`  

Oder per Settings der IDE. Je nach IDE variiert der Pfad. Zum Beispiel unter getOutside_backend oder getOutside_backend/Backend "venv" anlegen.

2. Dann virtual Environment activieren mit:  
> `python venv\Scripts\activate`  

wenn das nicht funktioniert, kann es helfen mit cd in den Ordner Scripts zu wechsel und so zu aktivieren:  
> `python . activate` (Leerzeichen ist wichtig)

3. Abhängikeiten installieren  
> `pip install -r ./requirements.txt`

5. to make sure all migrations are correct:  
> `python manage.py makemigrations` 
> `python manage.py migrate` 

5. Server starten   
> `python manage.py runserver`

## Abhängigkeiten
Alle Abhängigkeiten werden beim Starten des Projekts mit den requirements installiert. 


## Tools
Tools, die wir im Backend verwendet haben sind: 

   - Python (Programmiersprache)
   - Django Rest Framework (Webframework mit Model-View-Presenter Schema)
   - SQLite Datenbank im develop Branch (Programmbibliothek mit einem relationalen Datenbanksystem)
   - PostgreSQL im main Branch (Objektorientiertes Datenbankmanagementsystem)
   - git (GitHub, Versionskontrolle)
   - HTTPie, cURL (Programmbibliothek und ein Kommandozeilen-Programm (CLI) zum Testen) 
   - pytest (Test Framework)