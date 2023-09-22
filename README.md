# Curebox - Patient and Health Insurance Management System
This platform provides insurance providers with the ability to customize insurance packages for patients. Patients can search for doctors based on multiple fields and book appointments. Doctors can view these appointments and address those patients. In this way, the system provides a 360-degree view of the entire process.

Registration and login process-

![image](https://github.com/amitaranade43/Curebox/assets/34507621/13796661-b5cc-4c5f-9ca3-ed31fdb8d8eb)  ![image](https://github.com/amitaranade43/Curebox/assets/34507621/d41800a5-354e-4788-bf4e-973e34a3414c)


## Curebox web application has 3 logins:

### 1)Insurance provider login-

A list of default insurance packages specific to logged in user would be displayed on home page:
![image](https://github.com/amitaranade43/Curebox/assets/34507621/179628ed-6cbe-4b74-adb4-4bc7bb640e54)

User can create a new insurance package using create button:

![image](https://github.com/amitaranade43/Curebox/assets/34507621/c0b2e5ac-3e0a-4fbc-9a35-d95560523965)


### 2)Patient login-

Patient user can search any doctor using doctor name , disease, based on whether doctor provides covid care and location:
![image](https://github.com/amitaranade43/Curebox/assets/34507621/3c7df1e8-c4d5-4280-b9a2-90753ae1da8f)

Once a doctor is selected , patient can book appointment using Book button. A page with all time slots will be displayed and user must select a time slot to book. Patient can also see doctor’s ratings and view doctor’s details using ‘View Doctor’ button:

![image](https://github.com/amitaranade43/Curebox/assets/34507621/8bf35ef7-847c-404e-b5a9-065ccc3cba9d)

Patient can access appointment details using Appointment Detail option:
![image](https://github.com/amitaranade43/Curebox/assets/34507621/461675a1-9cfd-400b-9fe0-9e272c31f10c)

Patient can also give feedback to doctor once appointment is completed using give feedback option on Appointment Details page:

![image](https://github.com/amitaranade43/Curebox/assets/34507621/95707e03-49b2-4ac4-8132-74da20a2231b)

Patient can access Insurance Provider details using Insurance Package option.



### 3)Doctor login-

Doctor can view appointments booked by patients and review them on home page:
![image](https://github.com/amitaranade43/Curebox/assets/34507621/ab7977ad-907c-4127-8964-e3a6b393e124)

Doctor can view patient details using ‘View Patient Appointment’ option and mark that appointment as complete


<br/>

Require installations to run it locally-
pip install -U Flask Authlib requests
pip install Flask Flask-WTF

Application hosted on- https://curebox.onrender.com/

This project is developed using Python Flask.
