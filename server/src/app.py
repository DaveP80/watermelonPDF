from flask import Flask, render_template, redirect, url_for, send_from_directory
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from werkzeug.utils import secure_filename
import os
from pathlib import Path
from wtforms.validators import InputRequired
from script import process_pdf
import fitz

app = Flask(__name__, static_folder='staticStyle')
app.config.from_object('config.Config')

class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Upload File")

@app.route('/', methods=['GET',"POST"])
@app.route('/home', methods=['GET',"POST"])
def home():
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data # First grab the file
        def clearDir():    
            for f in Path('./output').glob('*.*'):
                try:
                    f.unlink()
                except OSError as e:
                    print('Error: %s : %s' % (f, e.strerror))
        def clearfDir():
            for f in Path('./static/files').glob('*.*'):
                try:
                    f.unlink()
                except OSError as e:
                    print('Error: %s : %s' % (f, e.strerror))
        clearDir()
        clearfDir()
        loc = os.path.join(os.path.abspath(os.path.dirname(__file__)),app.config['UPLOAD_FOLDER'],secure_filename(file.filename))
        if file.filename[-3:]!='pdf':
            clearfDir()
            return render_template('index.html', form=form, invalid='please upload .pdf')
        file.save(loc) # Then save the file
        doc = fitz.open(loc)
        count = doc.page_count
        if count<20:
            clearfDir()
            return render_template('index.html', form=form, invalid='upload pdf with more than 20 pages!')
        process_pdf(loc)
        return redirect(url_for('download'))
    return render_template('index.html', form=form)

@app.route('/download')
def download():
    return render_template('download.html', files=os.listdir('output'))

@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory('output', filename)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))