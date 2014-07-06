clean: clean-build clean-pyc

clean-build:
	rm -fr build/
	rm -fr dist/
	rm -fr *.egg-info

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +

pep8:
	flake8 --exclude=migrations dbsnapshot

release: clean
	python setup.py register sdist upload --sign
	python setup.py bdist_wheel upload --sign

sdist: clean
	python setup.py sdist
	ls -l dist

shell:
	cd demo && python manage.py shell

run:
	cd demo && python manage.py runserver_plus

run_celery:
	cd demo && python manage.py celeryd -v 2 -B -s celery -E -l INFO

run_shell:
	cd demo && python manage.py shell_plus --print-sql
