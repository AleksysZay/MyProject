use master 
create database WSAppDB

use WSAppDB

create table [User](
	ID_User int identity,
	[Name] nvarchar(30),
	DateOfBirth date,
	Age int,
	NumberPhone nvarchar(13),
	[Login] nvarchar(10) unique,
	[Password] nvarchar(10) unique,
	[Status] nvarchar(20),
	Primary key (ID_User)
);

create table Vacancy(
	ID_Vacancy int identity,
	ID_User int,
	[Description] nvarchar(30),
	Primary key (ID_Vacancy),
	Foreign key(ID_User) references [User](ID_User)
);

create table ListOfVacancies(
	ID_Vacancy int,
	ID_User int,
	Foreign key(ID_Vacancy) references Vacancy(ID_Vacancy),
	Foreign key(ID_User) references [User](ID_User)
);