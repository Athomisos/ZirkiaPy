from sys import platform
import json, os, requests, time

class Application:
    def __init__(self, AppName, DisplayName, DevName):
        self.AppName = AppName
        self.DisplayName = DisplayName
        self.DevName = DevName
        self.UrlSSE3 = self.Get_Url()
        
    #--------------------------------------------------------------------------------------------
    #  Open a Json
    def Get_Json(self, PathToJson):
        with open(PathToJson) as json_file:
            data = json.load(json_file)
            return data

    #--------------------------------------------------------------------------------------------
    #  Get ip/port of Steelseries GameSence™
    def Get_Url(self):
        if(platform == "darwin"):
            PathToJson = "/Library/Application Support/SteelSeries Engine 3/coreProps.json"
        elif(platform == "win32"):
            PathToJson = "C:\ProgramData\SteelSeries\SteelSeries Engine 3\coreProps.json"
        else:
            raise NameError("OS not compatible") 
        data = self.Get_Json(PathToJson)
        Url = "http://"+data["address"]
        return  Url

    #--------------------------------------------------------------------------------------------
    #  Get ip/port of Steelseries GameSence™
    def Get_Encrypt_Url(self):
        if(platform == "darwin"):
            PathToJson = "/Library/Application Support/SteelSeries Engine 3/coreProps.json"
        elif(platform == "win32"):
            PathToJson = "C:\ProgramData\SteelSeries\SteelSeries Engine 3\coreProps.json"
        else:
            raise NameError("OS not compatible") 
        data = self.Get_Json(PathToJson)
        Url = "https://"+data["encrypted_address"]
        return  Url

    #--------------------------------------------------------------------------------------------
    #  Send json to Steelseries GameSence™ with a Post request
    def Post_Request(self, URL, Json):
        response = requests.post(URL, json=Json)
        return(response)

    #--------------------------------------------------------------------------------------------
    #  Register App
    def Register_GAME(self, TimerLength):
        UrlEngine = self.UrlSSE3
        Json = "{ "
        "\"game\": \""+self.AppName+"\","
        "\"game_display_name\": \""+self.DisplayName+"\","
        
        "\"developer\": \""+self.DevName+"\","
        "\"deinitialize_timer_length_ms\" : "+TimerLength+""
        "}"
        return(self.Post_Request(UrlEngine+"/game_metadata", Json))

    def Event_Register(self, EventName, MinValue, MaxValue, idIcon, Optional):
        Event_Json = "{"
        "\"game\": "+self.AppName+", \"event\": "+EventName+" , \"min_value\": "+MinValue+", \"max_value\": "+MaxValue+", \"icon_id\": "+idIcon+", \"value_optional\": "+Optional+"}"
        return(self.Post_Request(self.UrlSSE3+"/register_game_event", Event_Json))
