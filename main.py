from models import *

#1.CREATE#
create_user("Test","testemail@gmail.com","test0330")
create_deck(1,"Turkish")
create_card(1,"merhaba","helloo")

#2.READ#
print(get_user_by_id(1))
print(get_deck_by_user(1))
print(get_cards_by_deck(1))

#3.UPDATE#
update_username(1, "test")
update_deck_name(1,"test deck")
update_card(1, "merhaba", "hello")

# 4. DELETE
# delete_card(1)
#delete_deck(1)
# delete_user(1)