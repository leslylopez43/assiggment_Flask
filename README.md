# Flask Motoring App
Motoring App is a web application built with Flask that allows users to manage suppliers, vehicles, sales, and maintenance information in a motoring business.

## Prerequisites

- Python 3.6 or higher
- Flask
- psycopg2


## Installation
1. The repository:

 https://github.com/your-username/flask-motoring-app.git


cd flask-motoring-app

2. Configure the PostgreSQL database:

 ### Install the required dependencies or packages.
pip install -r requirements.txt

3. ### Set up the PostgreSQL database:
- Create a new database named "motoring" on your PostgreSQL server.
- Update the database connection details in the `db_conn` function in `app.py` with your PostgreSQL credentials.

Start the application:
The application will be accessible at http://localhost:5000.

## Usage
The application provides the following pages

# British Fleet
## Features
#### Displays the main page of the application.
View and search for supplier details.
Supplier: http://localhost:5000/supplier

#### Displays a list of suppliers and their details.
View and search for vehicle details.
Vehicles: http://localhost:5000/vehicles

#### Displays a list of vehicles and their details.
View and search for sales details.
Sales: http://localhost:5000/sales

#### Displays a list of sales and their details.
View and search for maintenance details.
Maintenance: http://localhost:5000/maintenance

#### Displays the maintenance page.
- Click on the links in the navigation menu to access the respective pages.
Search: http://localhost:5000/search

# British Fleet

British Fleet is a web application for managing supplier information, displaying vehicles, managing sales, and managing maintenance/services. 
It is built using ,  and 
|     Flask | Python,| Bootstrap.|
| --------  | -------- |-------- |
### Usage 
Upon accessing the application, you will see a navigation bar with links to different sections of the application.
Click on the respective links to navigate to the desired section (e.g., Display Supplier, Display Vehicles, Manage Sales, Manage Maintenance/Services).
In the navigation bar, you can also choose an option from the dropdown menu and click "Submit" to directly navigate to a specific section.
Each section provides specific functionality related to its purpose (e.g., displaying, managing, or tracking relevant data).
Feel free to explore and use the application according to your requirements.

## Technologies Used

- Python
- Flask
- HTML
- CSS
- Bootstrap

# Feature 
# Home Page

The Home page is the landing page of the British Fleet application. It provides an overview of the different management sections available in the application, including Supplier, Vehicles, and Sales.

## Usage

1. When you access the British Fleet application, you will be directed to the Home page.

2. On the Home page, you will see the following headings:
   - "Manage Supplier": Clicking on this heading will navigate you to the Supplier management section.
   - "Manage Vehicles": Clicking on this heading will navigate you to the Vehicles management section.
   - "Manage Sales": Clicking on this heading will navigate you to the Sales management section.

3. Depending on your needs, you can click on the corresponding heading to access the desired management section.

4. Each management section provides specific functionality and features for managing suppliers, vehicles, and sales within the British Fleet application.

# Supplier Management Page

The Supplier Management page is a part of the British Fleet application. It allows users to view and manage supplier details. This page displays a table with supplier information and provides options to add new supplier details through forms.

## Usage

1. When you access the British Fleet application and navigate to the Supplier Management page, you will see a table displaying existing supplier details.

2. The table consists of columns representing different attributes of the suppliers, such as ID, Name, Contact, Address, etc.

3. You can view and scroll through the supplier information in the table.

4. To add new supplier details, click on one of the available forms listed under the "Forms" section:
   - "Enter New Supplier Details": Clicking on this form will allow you to enter and submit new supplier details.
   - "Enter New Vehicle Details": Clicking on this form will allow you to enter and submit new vehicle details.
   - "Enter New Sales Details": Clicking on this form will allow you to enter and submit new sales details.
   - "Enter New Maintenance Details": Clicking on this form will allow you to enter and submit new maintenance details.

5. After submitting the form, the new supplier details will be added to the table.

## Services Data Management System

This project is a Services Data Management System that allows you to track and manage maintenance records for vehicles. It provides a web-based interface for searching, adding, updating, and deleting maintenance records. The system is built using Python and the Flask web framework.

#### Features

- Search for Car Maintenance: Users can search for specific maintenance records by entering relevant keywords or criteria.
- Add Maintenance Record: Users can add new maintenance records by providing necessary details such as vehicle ID, registration number, date performed, tasks/services, and more.
- Update Maintenance Record: Users can update existing maintenance records to reflect any changes or updates.
- Delete Maintenance Record: Users can remove maintenance records that are no longer needed.
- Print Maintenance Record: Users can print out maintenance records for reference or documentation purposes.

