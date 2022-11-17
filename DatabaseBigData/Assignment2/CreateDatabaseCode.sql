create table Artist(
ArtistID integer primary key,
FName varchar(20),
LName varchar(20),
DOB date,
DOD date
);

create table ArtObject(
ArtObjID integer primary key,
ArtistID integer references Artist(ArtistID),
CreationYear date, # Can use Year(CreationYear) in the future to select sth.
Title varchar(20),
Description varchar(30),
Country varchar(20),
Epoch varchar(20),
DateAcquired date,
Cost float,
Status varchar(20),
ArtType varchar(20)
);

create table Staff(
StaffID integer primary key,
FName varchar(20),
LName varchar(20),
Position varchar(20)
);

create table ArtCurator(
ArtObjID integer references ArtObject(ArtObjID),
StaffID integer references staff(StaffID)
);

create table Painting(
ArtObjID integer references ArtObject(ArtObjID),
Type varchar(20),
Material varchar(20),
Style varchar(20)
);

create table StatueSculpture(
ArtObjID integer references ArtObject(ArtObjID),
Material varchar(20),
Height float,
Weight float,
Style varchar(20)
);

create table Other(
ArtObjID integer references ArtObject(ArtObjID),
Type varchar(20),
Style varchar(20)
);

create table Exhibition(
ExhibitionID integer primary key,
Name varchar(20),
Type varchar(20),
Description varchar(20),
StartDate date,
EndDate date
);

create table ExhibitionSupervisor(
ExhibitionID integer references Exhibition(ExhibitionID),
StaffID integer references Staff(StaffID)
);

create table ArtsFriendsCircle(
MuseumName varchar(20) primary key, #There are some troubles.
Description varchar(20),
Street varchar(20),
City varchar(20),
Postcode varchar(20),
PhoneNo varchar(20),
ContactName varchar(20)
);

create table ExhibitionDetail(
ExhibitionID integer references Exhibition(ExhibitionID),
ArtObjID integer references ArtObject(ArtObjID)
);

create table LoyalVistor(
FName varchar(20),
LName varchar(20),
LoyaltyNo integer primary key,
PhoneNo varchar(20),
Street varchar(20),
City varchar(20),
Postcode varchar(20),
Preferences varchar(20)
);
