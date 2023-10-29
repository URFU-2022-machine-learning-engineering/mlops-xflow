#!/bin/bash

working_dir=&1

if [ -z "$working_dir" ]
then
    echo "Path to project is not specified"
    echo "Using current folder as project"
    working_dir=$(pwd)
fi

if [ ! -d "$working_dir" ]
then
    echo "Directory $working_dir does not exist"
    exit 1
fi

if [ ! -d "$working_dir/venv" ]
then
    echo "Virtual environment does not exist"
    echo "Creating virtual environment"
    python3 -m venv "$working_dir"/venv
fi

source venv/bin/activate

export AIRFLOW_HOME="$working_dir"/airflow
export PYTHONPATH=$working_dir

airflow webserver -p 8080 -D
airflow scheduler -D
