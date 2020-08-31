

echo "Testing Application"
export TEST_DB_URI=${TEST_DB_URI}

cd app1
pip3 install -r requirements.txt
echo "Test Application 1"
python3 -m pytest --cov application --cov-report term-missing

cd ..

cd app2
pip3 install -r requirements.txt
echo "Test Application 2"
python3 -m pytest --cov application --cov-report term-missing

cd ..

cd app3
pip3 install -r requirements.txt
echo "Test Application 3"
python3 -m pytest --cov application --cov-report term-missing

cd ..

cd app4
pip3 install -r requirements.txt
echo "Test Application 4"
python3 -m pytest --cov application --cov-report term-missing

cd ..