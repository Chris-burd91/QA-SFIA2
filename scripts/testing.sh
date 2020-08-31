echo "Testing Application"

cd app1
pip3 install -r requirements.txt
echo "Test app1"
pytest --cov application --cov-report term-missing

cd ..

cd app2
pip3 install -r requirements.txt

pytest --cov application --cov-report term-missing

cd ..

cd app3
pip3 install -r requirements.txt

pytest --cov application --cov-report term-missing

cd ..

cd app4
pip3 install -r requirements.txt

pytest --cov application --cov-report term-missing

cd ..