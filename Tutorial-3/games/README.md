# Django Game Reviews

Simple Django app for game reviews and tags.

## Features

- Review page at `/` and `/reviews/`
- Sidebar navigation for Games, Reviews, Tags, Add Game, Add Review, and Add Tag
- Tag list page at `/tags/`
- Shared `base.html` layout with footer
- Review cards show developer, platform, and tags

## Quick Start (Windows PowerShell)

```powershell
cd "C:\Users\Asus\Documents\GitHub\Tutorial-WOC7014\Tutorial-3\games"
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_demo_data
python manage.py runserver
```

Open:

- `http://127.0.0.1:8000/`
- `http://127.0.0.1:8000/reviews/`
- `http://127.0.0.1:8000/tags/`
- `http://127.0.0.1:8000/tags/add/`
- `http://127.0.0.1:8000/admin/`

## Create sample data

Run `python manage.py seed_demo_data` to populate sample tags, games, and reviews.

If you want to load the JSON fixture directly on a fresh database, use:

```powershell
python manage.py loaddata sample_data
```

