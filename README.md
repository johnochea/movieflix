# movieflix
A simple CRUD for a movie management system

- Uses Python Django and Vue

Instructions:
- Clone the repo  
`git clone https://github.com/johnochea/movieflix.git`  
`cd movieflix`  

### BACKEND:

- Install python3
- After that, run the following:   
`cd backend`  
`python3 -m venv venv`  
then  
`source venv/bin/activate`  
`pip install -r requirements.txt`  

After installing, migrate:  
`python3 manage.py migrate`

Run the server:  
`python3 manage.py runserver`

### FRONTEND:
- Navigate to `movieflix`
- `cd frontend`  

Then install the packages:  
`npm i`

Run the server afterwards:
`npm run dev`

### INSTRUCTIONS
- Navigate to local
- Create an account
- Log in
- Upload a movie
- Click on the movie
- Watch the movie, edit, or delete

### MISSING FEATURES
Some features are missing, such as the following:
- title and description length validations
- file type and size validations
- specifying who can upload/edit videos and who can watch only
- missing success displays
- sorters
- editing can only edit if a new video is uploaded
- No breadcrumbs or navigation on header

### VIDEO DEMO:
https://drive.google.com/file/d/1TrgAOOWOPVd-9wfYtnKZd343lbENp1QG/view?usp=sharing
