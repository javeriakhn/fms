Farm Management System (FMS)

Design Decisions

Home Page: No complex graphical images, a heading bar, a couple of links, and the date.
Mobs Page: The mobs page shows the list of mobs together with the paddock to which they belong. Next the data is retrieved from the database and then this data is sorted.
Paddocks Page: This page shows and emphasizes paddocks according to DM/ha. It evolves from blue to a ‘nuclear red’ depending on the data fed into the application.
Data Handling: POST requests are used for changes, for example moving mobs between paddocks or ones created via POST requests. This makes the data safe and eliminates problems related to GET requests.
Bootstrap: Tables as well as page formatting is achieved using Bootstrap in order to enhance on a professional look.
Image Sources

In this project it was not used any external images.

Database Questions

Create Mobs Table:
CREATE TABLE mobs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    paddock_id INT,
    FOREIGN KEY (paddock_id) REFERENCES paddocks(id)
);
Relationship Between Mobs and Paddocks:
Foreign key mobs.paddock_id associated with paddocks.id.

Create Farms Table:
CREATE TABLE farms (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(255),
    description TEXT,
    owner VARCHAR(255)
);

Insert Farm Data:
INSERT INTO farms (name, description, owner) VALUES ('Greenfield Farm', 'A large dairy farm', 'John Doe');

Changes to Other Tables:
New column which will be added to paddock table is going to be the farm_id to relate farms to paddock.