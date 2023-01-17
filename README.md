# MICS_W295_Docker_POC
Docker POC to show teammates how to use docker

# Running the python hello world script
You can run the script in a python environment (3.9.16) no matter your OS or the version installed locally (or the absence thereof). You might get a warning running it on a Windows host but that's OK.
You can run this application without having a local installation of mongodb, that's the magic about containers
use the following commands:

first:

```docker-compose up```

Look at the output, you should see that there is only one name in the database. Close the application with ctrl+c
run the application again with the same command

```docker-compose up```

Notice that the first name is still there but that a second name has been added to the database.

If you modify the script, be sure to force a re-build of the container when using docker-compose:

```docker-compose up --force-recreate --build```

You can open a new terminal and use a local mongo client to interact directly with the database. For simplcity, the database has been setup without authentication so you can simply connect on localhost on port 27017.
Not that this mongo-client could be in a container but it's not the case here this is simply to demonstrate how two container (a python application and a database) can interact.

Have fun !