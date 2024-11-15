Multi Shop

Installation

To set up the project locally, follow these steps:

1. Clone the repository

   ```bash
   git clone https://github.com/ThompsonShell/multi_shop.git
   cd multi_shop
   ```


2. Create a virtual environment

   ```bash
   python3 -m venv venv
   source venv/bin/activate # For Windows, use `venv\Scripts\activate`
   ```

3. Install required packages

   ```bash
   pip install -r requirements.txt
   ```   

4. Configure Environment Variables
Rename the .env.example file to .env and replace your_secret_key with your actual Django secret key, along with any other necessary environment-specific values:

   ```bash
   SECRET_KEY=your_secret_key
   ```

5. Apply migrations

   ```bash
   python manage.py migrate
   ```

6. Create a superuser

   ```bash
   python manage.py createsuperuser
   ```

7. Run the project

   ```bash
   python manage.py runserver
   ```
   
Usage

After starting the project, you can access the following URLs:

    http://localhost:8000/ - Home page
    http://localhost:8000/admin/ - Admin panel
