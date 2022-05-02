from typing import Dict, Text, Any, List

from rasa_sdk import Tracker
from rasa_sdk.events import EventType, AllSlotsReset
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormAction

from tools import DataBase


class ActionQueryAttribute(FormAction):
    def __init__(self):
        self.database = DataBase()

    def name(self):
        return 'action_query_attribute'

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """
        1. what is the cpu?
        2. what is the cpu of the 1.1.1.1
        3. what is the cpu of the server 1.1.1.1
        """
        entity_type = tracker.get_slot('entity')
        if entity_type is None:
            return []
        else:
            return ['ip']

    def attribute_generate_button(self, attribute_name):
        buttons = []
        same_atttribute_entities = self.database.get_sameAttributeEntities(attribute_name)
        for s in same_atttribute_entities:
            buttons.append({
                "title": "{}".format(s),
                "payload": '/query_attribute{{"entity":"{0}"}}'.format(s)
            })
        return buttons

    def ip_generate_button(self,ip):
        buttons = []
        entity_list = self.database.getEntityIp()
        for s in entity_list:
            buttons.append({
                "title":"{}".format(s),
                "payload":'/query_attribute{{"entity":"{0}","{1}":"{2}"}}'.format(s,'ip',ip)
            })
        return buttons

    def submit(
        self,
        dispatcher: "CollectingDispatcher",
        tracker: "Tracker",
        domain: Dict[Text, Any],
    ) -> List[EventType]:

        entity = tracker.get_slot('entity')
        attribute = tracker.get_slot('attribute')
        ip = tracker.get_slot('ip')
        if attribute is None:
            dispatcher.utter_template("utter_rephrase",tracker)
            return [AllSlotsReset()]
        if entity is None:
            if ip is None:#what is the cpu?
                buttons = self.attribute_generate_button(attribute)
                dispatcher.utter_button_message('please select the node you want to query:',buttons)
                return []
            else:#what is the cpu of 1.1.1.1?
                buttons = self.ip_generate_button(ip)
                dispatcher.utter_button_message('please select the node of the ip:',buttons)
                return []
        try:
            res = self.database.get_attribute(attribute,ip,entity)
            dispatcher.utter_message(
                f"{entity} {ip} {attribute} is: {res}"
            )
            return [AllSlotsReset()]
        except Exception as e:
            dispatcher.utter_message(template='utter_query_error')
            return [AllSlotsReset()]


class ActionQueryHost(FormAction):
    def __init__(self):
        self.database = DataBase()

    def name(self):
        return 'action_query_host_in'

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """
        1. what is the cpu?
        2. what is the cpu of the 1.1.1.1
        3. what is the cpu of the server 1.1.1.1
        """
        entity_type = tracker.get_slot('entity')
        if entity_type is None:
            return []
        else:
            return ['ip']

    def attribute_generate_button(self,attribute_name):
        buttons = []
        same_atttribute_entities = self.database.get_sameAttributeEntities(attribute_name)
        for s in same_atttribute_entities:
            buttons.append({
                "title":"{}".format(s),
                "payload":'/query_attribute{{"entity":"{0}"}}'.format(s)
            })
        return buttons

    def ip_generate_button(self,ip):
        buttons = []
        entity_list =self.database.getEntityIp()
        for s in entity_list:
            buttons.append({
                "title":"{}".format(s),
                "payload":'/query_attribute{{"entity":"{0}","{1}":"{2}"}}'.format(s,'ip',ip)
            })
        return buttons

    def submit(
        self,
        dispatcher: "CollectingDispatcher",
        tracker: "Tracker",
        domain: Dict[Text, Any],
    ) -> List[EventType]:

        entity = tracker.get_slot('entity')
        attribute = tracker.get_slot('attribute')
        ip = tracker.get_slot('ip')
        if attribute is None:
            dispatcher.utter_template("utter_rephrase",tracker)
            return [AllSlotsReset()]
        if entity is None:
            if ip is None:#what is the cpu?
                buttons = self.attribute_generate_button(attribute)
                dispatcher.utter_button_message('please select the node you want to query:',buttons)
                return []
            else:#what is the cpu of 1.1.1.1?
                buttons = self.ip_generate_button(ip)
                dispatcher.utter_button_message('please select the node of the ip:',buttons)
                return []
        try:
            res = self.database.get_attribute(attribute,ip,entity)
            dispatcher.utter_message(
                f"{entity} {ip} {attribute} is: {res}"
            )
            return [AllSlotsReset()]
        except Exception as e:
            dispatcher.utter_message(template='utter_query_error')
            return [AllSlotsReset()]


class ActionQueryConfiguration(FormAction):
    def __init__(self):
        self.database = DataBase()

    def name(self):
        return 'action_query_configuration_by'

    @staticmethod
    def required_slots(tracker: Tracker) -> List[Text]:
        """
        1. what is the cpu?
        2. what is the cpu of the 1.1.1.1
        3. what is the cpu of the server 1.1.1.1
        """
        entity_type = tracker.get_slot('entity')
        if entity_type is None:
            return []
        else:
            return ['ip']

    def attribute_generate_button(self,attribute_name):
        buttons = []
        same_atttribute_entities = self.database.get_sameAttributeEntities(attribute_name)
        for s in same_atttribute_entities:
            buttons.append({
                "title":"{}".format(s),
                "payload":'/query_attribute{{"entity":"{0}"}}'.format(s)
            })
        return buttons

    def ip_generate_button(self,ip):
        buttons = []
        entity_list = self.database.getEntityIp()
        for s in entity_list:
            buttons.append({
                "title":"{}".format(s),
                "payload":'/query_attribute{{"entity":"{0}","{1}":"{2}"}}'.format(s,'ip',ip)
            })
        return buttons

    def submit(
        self,
        dispatcher: "CollectingDispatcher",
        tracker: "Tracker",
        domain: Dict[Text, Any],
    ) -> List[EventType]:

        entity = tracker.get_slot('entity')
        attribute = tracker.get_slot('attribute')
        ip = tracker.get_slot('ip')
        if attribute is None:
            dispatcher.utter_template("utter_rephrase",tracker)
            return [AllSlotsReset()]
        if entity is None:
            if ip is None:#what is the cpu?
                buttons = self.attribute_generate_button(attribute)
                dispatcher.utter_button_message('please select the node you want to query:',buttons)
                return []
            else:#what is the cpu of 1.1.1.1?
                buttons = self.ip_generate_button(ip)
                dispatcher.utter_button_message('please select the node of the ip:',buttons)
                return []
        try:
            res = self.database.get_attribute(attribute,ip,entity)
            dispatcher.utter_message(
                f"{entity} {ip} {attribute} is: {res}"
            )
            return [AllSlotsReset()]
        except Exception as e:
            dispatcher.utter_message(template='utter_query_error')
            return [AllSlotsReset()]
