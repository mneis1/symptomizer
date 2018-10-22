# Symptomizer

## Inspiration
Our group wanted to create a project where people could benefit from advice and guidance as to whether or not they may need to access health care, while having the ability to get a very quick idea of what may be ailing them. We wanted this to be accessible in a very interactive and informative context.

## What it does
Our hack uses a symptom and disease dataset and using the data we found we were able to estimate with good probability what diagnosis the patient may receive if they go for a doctor. This system could also be used for healthcare professional to provide a more accurate and thorough diagnosis that complements the doctor's professional opinion.

The user can use our system from a website or through the google home device by saying "Hey Google, talk to sympomizer." From there, the symptoms are sent to the backend to be matched against potential ailments via logistic regression machine learning. Finally, the information gleaned from the user's input is presented back to the user and the user is given the chance to follow up on the information by taking treatment actions.


## How we built it
We hosted our services using Amazon Web Services and the Google Cloud Platform for the Google home app. The identification of potential diseases takes place on a python Flask backend where we predict using a trained linear regression model.



## What we learned
Stuart learned how to make his own Google Assistant application via DialogFlow, a tool we had never built with until this weekend. It is a particularly fun tool to build with because you can talk and interact with your creation on any compatible Google hardware that is linked to your Google account. 

James learned new libraries in Javascript in a short period of time. He also learned how to make Ajax requests and build dynamic webpages using Ajax. 

Joe learned how to create new endpoints using Python flask as well as fulfilling requests from services such as the Google Cloud.

Marc learned how to use statistical learning to implement a linear regression algorithm (machine learning) with scikit-learn.

## What's next for Symptomizer
Symptomizer could integrate with doctors offices and train on anonymized patient data to further correlate diseases in symptoms.
