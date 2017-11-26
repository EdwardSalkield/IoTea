# IoTea
The IoT automated tea brewer!
The result of blood, crying, internal pain and suffering, a dead dragonboard, and a surprising lack of tea.

The codebase is outlined as follows:
pi contains the script used to monitor and encode the temperature sensor signal
piw0 contains the code for the pi zero, which listens to the web server for updates regarding new cups of tea to male
server contains the nginx config files, and also all of the web frontend, organised according to the config.
