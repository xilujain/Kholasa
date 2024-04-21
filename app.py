from __future__ import unicode_literals
from flask import Flask, render_template, request
from spacy_summarization import text_summarizer
from bs4 import BeautifulSoup
from urllib.request import urlopen
import spacy

nlp = spacy.load("en_core_web_sm")
app = Flask(__name__)


# Fetch Text From Url
def get_text(url):
    page = urlopen(url)
    soup = BeautifulSoup(page, "html.parser")
    fetched_text = ' '.join(map(lambda p: p.text, soup.find_all('p')))
    return fetched_text


@app.route('/')
def kholasa():
    return render_template('index.html')


@app.route('/analyze_url', methods=['GET', 'POST'])
def analyze_url():
    rawtext = ''
    final_summary = ''
    raw_url = ''
    section_reserach = ''
    section_summerize = ''
    if request.method == 'POST':
        raw_url = request.form['raw_url']
        rawtext = get_text(raw_url)
        final_summary = text_summarizer(rawtext)
        section_reserach = 'البحث'
        section_summerize = 'الملخص'
    return render_template('index.html', ctext=rawtext, final_summary=final_summary, url=raw_url,
                           section_reserach=section_reserach, section_summerize=section_summerize)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False)
