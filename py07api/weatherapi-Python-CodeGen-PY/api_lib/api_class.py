# Biblioteka z funkcjami zapisu i odczytu w plikach CSV | JSON | PICKLE |
import csv, json, pickle

class Weather:
    def __init__(self):
        self.response = []
        self.url = ''

    def read_apikey(self, file_name):
        '''metoda pobierająca klucz API z pliku'''
        if os.path.exists(file_name):
            with open(key_file) as file:
                for num in file:
                    return num.strip()
        else:
            return False

    def get_response(self, url_address, town):
        '''metoda pobierająca dane pogodowe z serwera (API)'''
        self.url = url_address
        querystring = {'q': town}
        headers = {
            'x-rapidapi-key': self.read_apikey(key_file),
            'x-rapidapi-host': 'community-open-weather-map.p.rapidapi.com'
        }
        self.response = requests.request(
            'GET', self.url, headers=headers, params=querystring).json()
        return self.response

    def save_forecast_json(self, file_name):
        '''metoda zapisująca dobowe dane pogodowe do pliku (JSON)'''
        with open(file_name, "w+", newline="", encoding='utf-8') as file:
            weather_json = json.dumps(self.response)
            file.write(weather_json)
        return True

    def collect_history(self):
        '''metoda zapisująca pobrane dane pogodowe w słowniku (JSON)'''
        for day in self.response['list']:
            date = datetime.utcfromtimestamp(day['dt']).strftime('%Y-%m-%d')
            forecast_hist = day['date']['forecast']
        return True

    @staticmethod
    def run(cmd):
        p = Popen(cmd, shell=True, stdout=PIPE)
        out, err = p.communicate()
        return (p.returncode, out, err)

    @staticmethod
    def install_requirements(file_name):
        '''funkcja pobierająca dane ze źródłowego pliku csv 'JSON' '''
        file_name = os.path.abspath(file_name)
        if os.path.exists(file_name):
            with open(file_name, 'r', newline='') as file:
                args = ['c:\windows\system32\cmd.exe', 'pip', 'install']
                read_file = file.readline().strip()
                for line in read_file:
                    args.append(line)
                    Popen(args)
            return True

'''
x = wfc.get_realtime_weather(q, lang)
x = wfc.get_history_weather(q, dt, unixdt, end_dt, unixend_dt, hour, lang)
x = wfc.get_forecast_weather(q, days, dt, unixdt, hour, lang)
'''