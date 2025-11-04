# Receipt Header (multiline string)
header = """\n\t*** WELCOME TO KNOWLEDGE BOOKSTORE ***
\t------------------------------------"""


item1 = "\nBook Title: {}\tPrice: ₹{}".format("Python Basics", 450)
item2 = "\nBook Title: {}\tPrice: ₹{}".format("Data Science Intro", 600)


total = 450 + 600
total_line = "\n\nTotal Amount:\t₹{}".format(total)

thank_you = "\n\n\tTHANK YOU FOR SHOPPING WITH US!"

receipt = header + item1 + item2 + total_line + thank_you


print(receipt.upper())
