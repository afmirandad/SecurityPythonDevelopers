import requests

class AttackDetector:
    def __init__(self, data):
        self.JsonData = []
        self.data = data


    def ApiCountriesByIpAddress(self):
        if not self.data:
            print("No hay datos para procesar.")
            return

        URI = "http://ip-api.com/json/"
        ip_seen = set()

        for ip, path, code in self.data:
            if ip in ip_seen:
                continue

            ip_seen.add(ip)
            formatData = {"ip": ip, "code": code, 'path':path}

            try:
                response = requests.get(f"{URI}{ip}").json()
                formatData["country"] = response.get("country")
                formatData["city"] = response.get("city")
            except Exception as e:
                formatData["country"] = None
                formatData["city"] = None

            self.JsonData.append(formatData)
        return self.JsonData