### 1. Install packages
```bash
virtual venv
source venv/bin/activate
pip3 install -r requirements.txt    
```
### 2. Version od python
python3.8 is required to check your version, enter the following command in the console
```bash
python3 --version
```
### 3. Run app
```bash
python3 main.py
```

### 4. Build app
```bash
pyinstaller --onefile --icon=yt-icon.png --name=yt_downloader main.py
```

### 5. Development app
if you want add next page create new file in 'pages' package,
create class, which it must inherit from BasePage class
and import this class to ```pages/__init__.py``` file and append 
to PAGES tuple.

