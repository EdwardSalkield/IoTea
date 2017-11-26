# IoTea
The IoT automated tea brewer!
The result of blood, crying, internal pain and suffering, a dead dragonboard, and a surprising lack of tea.

The codebase is outlined as follows:
server - nginx config files
       - web front end, organised according to the config
pi     - monitors and encodes the temperature sensor signal
piw0   - the code for the pi zero, which listens to the web server for updates regarding new cups of tea to make
