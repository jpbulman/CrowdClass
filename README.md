# CrowdClass
The idea of this is to be a crowd sourcing web app that gets training data for a machine learning program; we built this as our WPI hackathon project.
## Cookies
The goal of this project is to have a survey that can ask about any number of things, but to keep it simple we started with one idea: cookies. The survey simply shows you two cookies, and then asks you to determine whether each is a chocolate chip or an oatmeal raisin cookie. The survey randomly chooses one cookie to be a already known value, to determine whether the user is likely going to be entering data correctly instead of maliciously. The other cookie is an unknown one however, so if the user gets the known cookie correct, their response for the other one is recorded. Then the survey would (this part is not fully implemented) send this information to a database to record which type of cookie it is. Every so often, the data would be ripped from the database into a CSV in which would be used as training data.
## Scaling
Although this idea is simple, the purpose is to show this could be scaled up to any number of topics given the time and effort. The purpose is to have a simple way to get data from users that can easily be made into training data so a program can easily learn certain trends in the data.
## Under The Hood
The machine learning program for this example was made using Google's Tensor Flow and the database was started in Google Cloud Platform (GPC).
