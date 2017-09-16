# 6.5 Write code using find() and string slicing (see section 6.10)
#  to extract the number at the end of the line below.
#  Convert the extracted value to a floating point number and print it out.
text = "X-DSPAM-Confidence:    0.8475";
start_position = text.find('0')
str_number = text[start_position:]
try:
    flt_number = float(str_number)
    print(flt_number)
except:
    print('ññññaaaaaa, wrong extraction')

