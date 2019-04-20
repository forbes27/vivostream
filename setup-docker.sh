docker build -t shemarinv/app .

docker build -t shemarinv/postgres ./db

docker network create app-net

docker run -d --name postdb --net app-net -p 5432:5432 shemarinv/postgres 

docker run -d --name app-cont --net app-net -p 5000:5000 shemarinv/app 

