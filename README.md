Multi Shop

Installation

To set up the project locally, follow these steps:

1. Clone the repository

   
   git clone https://github.com/ThompsonShell/multi_shop.git
   cd multi_shop



3.  Create a virtual environment


      python3 -m venv venv

      source venv/bin/activate # For Windows, use `venv\Scripts\activate`


4. Install required packages

      
      pip install -r requirements.txt

5. Configure Environment Variables
Rename the .env.example file to .env and replace your_secret_key with your actual Django secret key, along with any other necessary environment-specific values:

   
      SECRET_KEY=your_secret_key

6. Apply migrations

   
      python manage.py migrate

7. Create a superuser

   
      python manage.py createsuperuser

8. Run the project


    python manage.py runserver

Usage

After starting the project, you can access the following URLs:

    http://localhost:8000/ - Home page
    http://localhost:8000/admin/ - Admin panel
