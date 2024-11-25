# DataCrafters Dashboard

## Overview
The **DataCrafters Dashboard** is a web application for analyzing and visualizing automotive cyber-attack datasets using advanced machine learning algorithms and interactive visualizations.

## Features
### Dynamic Visualizations
- Interactive attack type distribution visualization with toggleable pie and bar chart views
- Real-time animated trend analysis for attack progression patterns
- Customizable correlation heatmaps for identifying attack relationships
- Export capabilities for all visualization types

### Advanced Analytics
- Isolation Forest implementation for detecting anomalies in CAN bus data streams
- Multi-model clustering approach combining DBSCAN and k-means for robust pattern identification
- Configurable anomaly detection thresholds with preset recommendations
- Historical pattern analysis with trend forecasting

### Real-Time Integration
- Mock API interface for development and testing
- Websocket support for live data streaming
- Configurable data refresh rates
- Built-in data validation and sanitization

### Alert System
- Customizable email notifications for detected anomalies
- Severity-based alert prioritization
- Alert history tracking and analysis
- Integration with popular notification platforms

## Project Structure
```
project/
├── app/
│   ├── app.py                  # Flask application core
│   ├── config.py              # Configuration settings
│   └── templates/
│       ├── index.html         # Main dashboard interface
│       ├── analytics.html     # Analytics view
│       └── settings.html      # User settings panel
├── database/
│   ├── db_setup.py           # Database initialization
│   ├── db_queries.py         # Database utility functions
│   └── models.py             # Database models
├── visualizations/
│   ├── main_visualizer.py    # Streamlit visualization core
│   ├── anomaly_detection.py  # Anomaly detection algorithms
│   └── clustering_insights.py # Clustering analysis tools
├── static/
│   ├── css/
│   │   └── styles.css        # Application styling
│   └── js/
│       └── dashboard.js      # Frontend functionality
├── data/
│   ├── DoS_dataset.csv       # Denial of Service attack data
│   ├── Fuzzy_dataset.csv     # Fuzzing attack data
│   ├── gear_dataset.csv      # Gear manipulation data
│   └── RPM_dataset.csv       # RPM tampering data
├── tests/
│   ├── test_analytics.py     # Analytics unit tests
│   └── test_api.py          # API integration tests
├── requirements.txt          # Project dependencies
└── README.md                # This documentation
```

## Installation

### Prerequisites
- Python 3.8 or higher
- PostgreSQL 12+
- Node.js 14+ (for frontend development)

### Setup Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/your-org/datacrafters-dashboard.git
   cd datacrafters-dashboard
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure the database:
   ```bash
   python database/db_setup.py
   ```

5. Start the application:
   ```bash
   python app/app.py
   ```

## Configuration

Create a `.env` file in the project root with the following variables:
```
DB_HOST=localhost
DB_PORT=5432
DB_NAME=datacrafters
DB_USER=your_username
DB_PASSWORD=your_password
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your_email@gmail.com
SMTP_PASSWORD=your_app_password
```

## Usage

1. Access the dashboard at `http://localhost:5000`
2. Upload your dataset through the data import interface
3. Configure visualization parameters in the settings panel
4. Set up email alerts for anomaly detection

## Development

### Running Tests
```bash
pytest tests/
```

### Code Style
We follow PEP 8 guidelines. Run the linter:
```bash
flake8 .
```

## Contributing
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License
Distributed under the MIT License. See `LICENSE` file for more information.

## Contact
Project Maintainer - [@maintainer](https://github.com/maintainer)

Project Link: [https://github.com/your-org/datacrafters-dashboard](https://github.com/your-org/datacrafters-dashboard)