### Usage

Upon accessing the application, you will be presented with a table displaying existing maintenance records.
You can use the search form to find specific maintenance records by entering relevant keywords or criteria.
To add a new maintenance record, click on the "Add MAINTENANCE RECORD" link and fill in the necessary details in the provided form.
To update or delete a maintenance record, click on the respective links in the table.
You can also print out a maintenance record by clicking on the "Print" link.
To return to the main menu, click on the "Go to Menu" button.
Contributing

# Supplier Creation Form

The Supplier Creation Form is a part of the British Fleet application. It allows users to create a new supplier by filling out a form. The form collects information such as Supplier ID, Address, Mobile Phone, Email Address, and Contact Name.

## Usage

1. When you access the British Fleet application and navigate to the Supplier Creation Form page, you will see a form with input fields for Supplier ID, Address, Mobile Phone, Email Address, and Contact Name.

2. Fill out the form by entering the required details for the new supplier.

3. Click the "Create" button to submit the form and create a new supplier with the provided information.

4. After submitting the form, the new supplier will be added to the system.

# Delete Supplier Page

The Delete Supplier page is a web page in the British Fleet application that allows users to delete a supplier from the system. It is built using HTML and integrates with the Flask framework.

## Usage

1. Access the Delete Supplier page by navigating to the respective section in the British Fleet application.

2. On the Delete Supplier page, you will see a confirmation message asking if you want to delete the supplier.

3. If you want to proceed with the deletion, click the "Delete" button.

4. The system will process the deletion request and remove the supplier from the database.

5. After deleting the supplier, you will be redirected to the application's index page.

6. If you decide not to delete the supplier, you can click the "go to menu" link to return to the main menu without making any changes.

# Supplier Search Data Table

The Supplier Search Data Table is a component of the British Fleet application. It allows users to search for suppliers based on specific criteria and displays the search results in a table.

## Usage

1. When you access the British Fleet application and navigate to the Supplier Search Data Table, you will see a search form and a table.

2. In the search form, enter a search term in the "Search" input field that matches the criteria you want to search for among the suppliers.

3. Click the "Submit" button to initiate the search.

4. The table will dynamically update to display the search results. Each row represents a supplier that matches the search criteria.

5. The columns in the table display different attributes of the suppliers, such as the supplier ID, company name, address, post code, mobile phone, email address, and contact name.

6. You can perform multiple searches by entering different search terms in the input field and clicking the "Submit" button again.

7. To return to the main menu, click the "Go to Menu" button.

# Supplier Update Form

The Supplier Update Form is a component of the British Fleet application. It allows users to update supplier information by selecting a supplier from a dropdown menu and entering updated details.

## Usage

1. When you access the British Fleet application and navigate to the Supplier Update Form, you will see a form for updating supplier information.

2. In the "Select Supplier" dropdown menu, choose the supplier you want to update.

3. Enter the updated company name in the "Company Name" input field.

4. Enter the updated address in the "Address" input field.

5. Enter the updated mobile phone number in the "Mobile Phone" input field.

6. Enter the updated email address in the "Email Address" input field.

7. Enter the updated contact name in the "Contact Name" input field.

8. Enter the updated VAT (Value Added Tax) information in the "VAT" input field.

9. Click the "Update" button to submit the updated information.

10. The supplier's information will be updated in the system.

11. To return to the main menu, click the "Go to Menu" button.


# print 
To print the supplier's details, click the "Print" button. This will open the browser's print dialog,

## Usage

1. When you access the British Fleet application and navigate to the Supplier Details page, you will see a table displaying the supplier's information.

2. The table includes the following columns: Supplier ID, Supplier Name, Address, Mobile Phone, Email, Contact Name, and VAT.

3. The supplier's information is populated dynamically based on the selected supplier.

4. To view the details of a specific supplier, select the supplier from a dropdown or any other method provided by the application.

5. The table will update to display the information of the selected supplier.

6. To print the supplier's details, click the "Print" button. This will open the browser's print dialog, allowing you to print a physical copy of the supplier's information.

#### Notes

It's important to handle exceptions and errors appropriately when working with database connections and executing SQL statements. This script doesn't include error handling for simplicity.
For more information on using the psycopg2 library, refer to the official documentation: https://www.psycopg.org/

# Maintenance Data Insertion Form

The Maintenance Data Insertion Form is a part of the British Fleet application. It allows users to insert new maintenance data by filling out a form. The form collects information such as Vehicle ID, Registration Number, Date Performed, Task to be Performed, Performed By, Validated By, Material, Labor, and Total.

