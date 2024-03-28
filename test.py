import pdfkit

import base64

image_path = 'C:\\Users\\1661322\\OneDrive\\Рабочий стол\\front\\CV\\img\\my_picture.png'

output_file_path = 'C:\\Users\\1661322\\OneDrive\\Рабочий стол\\front\\CV\\img\\image_base64.txt'

with open(image_path, 'rb') as image_file:
    encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    with open(output_file_path, 'w') as output_file:
        output_file.write(encoded_string)



path_wkhtmltopdf = r'C:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe'
config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

pdfkit.from_file("index.html", "result.pdf", configuration=config)
