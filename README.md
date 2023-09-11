# neugo
# API Task
Input (Request): rowPref, seatPref, berthPref, totalPax
Output (Response): seatNumbers
Example: rowPref=Front, seatPref=Aisle, berthPref=None, is given as input then system should return seat numbers between 1A - 4D (depending on what is available). If there is more than 1 customer, then return a sequence starting from a number in between the above

Row Preference: Front (1-4), Center(5-7), Back(8-11)

# Neugo Assignment Docsfile Link
- https://docs.google.com/document/d/1_AvKwRH560B9G1WHHRFTnx5oRIhYuQuEhyq3o4mHXC4/edit


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

    - Input Example :
           {
          "coach": "GreenGo",
          "prefer_row": "Center",
          "prefer_seat": "Aisle",
          "total_pax": 2 
           }
     - Output Example : 
           {
        "seat": {
            "bus": {
                "id": 2,
                "coach": "GreenGo",
                "departure_city": 4,
                "destination_city": 7,
                "date": "2023-09-06",
                "hours": "7h 10m",
                "boarding_point": "Banglore Hotel",
                "dropping_point": "Chandigarh Point",
                "departure_time": "11:37:16",
                "destination_time": "04:00:00",
                "price": 500
            }
        },
        "prefer_row": "Center",
        "prefer_seat": "Aisle",
        "seat_number": "6",
        "is_booked": false,
        "created_at": "2023-09-08T10:33:32.529741Z",
        "updated_at": "2023-09-08T10:42:39.908761Z"
    },
    {
        "seat": {
            "bus": {
                "id": 2,
                "coach": "GreenGo",
                "departure_city": 4,
                "destination_city": 7,
                "date": "2023-09-06",
                "hours": "7h 10m",
                "boarding_point": "Banglore Hotel",
                "dropping_point": "Chandigarh Point",
                "departure_time": "11:37:16",
                "destination_time": "04:00:00",
                "price": 500
            }
        },
        "prefer_row": "Center",
        "prefer_seat": "Aisle",
        "seat_number": "7",
        "is_booked": false,
        "created_at": "2023-09-08T10:33:42.569231Z",
        "updated_at": "2023-09-08T10:33:42.569264Z"
    }

    - http://127.0.0.1:8000/v1/seat/    method:GET

    - Seat Availability GET Endpoint param Request

    - Query Params Input Example:
          - Note: coach=1,2 means 1=NueGo or 2=GreenG0
          coach=1
          prefer_row=Back
          prefer_seat=Aisle

    - Output Example:
                  {
            "seat": {
                "bus": {
                    "id": 1,
                    "coach": "NueGO",
                    "departure_city": 1,
                    "destination_city": 6,
                    "date": "2023-09-05",
                    "hours": "6h 20m",
                    "boarding_point": "Abohar bridge",
                    "dropping_point": "Amritsar Highway",
                    "departure_time": "06:00:00",
                    "destination_time": "18:00:00",
                    "price": 350
                }
            },
            "prefer_row": "Back",
            "prefer_seat": "Aisle",
            "seat_number": "9",
            "is_booked": false,
            "created_at": "2023-09-08T10:34:22.396812Z",
            "updated_at": "2023-09-08T10:34:22.396847Z"
        }

                      
    3.) BookSeat endpoint
      - http://127.0.0.1:8000/v1/book_seat/   method:POST
      
      - Input Example:
      - Note here bus:1 is NueGo or bus:2 is GreenGo
      - If you provide invalid param you got validation error
        and you try to already booked seat you got reponse "Seats already booked by other."
        
      - For Single Seat Booking
        {
          "bus": 1,
          "seat": [
              {
                  "prefer_row": "Front",
                  "prefer_seat": "Window",
                  "seat_number": 1
              }
       
          ]
      
      }
      
      - For multiple Seat Booking
      
      {
      "bus": 1,
      "seat": [
          {
              "prefer_row": "Front",
              "prefer_seat": "Window",
              "seat_number": 1
          },
          {
              "prefer_row": "Center",
              "prefer_seat": "Aisle",
              "seat_number": 6
          }
         
      ]
      }
      
      - Multiple Seat Output Example
       {
              "id": 88,
              "user": {
                  "id": 1,
                  "email": "admin@gmail.com",
                  "name": "admin",
                  "is_active": true
              },
              "bus": {
                  "id": 1,
                  "coach": "NueGO",
                  "departure_city": 1,
                  "destination_city": 6,
                  "date": "2023-09-05",
                  "hours": "6h 20m",
                  "boarding_point": "Abohar bridge",
                  "dropping_point": "Amritsar Highway",
                  "departure_time": "06:00:00",
                  "destination_time": "18:00:00",
                  "price": 350
              },
              "seat": [
                      {
                          "prefer_row": "Front",
                          "prefer_seat": "Window",
                          "seat_number": "1",
                          "is_booked": true,
                          "created_at": "2023-09-11T06:50:56.206245Z",
                          "updated_at": "2023-09-11T06:50:56.206288Z"
                      },
                      {
                          "prefer_row": "Center",
                          "prefer_seat": "Aisle",
                          "seat_number": "6",
                          "is_booked": true,
                          "created_at": "2023-09-11T06:50:56.206337Z",
                          "updated_at": "2023-09-11T06:50:56.206355Z"
                      }
                  ],
                  "total_passengers": 2,
                  "created_at": "2023-09-11T06:50:56.201649Z",
                  "updated_at": "2023-09-11T06:50:56.201683Z"
         }

     

    
