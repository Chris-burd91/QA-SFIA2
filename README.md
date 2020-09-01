# QA-SFIA2
Magic 8-Ball Application

### Links:
* JiraBoard : https://qaproject12.atlassian.net/jira/software/projects/QAS/boards/4/roadmap?selectedIssue=QAS-8
* Github : https://github.com/Chris-burd91/QA-SFIA2

### Introduction:
In this project we were tasked to design a webapp with at the core of it to generate "Objects". I chose to create a Magic 8 Ball app to randomly generate a anwser to a question the user may ask. We were requires to make it so that we have at least 4 services work together to make the app itself, with a database implemented into it.

### Magic 8-Ball App:
The design of the application is as follows:
* Service 1 is the front-end of the app as well as where all my other services communicate with one another.
* Service 2 is where my random number generator is which picks a random object out of List which could be an Integer or a String.
* Service 3 is where my Dictionary is which contains the value for the answer which is to be displayed on the front end.
* Service 4 is where services 2 & 3's objects come into to produce the value of the answer which is sent back to service 1.

### The Technologies used:
* GCP - Google Cloud Platform
* Python 
* Flask
* Jira
* Git/Github
* Docker
* Docker Compose
* Docker Swarm
* NGINX
* Ansible
* Jenkins

### Google Cloud Platform:
I used 3 Virtual Machines for my app where I used mainly 1 for designing the app and holding most dependencies onto. Using a Cloud Platform not only was benficial as not to clutter up my system but it is also fast and light, Easily Accessible and if there were any issues there would be a good amount of support behind most issues that arise.

### Python:
This is the programming language that was used for the base logic and back-end logic for the app itself, being able to use lists or dictionaries to store information and with the JSON(JavaScript Object Notation) format, I was able to send data in the form of dictionaries through my different services.

### Flask:
This is the micro-framwork that we used to be able to launch the webapp, its very simple and light and allows us to make web applications and extensive in functionality due to the variety of modules it can incoperate.

### Jira:
This is the planning board I used along with my project to make use of the agile framework and that my objectives were completed in an agile way. This made it visually clear what tasks were needed to be done and also recording and updating tasks when changed or completed to show the scale of completeness in the project.

### Git/Github:
This is a very important software that we've come to here. This is Version Control System that allows us to push our code to a repository of our choosing on any 'branch' we choose to depending on what we are working on and why we would need to seperate our working code to our development code. We push our code we want to store to github which is our version control management system and allows us to do alot of things, mainly store it but we can also provide a webhook and have it integrate with Jenkins and this will be important for the project as to automate building through just changes in code.

### Docker:
This is a containerisation tool we use to be able to launch our applications on any system depending it has docker installed. This is important as it sets up the environment we need to allow our application to run, and these environments are kept consistent as they run and you can make changes to the code without the performance of the app being effected at all, there are many benifits to containers but the fact they're very quick and they can run on any operating system that has docker provides big advantages.

### Docker Compose:
This allowed me to run multiple containers using a configuration file which made the process of launching each app itself much easier and alot more efficient due to the fact it improves the CI workflow and automation of my app.

### Docker Swarm:
This is the orchestration tool used to gather docker containers onto different nodes(machines, servers, etc) which we can deploy these programs to many machines if we wanted too. In my project I had 1 manager node and 2 worker nodes which shared the containers between one another.

### NGINX:
This is a web server itself but I used it mainly as a reverse proxy, which handled all traffic and requests through itself before being sent to the application. This is benficial as people who access this application do not have "direct" access to it, so its better for security purposes.

### Ansible:
I used an Ansible Playbook to configure the nodes for this project to install dependencies and docker to my VM's, as well as having the playbook start a docker swarm and have the workers connect to the manager node through this playbook. This is very handy as we could use this to spin up loads of nodes at once and have them configured in the desired state of our choosing.

### Jenkins:
This is the center of our continuous intergration/ delievery, we use jenkins to build our projects and deploy them and we do this through automation of all previous technologies discussed. We use a jenkins file then runs commmands to start our machines to fully deploy the application. With a github webhook, jenkins will build a project just from changes in the source code, which is something I will be demonstrating in the presentation. This is handy for Developers as they can fix code and make changes that have been fully tested to deploy without it being a manual deployment.

### Testing:
* Service 1: 100% coverage in Unit Test with 2/2 tests passed, I was testing that TestView of the home made and the TestView of the second page in which it generates an object. This includes the database being tested with a test database, we tested for this because we wanted to check that the functionality of any user could check these pages which would give a response code of 200.
* Service 2 & 3: These were simple tests, just getting a response out of these services was enought to get 100% converage on both and we did this to test we actually get a responce from these individual API's
* Service 4: Unfortunatly I was unable to get my tests to pass in this service as I was gettig a type error of none type so I do not believe an object was giving me the response I wanted. I got up to 92% coverage on this test but 7/8 failed. It would of properly tested the functionality of the app as this is where the logic is defined truely. 
