import requests

def get_location_from_ip(ip_address):
    try:
        url = f"https://ipinfo.io/{ip_address}"
        response = requests.get(url)
        data = response.json()

        params = ['country', 'city', 'region', 'loc']
        location = []
        for i in params:
            location.append(data.get(i, None))
        return location
    except Exception as e:
        return f"Ошибка при получении местоположения: {e}"

ip_address = "213.89.188.212"
location = get_location_from_ip(ip_address)

print(f"Местоположение для IP-адреса {ip_address}: {location}")
