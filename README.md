## VisionaryLearn

1. Install Python dependencies:

    ```console
    $ pip install -r requirements.txt
    ```

2. Create a development database:

    ```console
    $ python manage.py migrate
    ```

3. Install JavaScript dependencies (from 'frontend' folder):

    ```console
    $ npm install
    ```

4. If everything is alright, you should be able to start the Django development server from the main folder:

    ```console
    $ python manage.py runserver
    ```

5. and the Vue server from the 'frontend' sub-folder:

    ```console
    $ npm run dev
    ```

6. Open your browser and go to http://localhost:5173, you will be greeted with the application.
