# Security_Camera
A security camera project made using raspberry pi on python. Uses motion sensor to detect motion and turn on the camera to record videos.

I have used a PIR sensor, a buzzer and a raspi camera to make this project.

Whenever there is motion in the proximity of the PIR sensor it sends a command to the buzzer. The buzzer starts making sound and the camera starts recording the videos.

A notification is sent to the user via the MQTT app to notify them about potential dangers.
