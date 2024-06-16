test:
	python3 main.py < in.txt

# Simulate the python compile, run and delete
cpp:
	g++ -std=c++20 -Wall -O2 main.cpp -o main

build:
	python3 build.py