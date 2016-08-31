.open database.sqlite
.separator ','
CREATE TABLE `temp` (
	`p1`	TEXT,
	`p2`	TEXT,
	`char1`	TEXT,
	`char2`	TEXT,
	`eventID`	TEXT,
	`winnerID`	TEXT,
	`loserID`	TEXT,
	`date`	TEXT,
	`league`	TEXT
);
.import "static/data/Match_Log.csv" temp
INSERT INTO matchLog(p1,p2,char1,char2,eventID,winnerID,loserID, date, league) SELECT * FROM temp;
DROP TABLE `temp`;