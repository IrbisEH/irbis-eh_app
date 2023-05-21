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


def copy_css():
    for css in SOURCE_CSS_LIST:
        file_name = Path(css).name
        new_file_path = os.path.join(TARGET_STATIC_PATH, PROJECT_NAME, file_name)
        rebase_path = PROJECT_NAME + '/' + file_name
        NEW_PATHS[file_name] = rebase_path
        shutil.copy(css, new_file_path)


def copy_js():
    for js in SOURCE_JS_LIST:
        file_name = Path(js).name
        new_file_path = os.path.join(TARGET_STATIC_PATH, PROJECT_NAME, file_name)
        rebase_path = PROJECT_NAME + '/' + file_name
        NEW_PATHS[file_name] = rebase_path
        shutil.copy(js, new_file_path)


def copy_static():
    target_dir_path = os.path.join(TARGET_STATIC_PATH, PROJECT_NAME, 'static')
    if os.path.isdir(target_dir_path):
        shutil.rmtree(target_dir_path)
    os.mkdir(target_dir_path)
    static_files = glob.glob(f'{SOURCE_STATIC}/*')
    for file in static_files:
        file_name = Path(file).name
        new_file_path = os.path.join(TARGET_STATIC_PATH, PROJECT_NAME, 'static', file_name)
        rebase_path = PROJECT_NAME + '/static/' + file_name
        NEW_PATHS[file_name] = rebase_path
        shutil.copy(file, new_file_path)


def replace_links():
    for html in SOURCE_HTML_LIST:
        file_name = Path(html).name
        new_html_path = os.path.join(TARGET_TEMPLATES_PATH, PROJECT_NAME, file_name)
        with open(new_html_path, 'r') as file:
            html_content = file.read()
        soup = BeautifulSoup(html_content, 'html.parser')

        for link_tag in soup.find_all('link', href=True):
            href = link_tag['href']
            href = href.split('/')
            if href[-1] in NEW_PATHS.keys():
                link_tag['href'] = "{{ url_for('static', filename='" + NEW_PATHS[href[-1]] + "') }}"
        for script_tag in soup.find_all('script', src=True):
            src = script_tag['src']
            src = src.split('/')
            if src[-1] in NEW_PATHS.keys():
                script_tag['src'] = "{{ url_for('static', filename='" + NEW_PATHS[src[-1]] + "') }}"
        for img_tag in soup.find_all('img', src=True):
            src = img_tag['src']
            src = src.split('/')
            if src[-1] in NEW_PATHS.keys():
                img_tag['src'] = "{{ url_for('static', filename='" + NEW_PATHS[src[-1]] + "') }}"
        for object_tag in soup.find_all('object', data=True):
            data = object_tag['data']
            data = data.split('/')
            if data[-1] in NEW_PATHS.keys():
                object_tag['data'] = "{{ url_for('static', filename='" + NEW_PATHS[data[-1]] + "') }}"

        updated_html = str(soup)
        with open(new_html_path, 'w') as file:
            file.write(updated_html)

    # target_dir_path = os.path.join(TARGET_STATIC_PATH, PROJECT_NAME, 'static')
    # svg_files = glob.glob(f'{target_dir_path}/*.svg')
    # for file in svg_files:
    #     with open(file, 'r') as file:
    #         svg_content = file.read()
    #     soup = BeautifulSoup(svg_content, 'xml')
    #     tags = soup.find_all()
    #     for tag in tags:
    #         print(tag)



if __name__ == '__main__':
    renew_project_dirs()
    copy_html()
    copy_css()
    copy_js()
    copy_static()
    replace_links()
    # print(NEW_PATHS)




