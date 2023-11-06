#!/bin/bash

sudo apt-get update
sudo apt-get -y install python3-pip

# Установка Apache Airflow
pip3 install apache-airflow

# Создание необходимых директорий
mkdir ~/airflow
mkdir ~/airflow/dags
mkdir ~/airflow/logs
mkdir ~/airflow/plugins

# Инициализация базы данных Airflow
airflow initdb

echo "Установка и настройка Airflow завершены"
