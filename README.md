# Flask Photo App

## Getting Started

```
python -m venv venv
source venv venv
pip install -r requirements.txt
```

## Usage
```
export FLASK_APP=app.py 
flask run
```

## File Structure
- `app.py`: The main Flask application file to `index.html` template.
- `templates/`: Contains the HTML templates required.
  - `_base.html`: The base template for the web page.
  - `index.html`: A child template that extends the `_base.html` and provides the additional content.