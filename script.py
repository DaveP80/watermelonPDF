import fitz
import re
from re import search
from pathlib import Path
from PyPDF2 import PdfWriter, PdfReader

def process_pdf(filename):

    file1 = PdfReader(filename)
    doc = fitz.open(filename)
    toc = doc.get_toc()
    #list of nums, begin page and end page
    pagelist = []
    #bad page list
    notpagelist = []

    substring = ['half title','title','title page','about the author','copyright','contents','author','introduction',
    'references','glossary','index','notes','key terms','conclusions','appendix','appendix:','foreword','biography',
    'dedication','disclaimers','preface','safety notices','number of printings'
    'acknowledgments','afterword','postscript','prologue','bibliography']

    print(toc)
    if not toc:
        output_file = './output/SoftDuplicateTrynewPdf.pdf'

        output = PdfWriter()
        for p, page in enumerate(doc):
            if p in range(2, doc.page_count-2):
                page1 = file1.pages[p]
                output.add_page(page1)

    if toc:
        for i, t in enumerate(toc[:len(toc)-1]):
            if len(t[1])<2:
                pass
            else:
                count = 0
                for s in range(len(substring)):
                    if not re.search(substring[s], t[1].lower()):
                        count += 1
                    if re.search(substring[s], t[1].lower()):
                        notpagelist.append(t[2])
                if not pagelist:
                    if count==len(substring):
                        pagelist.append(t[2])
                else:
                    if count==len(substring):
                        pagelist.append(t[2])

        print(pagelist)
        output_file = './output/F'+filename.split('/')[-1:][0]

        output = PdfWriter()
        count = 0
        check = False
        for i in range(len(notpagelist)):
            if notpagelist[i]<pagelist[-1:][0]:
                count += 1
        if count<len(notpagelist):
            check = True
        if count==len(notpagelist):
            innercount = 0
            checklist = pagelist[-10:]
            for r in range(len(checklist)):
                if notpagelist[-1:][0]<checklist[r]:
                    innercount += 1
            if innercount==len(checklist):
                notpagelist= []

        if notpagelist:
            if not check:
                for i in range(len(notpagelist)):
                    if notpagelist[i]<pagelist[-1:][0]:
                        if notpagelist[i]>pagelist[0]:
                            for j in range(len(pagelist)):
                                if pagelist[j]>notpagelist[i]:
                                    #if we have a good not page list
                                    pagelist.remove(pagelist[j])

        for p, page in enumerate(doc):
            if p in range(pagelist[0], pagelist[-1:][0]):
                content = page.get_text()
                page1 = file1.pages[p]
                output.add_page(page1)    
            else:
                if notpagelist:
                    if p in range(pagelist[-1:][0]+1, notpagelist[-1:][0]):
                        content = page.get_text()
                        count = 0
                        for z in range(len(notpagelist)):
                            if notpagelist[z]>pagelist[-1:][0]:
                                if p==notpagelist[z]:
                                    quit()
                        for s in range(len(substring)):
                            if not re.search(substring[s], content[0:25].lower()):
                                count += 1
                        if count==len(substring):
                            page1 = file1.pages[p]
                            output.add_page(page1) 

                if not notpagelist:
                    if p in range(pagelist[-1:][0]+1, doc.page_count):
                        content = page.get_text()
                        count = 0
                        for s in range(len(substring)):
                            if not re.search(substring[s], content[0:25].lower()):
                                count += 1
                            else:
                                quit()
                        if count==len(substring):
                            page1 = file1.pages[p]
                            output.add_page(page1) 

    outputStream = open(output_file, "wb")
    output.write(outputStream)
    outputStream.close()