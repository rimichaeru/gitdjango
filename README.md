# GitDjango

## Setup
For Windows, other systems may differ.

<br />

#### Create the virtual environment & install dependencies
1. After cloning the repo (eg. git clone REPOHTTPS), cd into the repo and run your terminal in this directory.
2. Create a new python environment in the terminal with: virtualenv env
3. Activate the new environment with: source env/Scripts/activate
4. Install dependencies automatically from the requirements file: pip install -r requirements.txt

#### Set up environment variables (SECRETS)
1. Create a file called <i>.env</i> inside /GitDjango/GitDjango/
2. Copy and paste the following code into the file:
   <pre>
   DEBUG=True
   TEMPLATE_DEBUG=True
   SECRET_KEY=
   SOCIAL_AUTH_GITHUB_KEY=
   SOCIAL_AUTH_GITHUB_SECRET=
   </pre>
3. In terminal (with the python environment running) run the following and paste the result after <i>SECRET_KEY=</i> without spaces: 
<pre>python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'</pre>
4. For the GITHUB KEY and SECRET, log into www.github.com and go to: https://github.com/settings/developers
5. Click 'OAuth Apps' on the left and then the 'New OAuth App' button on the right
6. Enter the following: 
<pre>
Application name: Can be anything, eg. Test Git Django App
Homepage URL: http://localhost:8000/
Application description: Anything or blank, eg. Lee-Michael Git Django Test
Authorization callback URL: http://localhost:8000/
</pre>
7. Create it, then on the next page click 'Generate a new client secret'
8. After <i>SOCIAL_AUTH_GITHUB_KEY=</i> insert your Client ID, and after <i>SOCIAL_AUTH_GITHUB_SECRET=</i> insert your newly generated Client secret, without any spaces

#### Running the server
1. In the terminal, with the local python env running, cd into /GitDjango (where manage.py is)
2. Run: python manage.py runserver