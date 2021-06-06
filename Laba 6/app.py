import numpy as np
from flask import Flask, request, render_template, session, redirect, Response, send_from_directory, send_file
import pandas as pd
from flask_assets import Environment, Bundle
import matplotlib.pyplot as plt
import os
import requests

app = Flask(__name__)
assets = Environment(app)
assets.url = app.static_url_path
scss = Bundle('graphic-button.scss', filters='pyscss', output='all.css')
assets.register('scss_all', scss)

url = 'https://raw.githubusercontent.com/k0perX-X/mal-database/master/csv/latest.csv'
with requests.get(url, stream=True) as r:
    r.raise_for_status()
    with open('latest.csv', 'wb') as f:
        for chunk in r.iter_content(chunk_size=8192):
            # If you have chunk encoded response uncomment if
            # and set chunk_size parameter to None.
            # if chunk:
            f.write(chunk)

if not os.path.isdir('static/pictures'):
    os.mkdir('static/pictures')

for file in os.listdir('static/pictures'):
    if os.path.isfile(f'static/pictures/{file}'):
        os.remove(f'static/pictures/{file}')

# params = {"ytick.color": "black",
#           "xtick.color": "b",
#           "axes.labelcolor": "b",
#           "axes.edgecolor": "b"}
# plt.rcParams.update(params)


def float_format(fl):
    if fl == np.NAN:
        return 'NaN'
    else:
        return str(int(fl))


def make_df(find):
    return original_df.loc[find_df['Name'].str.contains(find) | find_df['Score rank'].isin([find]) |
                           find_df['Popularity rank'].isin([find]) | find_df['Score'].isin([find]) |
                           find_df['Episodes'].isin([find]) | find_df['Type'].str.contains(find) |
                           find_df['Premiered'].str.contains(find) | find_df['English name'].str.contains(find) |
                           find_df['Japanese name'].str.contains(find) | find_df['Synonyms'].str.contains(find) |
                           find_df['Status'].str.contains(find) | find_df['Aired'].str.contains(find) |
                           find_df['Broadcast'].str.contains(find) | find_df['Producers'].str.contains(find) |
                           find_df['Licensors'].str.contains(find) | find_df['Studios'].str.contains(find) |
                           find_df['Source'].str.contains(find) | find_df['Genres'].str.contains(find) |
                           find_df['Duration'].str.contains(find) | find_df['Rating'].str.contains(find)]


def make_df_percent(find):
    return percent_df.loc[find_df['Name'].str.contains(find) | find_df['Score rank'].isin([find]) |
                          find_df['Popularity rank'].isin([find]) | find_df['Score'].isin([find]) |
                          find_df['Episodes'].isin([find]) | find_df['Type'].str.contains(find) |
                          find_df['Premiered'].str.contains(find) | find_df['English name'].str.contains(find) |
                          find_df['Japanese name'].str.contains(find) | find_df['Synonyms'].str.contains(find) |
                          find_df['Status'].str.contains(find) | find_df['Aired'].str.contains(find) |
                          find_df['Broadcast'].str.contains(find) | find_df['Producers'].str.contains(find) |
                          find_df['Licensors'].str.contains(find) | find_df['Studios'].str.contains(find) |
                          find_df['Source'].str.contains(find) | find_df['Genres'].str.contains(find) |
                          find_df['Duration'].str.contains(find) | find_df['Rating'].str.contains(find)]


original_df = pd.read_csv('latest.csv', index_col=0).drop_duplicates()
original_df['Score'] = original_df['Score'].astype(str)
col = list(original_df.columns)
col.remove('Link')
col.append('Link')
original_df = original_df[col]
find_df = pd.read_csv('latest.csv', index_col=0, dtype=str).drop_duplicates()
for i in find_df.columns:
    find_df[i] = find_df[i].str.lower()

percent_df = original_df.copy()[['Members score 10', 'Members score 9', 'Members score 8', 'Members score 7',
                                 'Members score 6', 'Members score 5', 'Members score 4', 'Members score 3',
                                 'Members score 2', 'Members score 1']]
