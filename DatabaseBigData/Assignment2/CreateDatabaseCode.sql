create table Artist(
ArtistID int primary key,
FName varchar(20) ,
LName varchar(20) ,
DOB date ,
DOD date
);

create table ArtObject(
ArtObjID integer primary key,
ArtistID integer references Artist(ArtistID),
CreationYear date , 
Title varchar(20) ,
Description varchar(100) ,
Country varchar(20) ,
Epoch varchar(20) ,
DateAcquired date ,
Cost float ,
Status varchar(20) ,
ArtType varchar(20) 
);

create table Staff(
StaffID int primary key,
FName varchar(20) ,
LName varchar(20) ,
Position varchar(20) 
);

create table ArtCurator(
ArtObjID int primary key references ArtObject(ArtObjID),
StaffID int references Staff(StaffID)
);

create table Painting(
ArtObjID int primary key references ArtObject(ArtObjID),
PaintingType varchar(20) ,
Material varchar(20) ,
Style varchar(20) 
);

create table StatueSculpture(
ArtObjID integer references ArtObject(ArtObjID),
Material varchar(20) ,
Height float ,
Weight float ,
Style varchar(20) 
);

create table Other(
ArtObjID int primary key references ArtObject(ArtObjID),
OtherType varchar(20) ,
Style varchar(20) 
);

create table Exhibition(
ExhibitionID int primary key,
Name varchar(20) ,
ExhibitionType varchar(20) ,
Description varchar(20) ,
StartDate date ,
EndDate date 
);

create table ExhibitionSupervisor(
ExhibitionID int primary key references Exhibition(ExhibitionID) ,
StaffID integer references Staff(StaffID) 
);

create table ArtsFriendsCircle(
MuseumName varchar(20) primary key, 
Description varchar(20) ,
Street varchar(20) ,
City varchar(20) ,
Postcode varchar(20) ,
PhoneNo varchar(20) ,
ContactName varchar(20) 
);

create table ArtObjectBorrowed(
  ArtObjectBurrowedId int primary key,
  ArtObjID integer references ArtObject(ArtObjID) ,
  BorrowedDate date ,
  RetrunDate date 
);

create table ExhibitionDetail(
  ExhibitionDetailID int primary key,
  ExhibitionID int references Exhibition(ExhibitionID),
  ArtObjID int references ArtObject(ArtObjID) 
);

create table LoyalVistor(
FName varchar(20) ,
LName varchar(20) ,
LoyaltyNo integer primary key,
PhoneNo varchar(20) ,
Street varchar(20) ,
City varchar(20) ,
Postcode varchar(20) ,
Preferences varchar(20) 
);
