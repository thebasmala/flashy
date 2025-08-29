from db import get_connection

##USERS TABLE##

#CREATE#
def create_user(username,password,email):
    conn= get_connection()
    cursor= conn.cursor()
    cursor.execute("INSERT INTO Users (Username,PasswordHash,email) VALUES (?,?,?)",(username,password,email) )
    conn.commit()
    cursor.close()
    conn.close()

#READ#
def get_user_by_id(user_id):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("SELECT*FROM Users WHERE UserID = ?", (user_id,))
    row= cursor.fetchone()
    conn.close()

    if row:
        columns = [column[0] for column in cursor.description]
        return dict(zip(columns, row))
    return None
    

#UPDATE#
def update_username(user_id, new_username):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("UPDATE USERS SET Username = ? WHERE UserID= ?",(new_username,user_id))
    conn.commit()
    conn.close()

#DELETE#
def delete_user(user_id):
    conn=get_connection()
    cursor= conn.cursor()
    cursor.execute("Delete FROM Users WHERE UserID=?",(user_id,))
    conn.commit()
    conn.close()

##DECKS TABLE##

#CREATE#
def create_deck(user_id,name):
    conn=get_connection()
    cursor= conn.cursor()
    cursor.execute("INSERT INTO Decks (UserID,DeckName) VALUES (?,?)",(user_id,name))
    conn.commit()
    conn.close()

#READ#
def get_deck_by_user(user_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Decks WHERE UserID = ?", (user_id,))
    rows = cursor.fetchall()
    conn.close()
    if rows:
        columns = [column[0] for column in cursor.description]
        return [dict(zip(columns, row)) for row in rows]  # list of dicts
    return []

#UPDATE#
def update_deck_name(deck_id,new_deck_name):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("UPDATE Decks SET DeckName = ? WHERE DeckID= ?",(new_deck_name,deck_id))
    conn.commit()
    conn.close()

#Delete#
def delete_deck(deck_id):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("DELETE FROM Decks WHERE DeckID= ?",(deck_id,))
    conn.commit()
    conn.close()


##CARDS##

#CREATE#
def create_card(deck_id,front,back):
    conn= get_connection()
    cursor= conn.cursor()
    cursor.execute("INSERT INTO Cards (DeckID,FrontText,BackText) VALUES(?,?,?)",(deck_id,front,back))
    conn.commit()
    conn.close()

#READ#
def get_cards_by_deck(deck_id):
    conn= get_connection()
    cursor= conn.cursor()
    cursor.execute("SELECT * FROM Cards WHERE DeckID = ?",(deck_id,))
    rows=cursor.fetchall()
    conn.close()
    if rows:
        columns = [column[0] for column in cursor.description]
        return [dict(zip(columns, row)) for row in rows]
    return []

#UPDATE#
def update_card(card_id,new_front,new_back):
    conn=get_connection()
    cursor=conn.cursor()
    cursor.execute("UPDATE Cards SET FrontText = ?, BackText= ? WHERE CARDID= ?",(new_front,new_back,card_id))
    conn.commit()
    conn.close()

# DELETE
def delete_card(card_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Cards WHERE CardID = ?", (card_id,))
    conn.commit()
    conn.close()
