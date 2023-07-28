### App for Flask Motoring
Users of the Motoring App can handle suppliers, vehicles, sales, and maintenance data in a motoring business. It was created using the Flask programming language.

## Prerequisites

- Python 3.6 or higher
- Flask
- psycopg2


## Installation
1. The repository:

https://motoring-web-services.onrender.com

![repositori 2](/static/img/repositor2.webp)
![repositori3](/static/img/repositor3.webp)
![repositori 4](/static/img/repositor4.webp)
![repositori 5](/static/img/repositor5.webp)

cd flask-motoring-app

2. Configure the PostgreSQL database:

 ### Install the required dependencies or packages.
pip install -r requirements.txt

3. ### Set up the PostgreSQL database:
- Create a new database named "motoring" on your PostgreSQL server.
- Update the database connection details in the `db_conn` function in `app.py` with your PostgreSQL credentials.

## Tables Design in SQL Data Base
   I create a 4 tables each table have at least 10 rows that save the data

## Table: MAINTENANCE

### Description:
The "MAINTENANCE" table stores records related to the maintenance of vehicles. It includes information about maintenance tasks performed on vehicles, the date of maintenance, costs, and personnel involved.

#### Data Storage:
Each row in the "MAINTENANCE" table represents a specific maintenance event performed on a vehicle. The table includes various fields to store relevant information about each maintenance event:

| Field Name                   | Data Type   | Description                                                      |
|------------------------------|-------------|------------------------------------------------------------------|
| maintenanceid (Primary Key)  | number     | A unique identifier for each maintenance record (auto-incremented)|
| vehicle_id (Foreign Key)     | number     | References the vehicle for which the maintenance was performed   |
| registration_number          | number      | The registration number of the vehicle that underwent maintenance|
| date_performed               | Date        | The date when the maintenance was performed                      |
| task_to_be_performed_services| text      | Description of the maintenance task or service                    |
| performed_by                 | text      | Name or ID of the person or team who performed the maintenance   |
| validate_by                  | text      | Name or ID of the person who validated or approved the maintenance work |
| material                     | price     | The cost of materials used during the maintenance                |
| labor                        | price     | The cost of labor involved in performing the maintenance         |
| total                        | price     | The total cost of the maintenance, including materials and labor  |

## Table: SALES
### Description:
The "SALES" table stores records related to vehicle sales. It includes information about new and used car sales, the number of cars sold, profits, and employee details.

#### Data Storage:
Each row in the "SALES" table represents a specific sales transaction or event. The table includes various fields to store relevant information about each sale:

| Field Name                   | Data Type   | Description                                                              |
|------------------------------|-------------|--------------------------------------------------------------------------|
| salesid (Primary Key)        | number     | A unique identifier for each sales record (auto-incremented)             |
| sale_employee_number         | number     | The employee number of the salesperson responsible for the transaction   |
| new_car_brand                | text      | The brand of the new car sold                                            |
| used_car_brand               | text      | The brand of the used car sold                                           |
| number_of_used_cars_sold     | number     | The number of used cars sold in the transaction                          |
| profit_from_new_cars         | price     | The profit generated from selling new cars                               |
| profit_from_used_cars        | price     | The profit generated from selling used cars                              |
| profit                       | price     | The total profit from the sales transaction                              |
| vehicle_category             | text      | The category of the vehicles sold                                        |
| number_of_new_cars_sold      | number     | The number of new cars sold in the transaction                           |

## Table: SUPPLIER
#### Description:
The "SUPPLIER" table stores records related to suppliers who provide goods or services to the organization. It includes contact and business details of the suppliers.

#### Data Storage:
Each row in the "SUPPLIER" table represents a specific supplier. The table includes various fields to store relevant information about each supplier:


| Field Name                   | Data Type   | Description                                                      |
|------------------------------|-------------|------------------------------------------------------------------|
| supplierid (Primary Key)     | number     | A unique identifier for each supplier (auto-incremented)        |
| supplier_name                | name      | The name of the supplier                                         |
| address                      | text      | The address of the supplier                                      |
| mobile_phone                 | number      | The mobile phone number of the supplier                          |
| email                        | email      | The email address of the supplier                                |
| contact_name                 | text      | The name of the contact person at the supplier's organization    |
| vat                          | number      | The VAT (Value Added Tax) number of the supplier                 |

## Table: VEHICLES
#### Description:
The "VEHICLES" table stores records related to the vehicles owned or operated by the organization. It includes information about each vehicle, such as its registration details, pricing, and availability.

#### Data Storage:
Each row in the "VEHICLES" table represents a specific vehicle owned or available for sale. The table includes various fields to store relevant information about each vehicle:

