from flask import Flask, render_template, jsonify

app = Flask(__name__)

class Led:
    def __init__(self, red, green, blue, isLedOn):
        self.red = red
        self.green = green
        self.blue = blue
        self.isLedOn = isLedOn

class Dht:
    def __init__(self, temperature, object_temperature, humidity, object_humidity):
        self.temperature = temperature
        self.object_temperature = object_temperature
        self.humidity = humidity
        self.object_humidity = object_humidity

# 예제 데이터
kitchen_led = Led(255, 0, 0, True)  # 켜짐
living_room_led = Led(255, 0, 0, False)  # 꺼짐
bedroom_led = Led(0, 0, 255, True)  # 켜짐
dht = Dht(22, 24, 45, 50)  # 현재 및 목표 온도/습도

@app.route('/')
def index():
    return render_template('rasp_index.html')

# 실시간 데이터 반환
@app.route('/data')
def get_data():
    data = {
        'kitchen_led': vars(kitchen_led),
        'living_room_led': vars(living_room_led),
        'bedroom_led': vars(bedroom_led),
        'dht': vars(dht)
    }
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True, host="172.21.0.67")