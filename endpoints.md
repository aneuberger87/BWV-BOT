# Backend API Endpoints

## GET Endpoints

### Base Path: `/`

- `/companies`
  - Retrieves a list of all companies.

- `/students`
  - Fetches a list of all students.

- `/rooms`
  - Gets a list of all rooms.

- `/attendanceList`
  - Retrieves an attendance list for events.

- `calculate`
  - Triggers a backend script execution for data processing or analysis.

## POST Endpoints

### Base Path: `/`

- `/roomsList`
  - `fileLocation`: Location of the Excel file.
    - Uploads and processes a room list from an Excel file.

- `/companiesList`
  - `fileLocation`: Location of the Excel file.
    - Posts a list of companies from an Excel file for updating company records.

- `/studentsList`
  - `fileLocation`: Location of the Excel file.
    - Submits a student list from an Excel file for bulk updates.

### Base Path: `update`

- `/update/studentsList`
  - `studentsList`: New list of student preferences.
    - Updates the list of student preferences with a provided list.

- `/update/allocation/studentsList`
  - `studentsList`: New list of student allocations.
    - Updates the list of student allocations with a provided list.

- `/update/companiesList`
  - `companiesList`: New list of companies.
    - Updates the list of companies directly with a provided list.

- `/update/timetableList`
  - Requires a JSON string in the request body.
    - Updates the timetable list based on a provided JSON string.

### Base Path: `print`

- `/print/attendanceList`
  - `fileLocation`: Location of the Excel file.
    - Generates and saves an attendance list to an Excel file.

- `/print/timetableList`
  - `fileLocation`: Location of the Excel file.
    - Outputs a timetable list to an Excel file.

- `/print/roomAssignmentsList`
  - `fileLocation`: Location of the Excel file.
    - Exports a list of room assignments to an Excel file.
