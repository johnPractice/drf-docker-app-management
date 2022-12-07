# drf-docker-app-management


## Project Structure
```
├── docker_app
│   ├── migrations
│   ├── Optional[serializers]
│   ├── Optional[routers]
│   ├── Optional[models]
|
├── hamravesh
├── utils

```
In big application we must seperate big file into small files based on reason if we have large serializers should create serializers forlder and multiple file ex:
```
│   ├──serializers
|   │   ├── __init__.py
|   │   ├── x.py
|   │   ├── y.py
|   │   ├── .....


```

## Run project
For run project you should set <b>.env </b> file and add
<ul>
<li>SECRET_KEY</li>
<li>REDIS_HOST</li>
<li>REDIS_PORT</li>
<li>REDIS_PASSWORD</li>
<li>REDIS_USERNAME</li>
<li>DB_HOST</li>
<li>DB_PORT</li>
<li>DB_USER</li>
<li>DB_PASSWORD</li>
</ul>
some of these parameter optional and based on your configuration(ex: if you use postgress db you should pass DB_xxx variable in .env file).

## Future Work
for more work can do
<ul>
<li>Add user authentication for <b>CRUD</b> opration.</li>
<li>Create permision for action (ex: just see container,edit or create and...).</li>
<li>Add payment logic and calculate coast as <b>"pay as you go"</b>.</li>
<li>For big appliction should seperate big file into small files (ex : if routers are bigger than this should seperate it into multiple files)</li>
</ul>


## Assumptions
I assume that for every user have isolate envoironment that can run containers. (for example we can use Vgrant to create new  VM for  user and only on own VM run containers)