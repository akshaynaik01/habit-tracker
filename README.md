# Habit Tracker

A comprehensive habit tracking application to help build and maintain daily habits. Track your progress, monitor streaks, and break bad habits effectively.

## Features

- **Add Habits**: Easily create new habits to track
- **Daily Logging**: Log habit completion for each day
- **Streak Tracking**: Monitor your current streak for each habit
- **Progress Tracking**: View total completion count
- **Data Persistence**: Store habits in JSON format
- **Web API**: RESTful API for integration with other applications
- **Command-line Interface**: CLI for quick habit management

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/akshaynaik01/habit-tracker.git
cd habit-tracker
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Create environment file:
```bash
cp .env.example .env
```

## Usage

### Command-Line Interface

Run the interactive CLI version:
```bash
python main.py
```

Options:
- Add a new habit
- Log a habit completion
- View all habits and statistics
- Delete a habit

### Web API

Start the Flask server:
```bash
python app.py
```

The API will be available at `http://localhost:5000`

#### API Endpoints

- `GET /api/habits` - Get all habits
- `POST /api/habits` - Add a new habit
  - Body: `{"name": "habit_name"}`
- `POST /api/habits/<habit_name>/log` - Log a habit completion
- `DELETE /api/habits/<habit_name>` - Delete a habit

## Project Structure

```
habit-tracker/
├── main.py              # CLI application
├── app.py               # Flask web API
├── requirements.txt     # Project dependencies
├── .env.example         # Environment configuration template
├── .gitignore           # Git ignore rules
└── README.md            # This file
```

## Technologies Used

- **Python 3**: Core language
- **Flask**: Web framework for API
- **JSON**: Data storage format

## File Structure

Habits are stored in `habits.json` with the following structure:
```json
{
  "habit_name": {
    "created_date": "2024-01-30",
    "completed_dates": ["2024-01-30", "2024-01-29", ...]
  }
}
```

## Contributing

Contributions are welcome! Feel free to:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a pull request

## License

This project is open source and available under the MIT License.

## Author

**Akshay Naik**
- GitHub: [@akshaynaik01](https://github.com/akshaynaik01)

## Support

For support, please open an issue on GitHub.

## Roadmap

- [ ] Web frontend (HTML/CSS/JavaScript)
- [ ] Database integration (SQLite/PostgreSQL)
- [ ] User authentication
- [ ] Habit categories
- [ ] Analytics and charts
- [ ] Mobile app
- [ ] Notifications and reminders
