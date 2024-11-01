# Student RESTful API

This project is a simple RESTful API for managing student records, built using Flask. It supports basic CRUD operations: Create, Read, Update, and Delete for a Student entity.

## Project Setup

### Prerequisites
- Python 3.x
- pip (Python package manager)

### Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/student-api.git
   cd student-api
   ```

2. **Install Dependencies**
   Use the following command to install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**
   Start the Flask server with:
   ```bash
   python app.py
   ```
   The application will run at `http://127.0.0.1:5000/` by default.

## API Endpoints

| Method | Endpoint            | Description                     |
|--------|----------------------|---------------------------------|
| GET    | `/students`         | Retrieve all students           |
| GET    | `/students/{id}`    | Retrieve a student by ID        |
| POST   | `/students`         | Add a new student               |
| PUT    | `/students/{id}`    | Update an existing student by ID|
| DELETE | `/students/{id}`    | Delete a student by ID          |

### Example Requests
You can test the API using tools like `curl`, Postman, or the REST Client in VS Code. Refer to the `test-api.http` file for sample requests.

## Deployment

1. **Deploy to Azure Web App Service**
   - Push your code to GitHub.
   - Set up a new Web App in the Azure portal.
   - Use the Deployment Center to link your GitHub repository and deploy automatically.

2. **Configuration**
   Adjust configurations as necessary in Azure for environment variables or connection strings.

