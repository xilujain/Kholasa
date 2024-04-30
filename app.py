from __future__ import unicode_literals
from flask import Flask, render_template, request
from spacy_summarization import text_summarizer
from bs4 import BeautifulSoup
from urllib.request import urlopen

import spacy

nlp = spacy.load("en_core_web_sm")

app = Flask(__name__)


def get_text(url):
    page = urlopen(url)
    soup = BeautifulSoup(page, features="html.parser")
    fetched_text = ' '.join(map(lambda p: p.text, soup.find_all('p')))
    return fetched_text


@app.route('/')
def input():
    return render_template('index.html')


@app.route('/analyze_url', methods=['GET', 'POST'])
def analyze_url():
    rawtext = ""
    final_summary = ""
    raw_url = ""
    section_research = ""
    section_summarize = ""
    if request.method == 'POST':
        raw_url = request.form['raw_url']
        rawtext = get_text(raw_url)
        final_summary = text_summarizer(rawtext)
        section_research = "المقالة / البحث"
        section_summarize = "الملخص"
    return render_template('index.html', ctext=rawtext, final_summary=final_summary, url=raw_url,
                           section_reserach=section_research, section_summerize=section_summarize)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')