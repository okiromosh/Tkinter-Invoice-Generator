# Invoice Generator

This script generates an invoice using a graphical user interface (GUI). It allows you to enter client details, add items to the invoice, and generate a Word document invoice.

## Prerequisites
- Python 3.x
- `docxtpl` library
- `tkcalendar` library

## Getting Started
1. Install the required libraries by running the following command:
```
pip install docxtpl tkcalendar
```
2. Run the script using the following command:
```
python <script_name>.py
```
3. The GUI window will open, allowing you to create and generate invoices.

## Usage
1. Enter the invoice date using the provided date picker.
2. Fill in the client's name, address, and phone number.
3. Enter the description, quantity, and unit price of each item you want to add to the invoice. Click "Add Item" to add the item to the invoice.
4. The added items will be displayed in a table.
5. Click "Generate Invoice" to create the invoice in Word document format.
6. The generated invoice will be saved with a unique name in the current directory.
7. Click "New Invoice" to clear the form and start a new invoice.

Note: The generated invoice will use a template file named `temp.docx` located in the same directory as the script. Make sure to provide a valid template file or customize the script according to your needs.

Feel free to modify the script to suit your specific requirements.
