#
# RAPID PROJECT MANAGEMENT
#
# Use:
#	- make start - to start server.
#	- make stop - to stop server.
#	- make restart - to restart server.
#	- make status - show server status.
#	- make kill - forced to kill the server processes (not recommended).
#

# SETTINGS
project = 'dlvpef'


# MAIN
all: start
runserver: start
start:
	sudo supervisorctl start $(project)

stop:
	sudo supervisorctl stop $(project)
	sh ./world/bin/killserver.sh

status:
	sudo supervisorctl status $(project)

forcekill: kill
kill:
	sh ./world/bin/killserver.sh

restart: stop start


# ADDITIONAL
forcestart:
	sh ./world/etc/init.d/runserver.sh

cleardebris:
	sh ./world/bin/cleardebris.sh

deployserver:
	sh ./world/bin/createconfigs.sh --production

deploylocal:
	sh ./world/bin/createconfigs.sh --develop
