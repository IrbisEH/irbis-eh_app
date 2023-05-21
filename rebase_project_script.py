import os
import glob
from pathlib import Path
import shutil
from bs4 import BeautifulSoup

DIR = os.path.abspath(os.path.dirname(__file__))

PROJECT_NAME = 'landing_page_covid-19'
SOURCE_PROJECT_PATH = os.path.join(DIR, PROJECT_NAME)

SOURCE_HTML_LIST = glob.glob(f'{SOURCE_PROJECT_PATH}/*.html')
SOURCE_CSS_LIST = glob.glob(f'{SOURCE_PROJECT_PATH}/*.css')
SOURCE_JS_LIST = glob.glob(f'{SOURCE_PROJECT_PATH}/*.js')
SOURCE_STATIC = os.path.join(SOURCE_PROJECT_PATH, 'static')

TARGET_TEMPLATES_PATH = os.path.join(DIR, 'irbis-eh_app', 'templates')
TARGET_STATIC_PATH = os.path.join(DIR, 'irbis-eh_app', 'static')

NEW_PATHS = {}


def renew_project_dirs():
    template_dir = os.path.join(TARGET_TEMPLATES_PATH, PROJECT_NAME)
    static_dir = os.path.join(TARGET_STATIC_PATH, PROJECT_NAME)
    for target_dir in [template_dir, static_dir]:
        if os.path.isdir(target_dir):
            shutil.rmtree(target_dir)
        os.makedirs(target_dir)


def copy_html():
    for html in SOURCE_HTML_LIST:
        file_name = Path(html).name
        new_file_path = os.path.join(TARGET_TEMPLATES_PATH, PROJECT_NAME, file_name)
        rebase_path = PROJECT_NAME + '/' + file_name
        NEW_PATHS[file_name] = rebase_path
        shutil.copy(html, new_file_path)



if __name__ == '__main__':
    renew_project_dirs()
    copy_html()
    print(NEW_PATHS)




