from pdfminer3.layout import LAParams, LTTextBox
from pdfminer3.pdfpage import PDFPage
from pdfminer3.pdfinterp import PDFResourceManager
from pdfminer3.pdfinterp import PDFPageInterpreter
from pdfminer3.converter import PDFPageAggregator
from pdfminer3.converter import TextConverter
import io

# print(text)


task2file = open("task2.txt","r")
p1_names = []
p2_names = []
p3_names = []
r_names = []
use_data = input("Do you want to use default data? (y/n) ")
if use_data == 'y':
    fileno = 1
    while fileno <= 10:
        resource_manager = PDFResourceManager()
        fake_file_handle = io.StringIO()
        converter = TextConverter(resource_manager, fake_file_handle, laparams=LAParams())
        page_interpreter = PDFPageInterpreter(resource_manager, converter)
        with open('funding_applications/funding_application_'+str(fileno)+'.pdf', 'rb') as fh:
            for page in PDFPage.get_pages(fh, caching=True, check_extractable=True):
                page_interpreter.process_page(page)
            text = fake_file_handle.getvalue()
        converter.close()
        fake_file_handle.close()
        nums = ""
        text = text.split("\n")
        for item in text:
            if item == '':
                text.remove('')
        start_up = text[text.index("Business Name:")+1]
        if fileno == 4:
            start_up = text[text.index("Capability:")+1]
        i = 1
        nums = []
        while len(nums) < 4:
            try:
                nums.append(float(text[text.index("Gut:")+i]))
            except:
                i += 1
            else:
                nums.append(text[text.index("Gut:")+i])
                i += 1
        result = 0
        weighting = [0.3, 0.3, 0.35, 0.05]
        i = 0
        while i < len(nums):
            result += float(nums[i])*weighting[i]
            i += 1
        if result >= 4.0:
            p1_names.append(start_up)
        elif result >= 2.5:
            p2_names.append(start_up)
        elif result >= 1.0:
            p3_names.append(start_up)
        elif result >= 0:
            r_names.append(start_up)
        fileno += 1
else:
    exec(task2file.read())
option = input("1. Present all P1\n2. Present all P2\n3. Present all P3\n4. Present all R\n5. How many businesses do you want to invest in\n6. Terminate\nWhich option do you want to see: ")
while option != '6':
    if option == '1':
        if len(p1_names) != 0:
            print(*p1_names, sep='\n')
        else:
            print("No startup satisfied requirement for P1 ratings.")
    elif option == '2':
        if len(p2_names) != 0:
            print(*p2_names, sep='\n')
        else:
            print("No startup satisfied requirement for P2 ratings.")
    elif option == '3':
        if len(p3_names) != 0:
            print(*p3_names, sep='\n')
        else:
            print("No startup satisfied requirement for P3 ratings.")
    elif option == '4':
        if len(r_names) != 0:
            print(*r_names, sep='\n')
        else:
            print("No startup satisfied requirement for R ratings.")
    elif option == '5':
        if len(p1_names) != 0:
            print(*p1_names, sep=',P1\n', end=',P1\n')
        elif len(p2_names) != 0:
            print(*p2_names, sep=',P2\n', end=',P2\n')
        elif len(p3_names) != 0:
            print(*p3_names, sep=',P3\n', end=',P3\n')
        else:
            print("No startup worth investing in.")
    option = input("1. Present all P1\n2. Present all P2\n3. Present all P3\n4. Present all R\n5. How many businesses do you want to invest in\n6. Terminate\nWhich option do you want to see: ")