## Usage

1. When you access the British Fleet application and navigate to the Maintenance Data Insertion Form page, you will see a form with input fields for Vehicle ID, Registration Number, Date Performed, Task to be Performed, Performed By, Validated By, Material, Labor, and Total.

2. Fill out the form by entering the required details for the maintenance data.

3. Click the "Services/Create" button to submit the form and insert the new maintenance data with the provided information.

4. After submitting the form, the new maintenance data will be added to the system.

# Sales Data Table

The Sales Data Table is a component of the British Fleet application. It displays a table of sales data, including information such as the sale employee number, new car brand, used car brand, number of used cars sold, profit from new cars, profit from used cars, profit, vehicle category, and number of new cars sold.

## Usage

1. When you access the British Fleet application and navigate to the Sales Data Table, you will see a table displaying the sales data.

2. You can search for specific sales data by entering a search term in the "Search for Sales" input field and clicking the "Search" button.

3. The table will dynamically update to show the sales data that matches the search term.

4. The sales data is displayed in rows, with each row representing a sales entry. The columns represent different attributes of the sales data.

5. Each row has links to update, delete, or print the sales entry. Clicking the "Update" link allows you to update the sales information. Clicking the "Delete" link removes the sales entry from the database. Clicking the "Print" link prints the sales details.

6. You can click the "Add Sales" link to navigate to the page for adding new sales.

7. To return to the main menu, click the "Go to Menu" button.

# Sales Form

The Sales Form is a part of the British Fleet application. It allows users to enter sales data related to new and used cars. The form collects information such as the sale employee number, new car brand, used car brand, number of used cars sold, profit from new cars, profit from used cars, profit, vehicle category, and number of new cars sold.

## Usage

1. When you access the British Fleet application and navigate to the Sales Form, you will see a form for entering sales data.

2. Fill in the required fields such as sale employee number, new car brand, used car brand, number of used cars sold, profit from new cars, profit from used cars, profit, vehicle category, and number of new cars sold.

3. Submit the form by clicking the "Submit" button.

4. The data entered will be sent to the backend and processed to store the sales information in the database.

5. You can click the "Go to Menu" button to return to the main menu.



# New Vehicles Details Form

The New Vehicles Details Form is a part of the British Fleet application. It allows users to enter information about new vehicles, including the registration number, brand, model, color, price, car year, on-stock date, and availability.

## Usage

1. When you access the British Fleet application and navigate to the New Vehicles Details Form, you will see a form for entering new vehicle information.

2. Fill in the required fields such as the registration number, brand, model, color, price, car year, on-stock date, and availability.

3. Submit the form by clicking the "Create Vehicle" button.

4. The data entered will be sent to the backend and processed to store the new vehicle details in the database.

5. You can click the "Go to Menu" button to return to the main menu.

# Vehicle Data Table

The Vehicle Data Table is a component of the British Fleet application. It displays a table of vehicle information and allows users to search for specific vehicles and perform actions such as updating, deleting, and printing vehicle records.

## Usage

1. When you access the British Fleet application and navigate to the Vehicle Data Table, you will see a table displaying vehicle information.

2. In the "Search for Vehicle" input field, enter a search term to filter the displayed vehicles.

3. Click the "Search" button to apply the search filter.

4. The table will update to show only the vehicles that match the search term.

5. Each row in the table represents a vehicle record and displays information such as the vehicle ID, registration number, brand, model, color, price, car year, and availability.

6. To update a vehicle record, click the "Update" link in the corresponding row. This will direct you to the update form for that specific vehicle.

7. To delete a vehicle record, click the "Delete" link in the corresponding row. This will remove the vehicle record from the system.

8. To print a vehicle record, click the "Print" link in the corresponding row. This will generate a printable version of the vehicle information.

9. To add a new vehicle record, click the "Add New vehicle record" link. This will direct you to the form for adding a new vehicle.

10. To return to the main menu, click the "Go to Menu" button.




## License

This project is licensed under the [MIT License](LICENSE).

## Test table
| Test No     | Purpose| Test and Or data|Expected Outcome|Actual Outcome|Comments|
| --------  | -------- |-------- |--------|--------|--------|
| 1         |          |         |        |        |        |
| 2         |          |         |        |        |        |

Performs a search in the database based on the duration of courses.

## Contributing
Contributions are welcome! If you find any issues or have suggestions for improvement, please feel free to open an issue or submit a pull request.

## License
This project is licensed under the MIT License.


