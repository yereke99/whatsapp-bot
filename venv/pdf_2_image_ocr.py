from pdf2image import convert_from_path
import image_recognation



def pdf_2_image(file_name):
    pages = convert_from_path(file_name, 500,
                              poppler_path=r"C:\Program Files\poppler-20.12.1\Library\bin")
    for i, page in enumerate(pages):
        page.save(f'{file_name}.jpg', 'JPEG')
        name = f'{file_name}.jpg'
        image_recognation.recognition_text(name)




