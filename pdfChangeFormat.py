from PyPDF2 import PdfFileReader, PdfFileWriter, PdfFileMerger
import os


def dic(x):
    return {
        "(595, 842)": "A4h",
        "(842, 595)": "A4",
        "(1191, 842)": "A3",
        "(842, 1191)": "A3h",
        "(1684, 1191)": "A2",
        "(1191, 1684)": "A2h",
        "(2384, 1684)": "A1",
        "(1684, 2384)": "A1h",
    }.get(x, "not found")


def scale_pages(pdf_path):
    if pdf_path.endswith("_converted.pdf"):
        print(pdf_path + " was already converted\n")
    else:
        pdf_file = open(pdf_path, "rb")
        pdf_writer = PdfFileWriter()
        pdf_reader = PdfFileReader(pdf_file)
        num_pages = pdf_reader.getNumPages()
        output_name = pdf_path[slice(-4)] + "_converted.pdf"
        for page_num in range(0, num_pages):
            page_content = pdf_reader.getPage(page_num)
            crop_box = page_content.cropBox
            format_paper = dic(
                f"({(round(crop_box.upperRight[0]))}, {round(crop_box.upperRight[1])})"
            )
            print(
                f"Page [{str(page_num)}]: {format_paper} [{round(crop_box.upperRight[0])}, {round(crop_box.upperRight[1])}]"
            )

            if round(crop_box.upperRight[0] > 1191):
                if crop_box.upperRight[0] > crop_box.upperRight[1]:
                    page_content.scaleTo(1191, 842)
                else:
                    page_content.scaleTo(842, 1191)
                print("      Page [" + str(page_num) + "] scaled to A3")
            pdf_writer.addPage(page_content)
        pdf_output_file = open(output_name, "wb")
        pdf_writer.write(pdf_output_file)

        pdf_output_file.close()
        pdf_file.close()
        return output_name


def perform_on_each(extension):
    print("List of files to process:")
    your_dir = os.listdir(".")
    file_list = []

    for each in your_dir:
        if each.endswith(extension) or each.endswith(extension.upper()):
            file_list.append(each)
            print(each)
    print(f"file_list:{file_list}")
    print("-----------------------------------\n")

    performed_on_files = []
    for each in file_list:
        print(f"Casting magic on file: {each}")
        performed_on_files.append(scale_pages(each))

        print("-----------------------------------\n")
    print(performed_on_files)
    return performed_on_files


def merge_pdf_files(files_array):
    # Call the PdfFileMerger
    merged_object = PdfFileMerger()
    # Loop through list append their pages
    for file in files_array:
        if file != None:
            merged_object.append(PdfFileReader(file, "rb"))

    # Write all the files into a file which is named as shown below
    merged_object.write("mergedfilesoutput.pdf")


if __name__ == "__main__":
    files_list = perform_on_each("pdf")
    merge_pdf_files(files_list)
    print("done.")
    os.system("pause")


# A4 RectangleObject([0, 0, 595.276, 841.89])
# A3 RectangleObject([0, 0, 1190.55, 841.89])
# A2 RectangleObject([0, 0, 1683.78, 1190.55])
# A1 RectangleObject([0, 0, 2383.94, 1683.78])
