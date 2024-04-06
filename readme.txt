// nginx with a path html 
docker run --name nginx --hostname ng1 -p 80:80 -v /home/abhishek/nginx/html:/usr/share/nginx/html
 -d nginx

//ispect container 
docker logs nginx


//create fastapiapp
docker build . -t fastapiapp
docker run --hostname fastapiapp1 --name fastapiapp1 -d fastapiapp
docker run --hostname fastapiapp2 --name fastapiapp2 -d fastapiapp
docker run --hostname fastapiapp3 --name fastapiapp3 -d fastapiapp


// create a docker network
docker network create backendnet
docker network connect backendnet fastapiapp1
docker network connect backendnet fastapiapp2
docker network connect backendnet fastapiapp3
docker network connect backendnet nginx


//set configuration of nginx and mount nginx.conf
 docker run --hostname ng1 --name ng1 -p 80:8080 --network backendnet -v /home/abhishek/nginx/nginx1.conf:/etc/nginx/nginx.c
onf -d nginx
docker run --hostname ng2 --name ng2 -p 80:8080 --network backendnet1 -v /home/abhishek/nginx/nginx2.conf:/etc/nginx/nginx.c
onf -d nginx
