# RASA-NormalBank-Bot
#The Project Involves:

Classifying the user intent related to checking balance, transaction history and some basic intents like greet and goodbye.
Identifying entities such as account number, name, phone number.

Based on the values extracted by entities store it in slot and if the value matches with the values is in db (you can just add a small dictionary for that) then show a basic response, with the slot value example: {Dear {name} your {account number} has a balance of Rs. 1000}.