| Field Name                   | Data Type   | Description                                                      |
|------------------------------|-------------|------------------------------------------------------------------|
| vehiclesid (Primary Key)     | number     | A unique identifier for each vehicle (auto-incremented)          |
| registration_number          | number      | The registration number of the vehicle                           |
| brand                        | text      | The brand or make of the vehicle                                 |
| model                        | text      | The model name or number of the vehicle                          |
| color                        | text      | The color of the vehicle                                         |
| price                        | price     | The price of the vehicle                                         |
| car_year                     | text     | The manufacturing year of the vehicle                            |
| on_stock_from                | date        | The date when the vehicle became available in stock              |
| available                    | text     | Indicates whether the vehicle is available for purchase          |


Start the application:
The application will be accessible at http://localhost:5000.



### Chrome Lighthouse Test Results

We use Chrome Lighthouse to evaluate the performance and accessibility of our web application. The following screenshots highlight some of the key metrics:

![Screenshot 1](/static/img/index%20lighthouse.webp)
*Figure 1: Performance score as reported by Chrome Lighthouse.*

![Accessibility Score](/static/img/supplier%20lighthouse.webp)
*Figure 2: Accessibility score as reported by Chrome Lighthouse.*

![Accessibility Score](/static/img/new_vehicles%20lighthouse.webp)
*Figure 3: Accessibility score as reported by Chrome Lighthouse.*

![Accessibility Score](/static/img/sale-form%20light%20house.webp)
*Figure 4: Accessibility score as reported by Chrome Lighthouse.*

![Accessibility Score](/static/img/maintenance%20lighthouse.webp)
*Figure 5: Accessibility score as reported by Chrome Lighthouse.*

## PEP 8 Code Style Check
This project follows the PEP 8 style guidelines to maintain a consistent and readable codebase. To ensure adherence to these guidelines, we use the pycodestyle tool to check our Python code for style violations.

### Installation
To check your Python code against the PEP 8 style guidelines, you need to have pycodestyle installed.  

