# Documentation for using the CLI tool
This directory contains the codebase of a CLI tool which was built according to the following requirement:

1. Print the numbers from 1 to 10 in random order to the terminal

## Requirements
The CLI tool was built using Docker engine 19.03.8.It should work without any problems with other versions of Docker, though. 
The OS under which the development was done is Mac OS 10.15.4. The main reason that this cli tool was built using a docker image, is that it can run on every OS without making any modifications on the user's host machine (installing dependencies, configuration etc).

## How to use the files included in this repository
The structure of this codebase is shown below:

```
.
├── Dockerfile
├── Makefile
├── README.md
├── adjust.py
├── pylintrc
├── requirements.txt
└── test_adjust.py

```

# How to build and use the Docker Image that includes the CLI tool

All you need in order to build the Docker image that will contain the CLI tool is to run the following command:

``` make all  ```


The above command: 

1. Builds the Docker image
2. Runs pep8 compliance and linter on the code
3. Runs unit tests to verify the validity of the code

After the above command is complete you can invoke the CLI tool by running:

``` docker run adjust ```

Example:

```
➜ docker run adjust
[8, 1, 4, 7, 6, 2, 3, 9, 10, 5]

➜ docker run adjust
[10, 9, 6, 4, 1, 8, 3, 7, 2, 5]

```
