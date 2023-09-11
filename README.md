# neugo
# API Task
Input (Request): rowPref, seatPref, berthPref, totalPax
Output (Response): seatNumbers
Example: rowPref=Front, seatPref=Aisle, berthPref=None, is given as input then system should return seat numbers between 1A - 4D (depending on what is available). If there is more than 1 customer, then return a sequence starting from a number in between the above

Row Preference: Front (1-4), Center(5-7), Back(8-11)


# How to Run this NeuGo Project ?

- First open your any IDE then terminal in wriet the command
  - git clone https://github.com/alpitmalineo/neugo.git
- Second in project clone after create virtual enviorment for install project requirments library.
  - example : virtualenv venv (venv name) for active in linux or mac source venv/bin/active. for windows venv\Script\active
- after virtual enviorment active after go project directory in cd score then install "requirements.txt" file in virtual enviorment like "pip install -r requirements.txt"


# APIs endpoint

1.) Django superuser login  
    - http://127.0.0.1:8000/admin/
    - username: admin@gmail.com
    - password: admin

 2.) Seat availibility check endpoint  
    - http://127.0.0.1:8000/v1/seat/    method:POST
    
    - Seat Availability POST Endpoint Body Request

    - Example:
           {
          "coach": "GreenGo",
          "prefer_row": "Center",
          "prefer_seat": "Aisle",
          "total_pax": 2 
           }

    - http://127.0.0.1:8000/v1/seat/    method:GET

    - Seat Availability GET Endpoint param Request

    - Example:
    
