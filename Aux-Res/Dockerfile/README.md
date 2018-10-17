### How to build image and run it from terminal
1) Build the image
	```
	docker build -t <imagetag> <path to file>
	```
2) Run the vm
	```
	docker run -ti --name <name for vm> <imagetag>
	```

### How to restart the vm once used
```
docker start -i <name of vm>
```
