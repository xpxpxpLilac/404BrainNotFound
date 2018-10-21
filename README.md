# 404BrainNotFound
Data source: European Soccer Database (https://www.kaggle.com/hugomathien/soccer)

Description of scenario:
Extracting the database from FIFA and using various data to do data analyze and data processing and then make prediction
of two teams through some team attributes.  

Details:
•	Machine Learning
ml.py uploaded in github is used for our evaluation initially. It could be seen the accuracy of various model predictions. 
We choose the most accuracy one called LogisticRegression. So we establish the machine learning is based on the LogisticRegression machine learning model. This model is built after loading data into the database at the Back End. We will wait the request. If we 
receive the post request we could receive data from paylode and do machine learning then return the response with prediction result.

•	Front End (Home page, Sign in page, Log in page, Dashboard(Predict page), Result page)
We need to Log in at Home page. If you don’t have the account it will switch to the Sign up page to fill some information and then
submit the information. You could switch to Log in page after submission your personal information. You could get into Dashboard when
log in successfully. Dashboard is the main page with the Predict button which could fill in eight team attributes. After pushing the 
Predict button it will switch to the final page which show the result of the prediction with some relative charts. You can push the 
Save button to save the result in the database. If not the result could not be recorded and will return to the Predict page.
There are three buttons on the Navigation Bar: Home, Prediction, History. It is easily to understand when you push Prediction button 
it will switch to Dashboard. It will show all the records from database when push History button. You could click any record to get 
into the detail information including the team attributes you put in and the relative charts.
There is a Log out button on the right up corner of the page. You could log out through push this button.

•	Back End (Receive API request)
Data Service: Post: save the prediction
Security authorization: token
Database in Back End called User. It used to store exist usernames and passwords.
When users in Front End want to log in, the username and password will send to the Back End to verify whether it is exist. If it is
exist it will return a token and the user can do some requests with permission restrictions. 
When users create an account, usernames and passwords could be saved in the Back End database.

Task Assignment:
Idea of the project: All the team members
Machine Learning: Yuexuan Liu
Front End：Xiaodan Wang, Lianshuai Song
Back End:  Peiguo Guan, Hongkai Hu
Summary of the task: All the team members.

    To-do list:
    Plan :
    =====================Mid break & wk 10=====================
    ===============Preparation ==============
    Come up with a scenario
    Select the Data sources that would help fulfil your scenario
    Opinion:kaggle is good
    ========================================
    Perform Data Integration and pre-processing if needed .
    Building a machine learning model to fulfil the scenario (using the dataset that you have prepared for training and evaluation)
    Not sure now: how to do the machine learning
    ============================wk 11===========================
    Designing a RESTful API to allow the consumption of your service ( you need to consider an authentication scheme for the consumers of your service)
    Point: authentication

    Mentor meeting one(3 marks)
    ============================wk 12===========================
    Designing a Simple Client with GUI (you are free to use whatever you like whether it is a simple HTML- java-script , ASP, php, JSP, JSF, or even window-based interfaces )

        Montor meeting two(3 marks)
    =========================================================


    (6 marks) Mentor meeting(wk11,12)
    Meeting One - more or so complete design documentation (10% of the total mark).

    (3 marks) Points to be discussed/assessed:  
    ‐ Has the group established an effective communication channel (only in English) for group work? (e.g., messaging, code repository)  
    ‐ Has the group established the roles and tasks necessary for the group work?  
    ‐ Has the group identified datasets to use the Data Analytics Service?  
    ‐ Has the group identified the use‐case scenario for the Data Analytics Service application? (i.e.,  what is the service going to offer for the users?)    
    ‐ Has the group identified the (high‐level) system architecture and components necessary for the group work?  (not to be detailed, high‐level plan)    

    Notes: Bring one‐page document with following information:  
    ‐ What is the aim of the service?  
    ‐ What are the datasets?  
    ‐ What is your communication channel?  
    ‐ What is your code repository?  
    ‐ A very brief description of each member’s role in the project
    Meeting Two - an early implementation of the service , demo of work in progress (10% of the total mark).
    Happen in wk12, nearly due, maybe we should finish it and ask for feedback from the mentor, only do improvement rather than new coding.

    (3 marks) Points to be discussed/assessed:  
    ‐ Is the group maintaining an effective communication channel for group work? (e.g., messaging,  code repository)  
    ‐ Is the group tracking the roles and tasks necessary for the group work? (i.e., is everybody fulfilling their tasks on time, and is there a mechanism in place to resolve problems?)  
    ‐ Is the implementation progressing towards the planned scenario?     

    Notes:  
    ‐ Each student separately should talk about their roles and how they have made progress  
    ‐ Present your communication channel (Should be only in English)   
    ‐ Present your code repository  

