#!/bin/sh

host=$(echo "$1" | cut -d: -f1)
port=$(echo "$1" | cut -d: -f2)

echo "Waiting for PostgreSQL at $host:$port..."

for i in $(seq 1 30); do
  nc -z "$host" "$port" >/dev/null 2>&1
  if [ $? -eq 0 ]; then
    echo "PostgreSQL is available after $i seconds!"
    
    # Применяем миграции
    echo "Applying database migrations..."
    python manage.py migrate --noinput
    
    # Собираем статику (если нужно)
    echo "Collecting static files..."
    python manage.py collectstatic --noinput --clear
    
    # Запуск Django
    echo "Starting Django server..."
    exec python manage.py runserver 0.0.0.0:8000
    break
  fi
  echo "Attempt $i: PostgreSQL not ready at $host:$port..."
  sleep 1
done

if [ $? -ne 0 ]; then
  echo "Failed to connect to PostgreSQL after 30 seconds. Exiting."
  exit 1
fi