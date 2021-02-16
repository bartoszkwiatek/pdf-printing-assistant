# PdfPrintingAssistant

## Description

Goal for that program is to assist in printing files from pdf.
Main reason and purpose for this program was to create something that would speed up process of printing technical documentation.
Technical documentation often contains different paper formats in one file: from A4 to A0. Hovewer often we want to print these documents on smaller formats, on regular printer - meaning they have to be either A4 or A3. But problem often occcurs that you have to explicitly select which format that will be: A3 or A4.

## Solution

Program scans directory for .pdf files, and then checks one by one, page by page does following:

- if page is bigger than A3 - scales down to A3
- if it smaller - goes on
  And that is all, output file is pdf made either of A4 or A3 paper.

### Creating .exe file using pyinstaller:

`pyinstaller --onefile PdfChangeFormat.py --name PdfChangeFormat`

### Created using [PyPDF2](https://pypi.org/project/PyPDF2/)
