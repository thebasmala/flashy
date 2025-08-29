from fastapi import FastAPI
import models


app= FastAPI()


@app.get("/")
async def root():
    return {"message": "home"}


# USERS
@app.post("/users/")
def create_theuser(username: str, password: str, email:str):
    models.create_user(username,password,email)
    return {"message":"user created successfully"}

@app.get("/users/{user_id}")
def read_user(user_id: int):
    user= models.get_user_by_id(user_id)
    return {"user":user}

@app.put("/users/{user_id}")
def update_username(user_id:int, new_username:str):
    models.update_username(user_id,new_username)
    return {"message":"username updated successfully"}

@app.delete("/users/{user_id}")
def delete_user(user_id:int):
    models.delete_user(user_id)
    return {"message":"user deleted successfully"}



# DECKS
@app.post("/decks")
def create_deck(user_id:int, name:str):
    models.create_deck(user_id,name)
    return{"message":"Deck created successfully"}

@app.get("/decks/{user_id}")
def read_decks(user_id:int):
    decks= models.get_deck_by_user(user_id)
    return {"decks":decks}

@app.put("/decks/{deck_id}")
def update_deck_name(deck_id: int,new_deck_name: int):
    models.update_deck_name(deck_id,new_deck_name)
    return {"message": "Deck updated successfully"}

@app.delete("/decks/{deck_id}")
def delete_deck(deck_id: int):
    models.delete_deck(deck_id)
    return {"message": "deck deleted successfully"}

#CARDS
@app.post("/cards/")
def creat_card(deck_id:int, front: str, back:str):
    models.create_card(deck_id,front,back)
    return {"message": "card created successfully"}

@app.get("/cards/{deck_id}")
def get_cards_by_deck(deck_id:int):
    cards= models.get_cards_by_deck(deck_id)
    return {"cards": cards}


@app.put("/cards/{card_id}")
def update_card(card_id: int, new_front: str, new_back: str):
    models.update_card(card_id, new_front, new_back)
    return {"message": "Card updated successfully"}

@app.delete("/cards/{card_id}")
def delete_card(card_id: int):
    models.delete_card(card_id)
    return {"message": "Card deleted successfully"}
