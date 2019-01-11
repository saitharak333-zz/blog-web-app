# blog-web-app

I have used Python 3.6.7 version and Django 2.1 version.
It successfully ran on Ubuntu 18.04 OS.
These instructions are strictly for linux users, other users have to modify the statements as per their system standards.
Update the OS using, 

    sudo apt-get update
Open your project folder or Create it using your terminal.
    
    mkdir projects
    cd projects
Clone this repo,

    git clone https://github.com/saitharak333/blog-web-app.git
    
Open blog-web-app

    cd blog-web-app
    
Switch to  virtual environment,

    source env/bin/activate
    
Install python3,

    sudo apt install python3-minimal
    
Install pip3 for installing django,

    sudo apt-get -y install python3-pip
    
Install Django using pip3,

    pip3 install django
    
Install PILLOW, (to read and output images)

    pip3 install PILLOW
    
Now open the blog app,

    cd blog
    
Run the server using,

    python3 manage.py runserver
    
Open your web browser and type the url,

    http://127.0.0.1:8000/
    
This takes you to the homepage and you can create your own articles.

I have designed this blog assuming that it has to be a private inter college blog. 

So I have only given the permision to superadmin to create the users. But I also have given the template of creating our own signup form but left it as such. Didn't give connection to the user database.

In order to open admin site use this url,

    http://127.0.0.1:8000/admin
    
 I have already created a superuser which is stored in the database, to login into the database use credentials
 
    username: tharak
    password: test1234
    
Testings usernames,
 
    username: B150289ME
    password: tharaksaibobba
    
