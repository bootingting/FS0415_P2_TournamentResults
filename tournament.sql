-- Table definitions for the tournament project.

-- Drop database if database exists
DROP DATABASE IF EXISTS tournament;

-- Create a database called tournament
CREATE DATABASE tournament;
\c tournament;

-- Create table called Players in the tournament database
-- Players table stores the name of players registered for the tournament
CREATE TABLE Players(id serial primary key, name text);


-- Create table called Matches in the tournament database
-- Matches table stores the matches played between two players 
-- Matches table also the winning record of each match

CREATE TABLE Matches(
id serial primary key, 
player1 serial references Players(id), 
player2 serial references Players(id), 
winner serial references Players(id)
);





