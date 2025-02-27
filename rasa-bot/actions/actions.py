# from typing import Any, Text, Dict, List

# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher


# class ActionReservationTime(Action):

#     def name(self) -> Text:
#         return "action_reservation_time"

#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

#         # スロット "reserv_time" の値を取得
#         time = tracker.slots.get("reserv_time")  # .get()を使用して安全に取得

#         if time:
#             dispatcher.utter_message(text="{}に予約を完了しました！".format(time))
#         else:
#             dispatcher.utter_message(text="予約の時間が見つかりませんでした。")

#         return []
import random
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

class ActionTodayFortune(Action):
    def name(self) -> str:
        return "action_today_fortune"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict) -> list:
        fortunes = ["今日の運勢は大吉ねと", "今日の運勢は中吉ねと", "今日の運勢は小吉ねと"]
        fortune = random.choice(fortunes)
        dispatcher.utter_message(text=fortune)
        return []
