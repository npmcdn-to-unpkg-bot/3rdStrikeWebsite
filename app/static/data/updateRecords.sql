DROP TABLE IF EXISTS  `record`;
DROP TABLE IF EXISTS  `winRecord`;
DROP TABLE IF EXISTS  `lossRecord`;

CREATE TABLE `winRecord` AS
   SELECT
	matches.winnerID as playerID, 
	COUNT(matches.winnerID) as Wins
   FROM matchLog as matches
   GROUP BY matches.winnerID
   ORDER BY playerID ASC;
   
CREATE TABLE `lossRecord` AS
   SELECT
	matches.loserID as playerID, 
	COUNT(matches.loserID) as Losses
   FROM matchLog as matches
   GROUP BY matches.loserID
   ORDER BY playerID ASC;

CREATE TABLE `record` AS
	SELECT
	wins.playerID as playerID,
	wins.Wins as Wins,
	losses.Losses as Losses,
	wins.Wins - losses.Losses as record
   FROM winRecord as wins, lossRecord as losses
   GROUP BY wins.playerID;

   
DROP TABLE `winRecord`;
DROP TABLE `lossRecord`;