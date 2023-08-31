# Django Assessment

### 0. Prequisites
1. Download and Install Python from <link>https://www.python.org/downloads/</link>
3. To run the project, if you have downloaded it to you computer, the compand is;-
    ```python manage.py runserver``` or ```python3 manage.py runserver```
4. When the server is running, access the site here: <link>http://127.0.0.1:8000</link>
5. Password Reset email can be found here <link>https://mailtrap.io/inboxes/2393953/messages</link>
    ```
    Password: X8jN-TRYcesN@.r
    Email: cryptoappdjango@gmail.com
    ```

6. To run tests, the command is:  ```pytest -s -v```

### 1. How to get code and get started locally
1. clone the project from github using git, if you don't have git installed on your computer,\n
    Download it here <link>https://git-scm.com/</link> Follow a few steps to install and get started, you can follow this guide <link>https://github.com/git-guides/install-git</link>
    After setting up git, open the command prompt/terminal on your computer and type the following commands(after every command press enter);-
    ```
    i. cd Desktop
    ii. mkdir DjangoAssessment
    iii. cd DjangoAssessment
    iv. python -m venv assessmentenv
    v. source assessmentenv/bin/activate
    vi. git clone https://github.com/Paulndambo/ASETT-Type-E-Submission.git
    vii. cd ASETT-Type-E-Submission
    viii. pip install -r requirements.txt
    ```

    Note: The above instructions will work 100% on linux and mac computers, for windows you mignt need to check some things.

2. If you don't want to install git on your laptop, click this link and download a zip file of the project into your computer <link>https://github.com/Paulndambo/ASETT-Type-E-Submission.git</link>
3. You can also use the github desktop application, download it here, <link>https://desktop.github.com/</link>, download it and follow the prompt
    steps to get started.

    Note: After step 2 and 3 follow the steps on step 1. 

<br></br>

### 2. Note, If you just want to run the project and test the interface
1. On Docker, run the following command (assuming you have docker installed)
    ```docker run -p 8000:8000 40781998/django-crypto-app-assessment:latest```
2. Kubernetes, if you have access to a kubernetes cluster
    Follow the steps listed on step 1 of (How to get code and get started locally), Then run the following command
    ```kubectl apply -f k8s/```

### How to run tests, (this assumes you have downloaded the repository on to your laptop)
Run this command 
    ```
    pytest -s -v
    ```
