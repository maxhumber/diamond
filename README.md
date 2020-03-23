### Diamond

1. Setup env

```
python -m venv .venv
```

2. Activate

```
source .venv/bin/activate
```

3. Install depends

```
pip install gunicorn scikit-learn pandas sklearn-pandas flask
```

4. Freeze depends

```
pip freeze > requirements.txt
```

5. Run model

```
python model.py
```

6. Run app

```
python app.py
```



