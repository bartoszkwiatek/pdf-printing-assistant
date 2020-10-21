from PyPDF2 import PdfFileReader, PdfFileWriter
import os

def dic(x):
    return {
        'RectangleObject([0, 0, 595.276, 841.89])': 'A4',
        'RectangleObject([0, 0, 841.89, 595.276])': 'A4',
        'RectangleObject([0, 0, 1190.55, 841.89])': 'A3',
        'RectangleObject([0, 0, 1683.78, 1190.55])': 'A2',
        'RectangleObject([0, 0, 2383.94, 1683.78])': 'A1',
        }.get(x, 'not found')

def scale_pages(pdf_path):
    if pdf_path.endswith('_converted.pdf'):
        print(pdf_path + ' was already converted\n')
    else:
        pdf_writer = PdfFileWriter()
        pdf_reader = PdfFileReader(pdf_path)
        num_pages = pdf_reader.getNumPages()
        output_name = pdf_path[slice(-4)] + '_converted.pdf'
        for page_num in range(0, num_pages):
            page_content = pdf_reader.getPage(page_num)
            crop_box = page_content.cropBox
            print(f'Page [{str(page_num)}]: {dic(str(crop_box))} - {str(crop_box)}')
            if (crop_box.upperRight[0] > 1190.56):
                page_content.scaleTo(1190.55, 841.89)
                print('      Page ['+ str(page_num) + '] scaled to A3')
            pdf_writer.addPage(page_content)
        with open(output_name, 'wb') as fh:
            pdf_writer.write(fh)

def perform_on_each(extension):
    print("List of files to obliterate:")
    your_dir = os.listdir(".")
    file_list = []
    
    for each in your_dir:
        if each.endswith(extension) or each.endswith(extension.upper()):
            file_list.append(each)
            print(each)

    print('-----------------------------------\n')

    for each in file_list:
        print(f'Casting black magic on file: {each}')
        scale_pages(each)
        print('-----------------------------------\n')
        
if __name__ == '__main__':
    perform_on_each('pdf')
    print('done.')
    os.system("pause")


# A4 RectangleObject([0, 0, 595.276, 841.89])
# A3 RectangleObject([0, 0, 1190.55, 841.89])
# A2 RectangleObject([0, 0, 1683.78, 1190.55])
# A1 RectangleObject([0, 0, 2383.94, 1683.78])