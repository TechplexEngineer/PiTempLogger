import hih6130
import thingspeak

data = hih6130.readSensor()

print data

thingspeak.sendData(data['tempc'], data['tempf'], data['humidity'])