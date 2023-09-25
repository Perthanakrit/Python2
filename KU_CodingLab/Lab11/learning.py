# 1) Indexing (Access)
def access_index():
    subject = 'Fundamental Programming Concept'
    text = subject[-22] * 5 + subject[0] * 0
    print(text)
#access_index()

# 2) String index out of range

# 3) Strings are immutable (ไม่สามารถเปลี่ยนแปลง)

'''
4) Slicing
   [string:step:stop-1] 
'''
def slicing():
    subject = "Fundamental Programming Concept"
    print(1, subject[:23])
    print(2, subject[:23:1])
    print(3, subject[:23:2])


slicing()