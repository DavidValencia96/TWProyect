// web: uvicorn main:app --reload --host=0.0.0.0 --port=${PORT-5000}


// web: gunicorn django_proyect.wsgi

web: gunicorn social_proyect.wsgi:application --log-file - --log-level debug
python manage.py collectstatic --noinput
manage.py migrate