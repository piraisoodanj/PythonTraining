import win32com.client

def create_word_document(file_path):
    word = win32com.client.Dispatch("Word.Application")
    word.Visible = True

    doc = word.Documents.Add()

    selection = word.Selection
    selection.TypeText("Helllo word deocument")
    selection.TypeParagraph()
    selection.TypeText("Automation testing")


    #save the document
    doc.SaveAs(file_path)
    #word.Quit()

create_word_document(r"C:\Users\Administrator\Desktop\UST_Training\PYWin_automation\sampledemodoc.docx")