percent_df['Members score 10'] = original_df['Members score 10'] / (
        original_df['Members score 10'] + original_df['Members score 9'] + original_df['Members score 8'] +
        original_df['Members score 7'] + original_df['Members score 6'] + original_df['Members score 5'] +
        original_df['Members score 4'] + original_df['Members score 3'] + original_df['Members score 2'] +
        original_df['Members score 1'])
percent_df['Members score 9'] = original_df['Members score 9'] / (
        original_df['Members score 10'] + original_df['Members score 9'] + original_df['Members score 8'] +
        original_df['Members score 7'] + original_df['Members score 6'] + original_df['Members score 5'] +
        original_df['Members score 4'] + original_df['Members score 3'] + original_df['Members score 2'] +
        original_df['Members score 1'])
percent_df['Members score 8'] = original_df['Members score 8'] / (
        original_df['Members score 10'] + original_df['Members score 9'] + original_df['Members score 8'] +
        original_df['Members score 7'] + original_df['Members score 6'] + original_df['Members score 5'] +
        original_df['Members score 4'] + original_df['Members score 3'] + original_df['Members score 2'] +
        original_df['Members score 1'])
percent_df['Members score 7'] = original_df['Members score 7'] / (
        original_df['Members score 10'] + original_df['Members score 9'] + original_df['Members score 8'] +
        original_df['Members score 7'] + original_df['Members score 6'] + original_df['Members score 5'] +
        original_df['Members score 4'] + original_df['Members score 3'] + original_df['Members score 2'] +
        original_df['Members score 1'])
percent_df['Members score 6'] = original_df['Members score 6'] / (
        original_df['Members score 10'] + original_df['Members score 9'] + original_df['Members score 8'] +
        original_df['Members score 7'] + original_df['Members score 6'] + original_df['Members score 5'] +
        original_df['Members score 4'] + original_df['Members score 3'] + original_df['Members score 2'] +
        original_df['Members score 1'])
percent_df['Members score 5'] = original_df['Members score 5'] / (
        original_df['Members score 10'] + original_df['Members score 9'] + original_df['Members score 8'] +
        original_df['Members score 7'] + original_df['Members score 6'] + original_df['Members score 5'] +
        original_df['Members score 4'] + original_df['Members score 3'] + original_df['Members score 2'] +
        original_df['Members score 1'])
percent_df['Members score 4'] = original_df['Members score 4'] / (
        original_df['Members score 10'] + original_df['Members score 9'] + original_df['Members score 8'] +
        original_df['Members score 7'] + original_df['Members score 6'] + original_df['Members score 5'] +
        original_df['Members score 4'] + original_df['Members score 3'] + original_df['Members score 2'] +
        original_df['Members score 1'])
percent_df['Members score 3'] = original_df['Members score 3'] / (
        original_df['Members score 10'] + original_df['Members score 9'] + original_df['Members score 8'] +
        original_df['Members score 7'] + original_df['Members score 6'] + original_df['Members score 5'] +
        original_df['Members score 4'] + original_df['Members score 3'] + original_df['Members score 2'] +
        original_df['Members score 1'])
percent_df['Members score 2'] = original_df['Members score 2'] / (
        original_df['Members score 10'] + original_df['Members score 9'] + original_df['Members score 8'] +
        original_df['Members score 7'] + original_df['Members score 6'] + original_df['Members score 5'] +
        original_df['Members score 4'] + original_df['Members score 3'] + original_df['Members score 2'] +
        original_df['Members score 1'])
percent_df['Members score 1'] = original_df['Members score 1'] / (
        original_df['Members score 10'] + original_df['Members score 9'] + original_df['Members score 8'] +
        original_df['Members score 7'] + original_df['Members score 6'] + original_df['Members score 5'] +
        original_df['Members score 4'] + original_df['Members score 3'] + original_df['Members score 2'] +
        original_df['Members score 1'])


