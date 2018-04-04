# ThingaMaDashboardImporter
This is a Python 2.7.8 project that allows the import of data from Observium through their API and then places it in InfluxDB.

I am currently using this to support a Grafana dashboard at my workplace. Observium's API still has a lot of other types of data which could be derived from it. This iteration of the project simply includes what I needed for the initial dashboard I created. We use a mash up of Zabbix and Observium to monitor our systems. So I have a Grafana board consisting of server status taken from Zabbix using Alexander Zobnin's awesome plugin. Check it out it is on Git Hub, and network stats from the InfluxDB data source which I supplied data through the Observium API using my Python project here. 

THE COMPLETE PROJECT WITH PYTHON VIRTUAL ENVIRONMENT AND ALL ITS REQUIRED LIBRARIES IS IN THE Observer.zip file.
  You can unzip and import to PyCharmCE and make custom changes. *(YOU WILL HAVE TO MAKE CHANGES TO SOME OF THE CONSTANTS IN THE data.py FILE)*
  Or unzip where you need to run it call the main.py file.
  don't forget to call using the complete path from wherever you call it. I.E. Python /thisuser/Observer/main.py.
  On some redhat editions you may even have to specify Python2.7.8 then the filepath.
