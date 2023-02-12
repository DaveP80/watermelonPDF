### flask python

**activate a virtual environment**

```
pip3 install -r requirements.txt
```
```
mkdir server/src/output
mkdir server/src/static
```
declare your `SECRET_KEY`

A user can upload (only) pdf files. then the program removes
"frontmatter" i.e. pages from the table of contents with headers such as, 'half title','title','title page','about the author','copyright','contents','author','introduction',
'references','glossary','index','notes','key terms','conclusions','appendix','appendix:','foreword','biography',
'dedication','disclaimers','preface','safety notices','number of printings'
'acknowledgments','afterword','postscript','prologue','bibliography'

### feature

the next page rendered contains a window with a pdf viewer with the newly
formatted pdf document.

**note**

pdf documents with less than 20 pages are returned, pdf files with unclear table of contents are 
returned with a download line of `SoftDuplicateTrynewPdf.pdf`

url: https://watermelonpdf.org
