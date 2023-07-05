from kivy.app import App
from kivy.utils import platform
from plyer import gps
from plyer import sms
from kivymd.uix.dialog import MDDialog
#from android.permissions import Permission, request_permissions
from jnius import autoclass
from time import sleep

class Service(App):
    def __init__(self, recipient_number):
        number = open("number.txt", "r")
        read_number = number.read()
        number_str = str(read_number)
        self.recipient_number = number_str
        self.location_manager = None
    def run(self):
        self.start_location_updates()

#gps and getting info part
    def start_location_updates(self):
        activity = autoclass('org.kivy.android.PythonActivity').mActivity
        self.location_manager = activity.getSystemService('location')
        location_provider = self.location_manager.GPS_PROVIDER 
        self.location_manager.requestLocationUpdates(location_provider, 10000, 0, self.location_listener)

#send sms part
    def open_sms_failed_popup(self):
            dialog = MDDialog(title="Ошибка!", text="Не удалось отправить SMS")
            dialog.size_hint = [0.8, 0.8]
            dialog.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
            dialog.open()
    def send_sms(self, latitude, longtitude):
"""         last_known_location = self.location_manager.getLastKnownLocation(self.location_provider)
        if last_known_location:
            latitude = last_known_location.getLatitude()
            longtitude = last_known_location.getLongtitude()
        else:
            start_location_updates() """

        message = f"{latitude} {longtitude}"
        try:
            SmsManager = autoclass('android.telephony.SmsManager')
            sms_manager = SmsManager.getDefault()
            sms_manager.sendTextMessage(self.recipient_number, None, message)
        except Exception as e:
            open_sms_failed_popup()

class LocationListener:
    def __init__(self, location_service):
        self.location_service = location_service

    def onLocationChanged(self, location):
        latitude = location.getLatitude()
        longtitude = location.getLongtitude()
        self.location_service.send_sms(latitude, longtitude)