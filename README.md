# eterhoven_voting_app
Simple voting_app

The python script contained in this folder will execute a simple voting app, to choose between your favourite pet: dog, cat, or hamster.

Using the rule that each person can only vote once, voting is blocked once you make your choice. So, choose wisely! If you wish to cast a different vote, the script will need to be refreshed.

(The correct answer is DOG by the way. Choose any of the others, and the app will tell you what it thinks of your choice).

As this is simply a standalone python script, there is no storage attached. In a real-world environment, a script such as this would need to be deployed with attached storage, such as MySQL, to record all votes and display a total for each pet as new votes are cast. This could be within a Kubernetes cluster behind a Load Balancer and made available on the public web.

RUNNING THE PYTHON SCRIPT

The script can be run on your local machine once downloaded.
•	In a terminal or command prompt, navigate to the downloaded folder, or where you have saved the downloaded files. Now execute the following command:

python main2.py 

The script can be viewed online at the following link: 
https://replit.com/@eterhoven/votingapp?embed=1&output=1

DOCKER CONTAINER

The docker container for this app can be found at the following link:
•	https://hub.docker.com/r/uglyspud/voting_app

The following command will pull the image into your local repository of Docker images:
•	docker pull uglyspud/voting_app

Running the container would (theoretically) happen with:
•	docker run uglyspud/voting_app

Now, unfortunately, the issue:
As I used a GUI to design my python app, I was unable to find a way to display the GUI window within the app. I spent many hours and cups of coffee trying to find a solution, but none work. The issue seemingly lies with sharing the host PC’s display capabilities with the container, but I was unable to find a workable solution within the allotted timeframe ☹
For this same reason, I was unable to deploy my app on the public web using Flask, other than using the link provided above, which is a little slow and ungainly. It seems the GUI I used is not suited to this sort of use and resulted only in errors. I learnt this only after building the app. Another ☹

In closing, I enjoyed the learning experience, and I come away from the challenge better informed and educated.
I thank you for your time and wish you well,

Emil

