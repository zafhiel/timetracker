from pathlib import Path
import os

HOME = str(Path.home())
CONFIG_PATH = os.path.join(HOME, '.timetracker/config.toml')
BASE_URL = 'https://timetracker.bairesdev.com'

PROJECT_DROPDOWN = 'ctl00_ContentPlaceHolder_idProyectoDropDownList'
ASSIGNMENT_DROPDOWN = 'ctl00_ContentPlaceHolder_idTipoAsignacionDropDownList'
FOCAL_DROPDOWN = 'ctl00_ContentPlaceHolder_idFocalPointClientDropDownList'
TASK_CATEGORY_DROPDOWN = 'ctl00_ContentPlaceHolder_idCategoriaTareaXCargoLaboralDropDownList'
TASK_DESCRIPTION_DROPDOWN = 'ctl00_ContentPlaceHolder_idTareaXCargoLaboralDownList'

DICT_TASKS = {
    1:  ('Development', 'Bug Fixing'),
    2:  ('Development', 'Code review'),
    3:  ('Development', 'Configuration'),
    4:  ('Development', 'Debug'),
    5:  ('Development', 'Deployment'),
    6:  ('Development', 'Environment setup'),
    7:  ('Development', 'Features development'),
    8:  ('Development', 'Other - Development'),
    9:  ('Development', 'Requirements analysis'),
    10: ('Development', 'Research / Analysis'),
    11: ('Development', 'Research and Learning'),
    12: ('Meetings (Client)', 'Client Meeting'),
}

LOGIN_CREDENTIALS = ['username', 'password']
LOAD_HOURS_OPTIONS = ['project', 'focal']

WEEKDAYS = ['M', 'T', 'W', 'TH', 'F', 'S', 'SU']
