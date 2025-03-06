# Algerian Forest Fire Prediction ML Project

This project predicts the occurrence and severity of forest fires in Algeria using machine learning models. The project utilizes a Flask web application to provide an interface for users to input weather and fire-related data and receive predictions.

## Project Structure

- `application.py`: The main Flask application that handles routes and predictions.
- `requirements.txt`: Contains the dependencies required to run the project.
- `env/`: Directory for environment-related files.
- `models/`: Directory containing the machine learning models and scaler.
- `notebooks/`: Directory for Jupyter notebooks related to the project.
- `templates/`: Directory containing HTML templates for the Flask application.

## Installation

To run this project, you need to have Python installed. Follow the steps below to set up the environment:

1. Clone the repository:
   ```bash
   git clone https://github.com/saifimd1234/AlgerianForestFireML_Project.git
   cd AlgerianForestFireML_Project
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

To start the Flask application, run the following command:
```bash
python application.py
```

The application will be accessible at `http://0.0.0.0:5000/`.

### Routes

- `/`: Home page.
- `/predictdata`: Endpoint to submit data for prediction.

## Languages Used

- Jupyter Notebook: 99.6%
- Other: 0.4%

## Example

To predict the forest fire severity, input the following data:

- Temperature (°C)
- Relative Humidity (%)
- Wind Speed (km/h)
- Rain (mm/m²)
- Fine Fuel Moisture Code (FFMC)
- Duff Moisture Code (DMC)
- Initial Spread Index (ISI)
- Classes (Fire severity class)
- Region (Region code)

The model will return the predicted severity of the forest fire.

## License

This project is licensed under the MIT License.
```
