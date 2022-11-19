# 2. Change the end date of a featured exhibition

select * from exhibition
where ExhibitionType = 'featured';

update exhibition 
set EndDate ='2022-07-04'
where ExhibitionID = 1;

select * from exhibition
where ExhibitionType = 'featured';
