-- Table definitions for the tournament project.
-- Players table stores the name of players registered for the tournament
-- Matches table stores the matches played between two players and also the winning record of each match

CREATE DATABASE tournament;
\c tournament;

CREATE TABLE Players(id serial primary key, name text);
CREATE TABLE Matches(id serial primary key, player1 serial references Players(id), player2 serial references Players(id), winner serial references Players(id));





