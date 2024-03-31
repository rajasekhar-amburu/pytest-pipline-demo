Install Docker Desktop / Engine on your local machine.
Run this command: docker run -p 8080:8080 -p 50000:50000 -v jenkins_home:/var/jenkins_home jenkins/jenkins:lts-jdk11
Write down the password that's created for you during this first time set up process: like <<password>>
Go to localhost:8080 and enter the password

Enter the 'docker ps' to see what containers are running - Copy the container id
Connect to the container bash using the container id.
> docker exec -it -u 0 dcbcc31e91c2 /bin/bash

1. root@dcbcc31e91c2:/# apt-get update
2. root@dcbcc31e91c2:/# apt-get install python3
3. root@dcbcc31e91c2:/# apt-get install python3-pip
4. root@dcbcc31e91c2:/# apt install python3-pytest


You can do the git configs as below
1. Create a git repo
2. Do git clone :  git clone https://github.com/rajasekhar-amburu/pytest-pipline-demo.git
3. git add <files.py>
4. git commit -m <commit-message>
5. git push

Refer the Jenkins file and configure the pipeline script
Save and Run the pipeline -> 'Build Now'
