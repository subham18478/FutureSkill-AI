# FutureSkill AI --- Setup

## Run locally

``` powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python app\main.py
```

Open:

`http://127.0.0.1:5000/`

## Main API endpoints

-   `/api/data`
-   `/api/skill-gaps`
-   `/api/future-skills`
-   `/api/declining-skills`
-   `/api/reskilling-roles`
-   `/api/records`

Make sure each Flask endpoint is defined only once in `main.py`.
