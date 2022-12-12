coverage erase
for f in Tests*.py
do
   coverage run -a $f
done
coverage report
coverage html
open htmlcov/index.html

