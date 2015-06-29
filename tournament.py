#!/usr/bin/env python
# 
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database.
    The database, Matches, consists of four columns.
    First column is the index, second column is the index of player1, referenced by Players database,
    third column is the index of player2, referenced by Players database
    and the fourth column is the index of the winner of the match, reference by Players database.
    Column index is unique serial id number for each match"""
    
    conn = connect()
    c = conn.cursor()
    c.execute("DELETE FROM Matches;")
    conn.commit()
    conn.close()


def deletePlayers():
    """Remove all the player records from the database.
    The database, Players, consists of two columns.
    First column is the index and second is the name of registered players.
    Column index is unique serial id number for each player"""
    
    conn = connect()
    c = conn.cursor()
    c.execute("DELETE FROM Players;")
    conn.commit()
    conn.close()

def countPlayers():
    """Returns the number of players currently registered in Players table.
    The database, Players, consists of two columns.
    First column is the index and second is the name of registered players.
    Column index is unique serial id number for each player"""
    
    conn = connect()
    c = conn.cursor()
    c.execute("SELECT COUNT(*) as num FROM Players;")
    for row in c:
     conn.commit()
     conn.close()
     return row[0]



def registerPlayer(name):
    """Adds a player to the tournament database.
    The database, Players, consists of two columns.
    First column is the index and second is the name of registered players
    
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
  
    Args:
      name: the player's full name (need not be unique).

    The players information is inserted into Players database.
    """
    conn = connect()
    c = conn.cursor()
    c.execute("INSERT INTO Players(name) VALUES ('"+name.replace("'", "''")+"');")
    conn.commit()
    conn.close()

def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.
    The database, Players, consists of two columns.
    First column is the index and second is the name of registered players

    The database, Matches, consists of four columns.
    First column is the index, second column is the index of player1, referenced by Players database,
    third column is the index of player2, referenced by Players database
    and the fourth column is the index of the winner of the match, reference by Players database.
    Column index is unique serial id number for each match
    
    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played

    The query counts the number of winners based on the id from the Mathes database,
    and references the id with the name from the Players table.
    All players are included in the return list, even if a player has not been registered in any matches.
    """
    conn = connect()
    c = conn.cursor()
    c.execute("SELECT Players.id as Id, Players.name as Name, COUNT(wincount.winner) as Wins, COUNT(matchcount.winner) as Games FROM Players LEFT JOIN Matches as wincount on wincount.winner = Players.id LEFT JOIN Matches as matchcount on (matchcount.player1 = Players.Id OR matchcount.player2 = Players.Id) GROUP BY Players.id, Players.name ORDER BY Wins DESC;")
    playerStanding = []
    for row in c:
        playerStanding.append(row)
    conn.commit()
    conn.close()
    return playerStanding


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    The database, Matches, consists of four columns.
    First column is the index, second column is the index of player1, referenced by Players database,
    third column is the index of player2, referenced by Players database
    and the fourth column is the index of the winner of the match, reference by Players database.
    Column index is unique serial id number for each match
    
    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost

    The match information is inserted in to the Matches database.
    """
    conn = connect()
    c = conn.cursor()
    c.execute("INSERT INTO Matches(player1, player2, winner) VALUES('"+str(winner)+"','"+str(loser)+"','"+str(winner)+"')");
    conn.commit()
    conn.close()
 
 
def swissPairings():
    """Returns a list of pairs of players for the next round of a match.
    
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
  
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name

    The query gets the player standing by calling playerStanding.
    The playerStanding function returns a list of the players and their win records,
    sorted by wins using database, Players and Matches.
    The database, Players, consists of two columns.
    First column is the index and second is the name of registered players

    The database, Matches, consists of four columns.
    First column is the index, second column is the index of player1, referenced by Players database,
    third column is the index of player2, referenced by Players database
    and the fourth column is the index of the winner of the match, reference by Players database.
    Column index is unique serial id number for each match
    
    The first entry in the list returned by playerStanding function should be the player in first place, or a player
    tied for first place if there is currently a tie.

    playerStanding function returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played

    The query counts the number of winners based on the id from the Mathes database,
    and references the id with the name from the Players table.
    All players are included in the return list, even if a player has not been registered in any matches.

    When the list is returned, the pairing result is obtained by pairing alternate players from player
    standings table, zipping them up and appending them to a list with values(id1, name, id2, name2)
    """
    count = 0
    pairing = []
    standings = playerStandings()
    for rank, player in enumerate(standings):
        if rank%2 == 0:
            for rank2, player2 in enumerate(standings):
                if rank2 == rank+1:
                  pairing.append((player[0],player[1],player2[0],player2[1]))
    return pairing




         

     


