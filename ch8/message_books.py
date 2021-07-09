from functions import display_message as dm, show_sent_messages, send_messages, favorite_book

message_list = ['Hey there Kyle', 'Where are you dad?', 'How was work mom?']
sent_messages = []

dm()


# To retain orig message list, send a copy to the function call with '[:]' notation
send_messages(message_list[:], sent_messages)
show_sent_messages(message_list, sent_messages)

favorite_book('The Lord of the Rings')
favorite_book('The Stand')
