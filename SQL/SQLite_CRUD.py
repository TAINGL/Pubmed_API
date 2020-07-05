"""
Mini projet API & SQL
1.Faire de CRUD operation avec sqlite en créant une base de donnée simplon avec une table apprenant avec comme colonnes : 
nom âge et hobbie => ceci va être votre snipet de SQLlite sur votre boostnote

### Mini projet
2. Récupérer Titre, abstract, pubmed_id, publication_date, keywords, journal, doi, dernier auteur (le plus a gauche) de différents articles (au moins 1000) scientifiques via l'api pubmed, avec la recherche par thématique en utilisant ""gene""
3. Utiliser pandas pour  séparer les données afin de les mettre dans plusieurs tables d'une base de donnée que vous allez appeler pubmed (en faisant noramlizant vos données).
4. Faire des requêtes SQL :
      - pour récupérer les abstracts des auteurs ayant au moins publiés deux fois.
      - pour récupérer un classement des journaux scientifiques par rapport aux nombres d'articles publiés
      - pour récupérer le nombre d'articles publiés par an
"""

"""
CRU operation avec SQLite
https://www.tutorialsteacher.com/python/database-crud-operation-in-python
https://www.tutorialspoint.com/sqlite/sqlite_create_table.htm

Create A New Database:
sqlite3 simplon.db

This will create a new database named "simplon.db".

CREATE TABLE Apprenant(
  Id INTEGER PRIMARY KEY AUTOINCREMENT,
  FirstName TEXT NOT NULL,
  LastName TEXT NOT NULL,
  Age NUMERIC NOT NULL,
  Hobbie TEXT
);

INSERT INTO Apprenant (FirstName, LastName, Age, Hobbie)
VALUES ('Céline','DUMEZ', 30, 'Danse');  
 

SELECT * FROM Apprenant;

INSERT INTO Apprenant (FirstName, LastName, Age, Hobbie)
VALUES ('Lydia','HIBA', 25, 'Nature');  

UPDATE Apprenant
SET Hobbie = 'Santé'
WHERE Hobbie = 'Nature';

INSERT INTO Apprenant (FirstName, LastName, Age, Hobbie)
VALUES ('Bintou','KOITA', 30, 'Economie');  

DELETE FROM Apprenant
WHERE LastName = 'KOITA';

.schema
.tables
.databases
.open nomdedb.db
.quit
.help
"""
# Database CRUD Operations in Python
# Create : créer, Read : lire, Update : mettre à jour, Delete : supprimer

import sqlite3
db=sqlite3.connect('Apprenant.db') 

# Python DB-API

try:
    cur=db.cursor() # Returns a Cursor object which uses this Connection. 
    cur.execute("Query")
    db.commit()
    print ("success message")
except:
    print ("error")
    db.rollback()
db.close()

# Create a New Table

try:        
    cur =db.cursor()
    cur.execute('''CREATE TABLE Apprenant (
    Id INTEGER PRIMARY KEY AUTOINCREMENT,
    FirstName TEXT NOT NULL,
    LastName TEXT NOT NULL,
    Age NUMERIC NOT NULL,
    Hobbie TEXT);''')
    print ('table created successfully')
except:
    print ('error in operation')
    db.rollback()
db.close()
