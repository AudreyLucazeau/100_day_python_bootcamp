import unidecode
import morse_decode

text_to_transmit = input("What is your message ? \n")

message= unidecode.unidecode(text_to_transmit)
message = message.upper()

morse_message = morse_decode.code_message(message)
morse_decode.read_message(morse_message)
