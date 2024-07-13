# rpi-zero-2w-setup
Setup for the transmitter pi

1. Create a file in the home directory called gnuradio

```
mkdir gnuradio
```

3. Put both python files in that folder

4. Run the script on startup

```
cd /etc/systemd/system
nano
```

paste this into nano

```
[Unit]
Description=Script to transmit when pi receives signal in

[Service]
ExecStart=/usr/bin/python3 /home/lab3/piTransmitWhenSignalIn.py

[Install]
WantedBy=multi-user.target
```

Save as transmitScript.service
then run

```
sudo systemctl start myscript    # Runs the script now
sudo systemctl enable myscript   # Sets the script to run every boot
```
