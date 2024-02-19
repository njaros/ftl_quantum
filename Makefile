all : build run

build :
		docker build -t qiskit_img .

run :
		docker run -it --volume=./:/app qiskit_img