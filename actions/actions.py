# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"
# from databases import Database
from actions.data import DataUpdate
from typing import Any, Text, Dict, List, Union

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormValidationAction

#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
    

class ValidateBankForm(FormValidationAction):
    def name(self):
         return"validate_bank_form"
    
    # @staticmethod
    # def required_slots(tracker:"Tracker") -> List[Text]:
    #     return ["name", "Phone_number", "account_number",]
    
    def slot_mappings(self) -> Dict[Text, Union[Dict, List[Dict]]]:
         return {
            "name":[self.form_entity(entity="name")],
            "phone_number":[self.form_entity(entity="number")],
            "account_number":[self.form_entity(entity="number")],
            # "check_balance": [
            #     self.form_intent(intent="inform", value=True)
            # ],
        
        }
    
    @staticmethod
    def name_db() -> List[Text]:
        """ Database of name"""
        return[
            "hari",
            "maya",
            "sita",
            "cimran"
        ]
    
    
    @staticmethod
    def phone_number_db() -> List[Text]:
        """ Database of phone"""
        return[
            "9888888888",
            "9777777777",
            "9666666666",
            "9655555555"
        ]
    
    
    @staticmethod
    def account_number_db() -> List[Text]:
        """ Database of account"""
        return[
            "10000000",
            "12222222",
            "13333333",
            "14444444"
        ]
    
    @staticmethod
    def is_int(string: Text) -> bool:
        """Check if a string is an integer."""

        try:
            int(string)
            return True
        except ValueError:
            return False
        
    
    def validate_name(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
         """Validate name value."""

         if value.lower() in self.name_db():
            # validation succeeded, set the value of the "art_type" slot to value
            return {"name": value}
         else:
            dispatcher.utter_message(response="utter_wrong_name")
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return {"name": None}

    def validate_phone_number(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
         """Validate phone value."""

         if value.lower() in self.phone_number_db():
            # validation succeeded, set the value of the "art_type" slot to value
            return {"phone_number": value}
         else:
            dispatcher.utter_message(response="utter_wrong_phone")
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return {"phone_number": None}   


    def validate_account_number(
        self,
        value: Text,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any],
    ) -> Dict[Text, Any]:
         """Validate account value."""

         if value.lower() in self.account_number_db():
            # validation succeeded, set the value of the "art_type" slot to value
            return {"account_number": value}
         else:
            dispatcher.utter_message(response="utter_wrong_account")
            # validation failed, set this slot to None, meaning the
            # user will be asked for the slot again
            return {"account_number": None}          



    
    
    def submit(
        self,
        dispatcher: "CollectingDispatcher",
        tracker: "Tracker",
        domain: Dict[Text, Any],
    ) -> List[Dict]:
         
        
        dispatcher.utter_message(template="utter_balance_info")

        
        DataUpdate(tracker.get_slot("name"), tracker.get_slot("phone_number"), tracker.get_slot("account_number"))
        dispatcher.utter_message("Your response has been loaded.") 

        return []