@app.route('/')
def f():
    find = request.args.get('find')
    if find == '' or find is None:
        return render_template('finder.html')
    else:
        graph = request.args.get('graph')
        user_find = find
        if graph is None:
            find = find.lower()
            df = make_df(find)
            df = df.reset_index()
            del df['index']
            df = df.loc[df.index < 300]
            return render_template('finder.html', find=user_find, tables=[df.to_html(classes='table-fill', index=False,
                                                                                     float_format=float_format,
                                                                                     # notebook=True,

                                                                                    )])
        else:
            return render_template('graphic.html', find=user_find)


@app.route('/css/<path:path>')
def css(path):
    return render_template(path)


@app.route('/pictures/<path:path>')
def picture(path):
    if path[0] == '1':
        if os.path.isfile(f'static/pictures/{path}'):
            return send_file(f'static/pictures/{path}', mimetype='image/gif')
        else:
            df = make_df(path[1:-4])
            fig, ax = plt.subplots()
            y = [df['Members Total'].sum(), df['Members Watching'].sum(),
                    df['Members Completed'].sum(), df['Members On-Hold'].sum(),
                    df['Members Dropped'].sum(), df['Members Plan to Watch'].sum()]
            x = ['Total', 'Watching', 'Completed', 'On-Hold', 'Dropped', 'Plan to Watch']
            ax.bar(x, y, color='#FFAD33')
            ax.set_xticklabels(x, rotation=19)
            ax.set_title(f'Распределение состояний', color='black')
            b = sum(y)
            y1 = list(map(lambda x: x / b, y))
            for i, v in enumerate(y):
                ax.text(i, v / 2, "{:.1%}".format(y1[i]), color='black', ha='center', fontsize=9)
            fig.savefig(f'static/pictures/{path}', transparent=True, dpi=200)
            return send_file(f'static/pictures/{path}', mimetype='image/gif')
    elif path[0] == '2':
        if os.path.isfile(f'static/pictures/{path}'):
            return send_file(f'static/pictures/{path}', mimetype='image/gif')
        else:
            df = make_df_percent(path[1:-4])
            y = [df['Members score 10'].sum(), df['Members score 9'].sum(),
                    df['Members score 8'].sum(), df['Members score 7'].sum(),
                    df['Members score 6'].sum(), df['Members score 5'].sum(),
                    df['Members score 4'].sum(), df['Members score 3'].sum(),
                    df['Members score 2'].sum(), df['Members score 1'].sum()]
            x = ['10', '9', '8', '7', '6', '5', '4', '3', '2', '1']
            b = sum(y)
            y = list(map(lambda x: x / b, y))
            fig, ax = plt.subplots()
            ax.bar(x, y, color='#FFAD33')
            for i, v in enumerate(y):
                ax.text(i, v / 2, "{:.1%}".format(v), color='black', ha='center', fontsize=9)
            ax.set_title(f'Уравновешивание аниме', color='black')
            fig.savefig(f'static/pictures/{path}', transparent=True, dpi=200)
            return send_file(f'static/pictures/{path}', mimetype='image/gif')
    elif path[0] == '3':
        if os.path.isfile(f'static/pictures/{path}'):
            return send_file(f'static/pictures/{path}', mimetype='image/gif')
        else:
            df = make_df(path[1:-4])
            fig, ax = plt.subplots()
            y = [df['Members score 10'].sum(), df['Members score 9'].sum(),
                    df['Members score 8'].sum(), df['Members score 7'].sum(),
                    df['Members score 6'].sum(), df['Members score 5'].sum(),
                    df['Members score 4'].sum(), df['Members score 3'].sum(),
                    df['Members score 2'].sum(), df['Members score 1'].sum()]
            x = ['10', '9', '8', '7', '6', '5', '4', '3', '2', '1']
            ax.bar(x, y, color='#FFAD33')
            b = sum(y)
            y1 = list(map(lambda x: x / b, y))
            for i, v in enumerate(y):
                ax.text(i, v / 2, "{:.1%}".format(y1[i]), color='black', ha='center', fontsize=9)
            ax.set_title(f"По количеству оценок", color='black')
            fig.savefig(f'static/pictures/{path}', transparent=True, dpi=200)
            return send_file(f'static/pictures/{path}', mimetype='image/gif')


if __name__ == '__main__':
    app.run()