1. **Install `pycodestyle`**:
   If you haven't installed `pycodestyle` yet, you can find it on PyPI (Python Package Index) at the following link:
   [pycodestyle on PyPI](https://pypi.org/project/pycodestyle/)

   You can install `pycodestyle` using `pip` by running the following command:

2. **Run `pycodestyle` on your Python file**:
Open a terminal or command prompt and execute the following command:
Replace `nameofpythonfile.py` with the actual name of the Python file you want to test.

3. **Review the output**:
If there are no errors or warnings displayed in the output, it means your code meets the PEP 8 standards.



## Running PEP 8 Check
Once you have pycodestyle installed, you can run the following command in your terminal or command prompt to check a specific Python file:

## About PEP 8
PEP 8 is the official style guide for Python code, providing guidelines on how to format and structure your code to enhance readability and maintainability. Adhering to PEP 8 helps create a consistent coding style across the Python community.

For more information on PEP 8, you can visit the official Python website: PEP 8 -- Style Guide for Python Code

## Additional Resources
|     pycodestyle on PyPI | | PEP 8 on Python.org|
| --------  | -------- |-------- |


## Usage
The application provides the following pages

# British Fleet
## Features
#### Displays the main page of the application.
View and search for supplier details.
Supplier's website is located at localhost:5000.

### Displays a list of suppliers together with their information.
View and search for vehicle details.
Vehicles: http://localhost:5000/vehicles

#### Displays a list of vehicles and their details.
View and search for sales details.
Sales: http://localhost:5000/sales

#### Displays a list of sales and their details.
View and search for maintenance details.
Maintenance: http://localhost:5000/maintenance

#### Displays the maintenance page.
- To reach the corresponding pages, click on the links in the navigation menu.
Visit localhost:5000 to perform a search.

# British Fleet

British Fleet is a web application for managing supplier information, displaying vehicles, managing sales, and managing maintenance/services. 
It is built using ,  and 
|     Flask | Python,| Bootstrap.|
| --------  | -------- |-------- |
### Usage 
You will see a navigation bar with links to the application's many sections when you first view it.
Click on the pertinent links (such as Display Supplier, Display Vehicles, Manage Sales, or Manage Maintenance/Services) to reach the necessary section.
To get directly there, you may also choose a section from the drop-down menu and click "Submit" in the navigation bar.

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

1. The Home page will be displayed when you access the British Fleet application.

2. The following headings can be found on the Home page:
   - With "Manage Supplier": You can access the Supplier management area by clicking this heading.
   - "Manage Vehicles": Clicking on this heading will navigate you to the Vehicles management section.
   - "Manage Sales": Clicking on this heading will navigate you to the Sales management section.

3. Depending on your needs, you can click on the corresponding heading to access the desired management section.

4. Each management section provides specific functionality and features for managing suppliers, vehicles, and sales within the British Fleet application.

# Supplier Management Page

The Supplier Management page is a part of the British Fleet application. It allows users to view and manage supplier details. This page displays a table with supplier information and provides options to add new supplier details through forms.

## Usage

1. When you access the British Fleet application and navigate to the Supplier Management page, you will see a table displaying existing supplier details.

2. The table has columns for the providers' various characteristics, including ID, Name, Contact, Address, etc.

3. The table's supplier information is viewable and scrollable.

4. To add new supplier details, click on one of the available forms listed under the "Forms" section:
   - "Enter New Supplier Details": Clicking on this form will allow you to enter and submit new supplier details.
   - "Enter New Vehicle Details": Clicking on this form will allow you to enter and submit new vehicle details.
   - "Enter New Sales Details": Clicking on this form will allow you to enter and submit new sales details.
   - "Enter New Maintenance Details": Clicking on this form will allow you to enter and submit new maintenance details.

5. After submitting the form, the new supplier details will be added to the table.

## Services Data Management System

This project is a services data management system that enables you to monitor and control vehicle maintenance logs. For searching, adding, amending, and removing maintenance records, it offers a web-based interface. The Flask web framework and Python are used to create the system.

#### Features

- Search for Car Maintenance: Users can search for specific maintenance records by entering relevant keywords or criteria.
- Add Maintenance Record: Users can add new maintenance records by providing necessary details such as vehicle ID, registration number, date performed, tasks/services, and more.
- Update Maintenance Record: Users can update existing maintenance records to reflect any changes or updates.
- Delete Maintenance Record: Users can remove maintenance records that are no longer needed.
- Print Maintenance Record: Users can print out maintenance records for reference or documentation purposes.

### Usage

Using the search form, you may input pertinent keywords or other criteria to find particular maintenance records.
Click the "Add MAINTENANCE RECORD" link and complete the fields in the supplied form to add a new maintenance record.
Click on the corresponding links in the table to edit or delete a maintenance record.
By choosing the "Print" link, you may also print a maintenance log.
To return to the top menu, click the "Go to Menu" button.

##### Contributing

# Supplier Creation Form

The Supplier Creation Form is a part of the British Fleet application. By completing a form, users can create new suppliers. The form asks for details such the contact name, email address, mobile phone number, and supplier ID.

## Usage

1. When you access the British Fleet application and navigate to the Supplier Creation Form page, you will see a form with input fields for Supplier ID, Address, Mobile Phone, Email Address, and Contact Name.

2. Fill out the form by entering the required details for the new supplier.

3. Click the "Create" button to send the form and create a new supplier using the provided data.

4. The new supplier will be added to the system after the form has been submitted.

# Delete Supplier Page

The Delete Supplier page is a web page in the British Fleet application that allows users to delete a supplier from the system. It is built using HTML and integrates with the Flask framework.

## Usage

1. Access the Delete Supplier page by navigating to the respective section in the British Fleet application.

2. On the eliminate provider page, a confirmation message will ask you if you really want to eliminate the provider.

3. To continue the deletion, select "Delete" from the menu.

4. Following the system's processing of the deletion request, the provider will be removed from the database.

5. You will be taken to the application's index page after deleting the provider.

6. You can click the "go to menu" option to return to the primary menu without making any changes if you decide not to eliminate the supplier.


# Supplier Search Data Table

The Supplier Search Data Table is a component of the British Fleet application. It allows users to search for suppliers based on specific criteria and displays the search results in a table.

## Usage

1. A search form and a table are visible when you enter the British Fleet programme and select the Supplier Search Data Table.

2. In the search form, type a search word that satisfies the requirements you wish to look for among the suppliers in the "Search" input area.

3. To start the search, click the "Submit" button.

4. The table displaying the search results will be dynamically updated. A row represents each supplier that fits the search criteria.

5. The columns of the table include the supplier ID, firm name, address, postcode, phone number, email address, and contact name, among other supplier details.

6. By modifying your search parameters and then clicking the "Submit" button a second time, you can carry out a variety of searches.

7. Press the "Go to Menu" button to return to the main menu.


# Supplier Update Form

The Supplier Update Form is a component of the British Fleet application. It allows users to update supplier information by selecting a supplier from a dropdown menu and entering updated details.

## Usage

1. When you access the British Fleet application and navigate to the Supplier Update Form, you will see a form for updating supplier information.

2. Select the provider you want to edit from the "Select Supplier" selection option.

3. Fill up the "Company Name" input form with the new firm name.

4. Enter the updated address in the "Address" input field.

5. Fill out the "Mobile Phone" input area with the updated mobile number.

6. Fill out the "Email Address" input area with the changed email address.

7. Fill out the "Contact Name" input field with the updated contact's name.

8. Fill out the "VAT" input field with the most recent VAT (Value Added Tax) information.

9. To send the revised information, click the "Update" button.

10. The system will be updated with the data from the supplier.

11. Choose "Go to Menu" to go back to the main menu.

# print 
Click the "Print" button to print the supplier's information. This will launch the print dialogue for the browser.

## Usage

1. A table with the supplier's details will appear when you visit the British Fleet application and go to the Supplier Details page.
2. The table has the following columns: VAT, Contact Name, Address, Mobile Phone, Supplier ID, and Supplier Name.
3. The supplier's information is populated dynamically based on the selected supplier.

4. To view the details of a specific supplier, select the supplier from a dropdown or any other method provided by the application.

5. The table will update to display the information of the selected supplier.

6. Select "Print" to print the supplier's information. By doing this, you can access the print dialogue in your browser and print a hard copy of the supplier's details.

#### Notes

It's important to handle exceptions and errors properly while working with database connections and executing SQL statements. The objective of this script's brevity is to avoid including error handling.
Visit https://www.psycopg.org/ to see official guidelines on how to use the psycopg2 library.
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

1. You will see a table with the sales data when you enter the British Fleet programme and navigate to the Sales Data Table.

2. You can search for certain sales data by entering a search word in the "Search for Sales" input field and pressing the "Search" button.

3. The table will dynamically refresh with the sales data relevant to the search keyword.

4. The sales data is displayed in rows, with each row representing a sales entry. The columns represent different attributes of the sales data.

5. Each row has links to update, delete, or print the sales entry. Clicking the "Update" link allows you to update the sales information. Clicking the "Delete" link removes the sales entry from the database. Clicking the "Print" link prints the sales details.

6. Click "Add Sales" to see the page where you may enter new sales.

7. Press the "Go to Menu" button to return to the main menu.

# Sales Form

The Sales Form is a part of the British Fleet application. It allows users to enter sales data related to new and used cars. The form collects information such as the sale employee number, new car brand, used car brand, number of used cars sold, profit from new cars, profit from used cars, profit, vehicle category, and number of new cars sold.

## Usage

1. When you access the British Fleet application and navigate to the Sales Form, you will see a form for entering sales data.

2. Complete the relevant fields, including the sale employee number, the brand of the new and used cars sold, the number of used cars sold, the profit from new and used cars, the vehicle type, and the quantity of new cars sold.

3. To transmit the form, click the "Submit" button.

4. The backend will receive the entered data and process it before using it to store the sales data in the database.

5. Select "Go to Menu" to return to the primary menu.



# New Vehicles Details Form

The New Vehicles Details Form is a part of the British Fleet application. It allows users to enter information about new vehicles, including the registration number, brand, model, color, price, car year, on-stock date, and availability.

## Usage

1. When you access the British Fleet application and navigate to the New Vehicles Details Form, you will see a form for entering new vehicle information.

2. Complete the fields that are necessary, such the registration number, brand, model, colour, price, year of the vehicle, on-stock date, and availability.

To submit the form, select "Create Vehicle" from the menu.

4. After the data has been entered, the backend will process it and add the new vehicle's information to the database.

5. Select the "Go to Menu" option to return to the main menu.

# Vehicle Data Table

The Vehicle Data Table is a component of the British Fleet application. It displays a table of vehicle information and allows users to search for specific vehicles and perform actions such as updating, deleting, and printing vehicle records.

## Usage

1. When you access the British Fleet application and navigate to the Vehicle Data Table, you will see a table displaying vehicle information.

2. Type a search term into the "Search for Vehicle" input form to narrow the selection of vehicles.

To use the search criteria, click the "Search" button in step 3.

4. The vehicle listings in the amended table will only be those that are relevant to the search term.

5. Each row in the table corresponds to a record for a certain vehicle, and it contains details such as the make, model, colour, price, model year, and availability of the vehicle, as well as its identification number, registration number, and other information.

6. To edit a vehicle record, click the "Update" link in the relevant row. To access the update form for that specific vehicle, you will be directed there.

7. In the corresponding row, click the "Delete" link to remove a vehicle record. The car record will be deleted as a result.

8. To print a vehicle record, select "Print" in the appropriate row. After that, a printable version of the car information will be generated.

9. To add a new vehicle record, click the "Add New Vehicle Record" option. You will be routed there to complete the new car addition form.

10. To get back to the main menu, click the "Go to Menu" button.




## License

This project is licensed under the [MIT License](LICENSE).

## Test table
| Test No     | Purpose| Test and Or data|Expected Outcome|Actual Outcome|Comments|
| --------  | -------- |-------- |--------|--------|--------|
| 1         |          |         |        |        |        |
| 2         |          |         |        |        |        |

based on the length of the courses, does a database search.

## Contributing We encourage contributions! Feel free to raise an issue or send a pull request if you discover any problems or have ideas for improvement.

## Permit
The MIT Licence applies to this project.


