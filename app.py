from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
import json
import os
from datetime import datetime

app = Flask(__name__)
CORS(app)

DATA_FILE = 'habits.json'

def load_habits():
    """Load habits from JSON file."""
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            return {}
    return {}

def save_habits(habits):
    """Save habits to JSON file."""
    with open(DATA_FILE, 'w') as f:
        json.dump(habits, f, indent=2)

@app.route('/')
def index():
    """Serve the main HTML page."""
    return render_template('index.html')

@app.route('/api/habits', methods=['GET'])
def get_habits():
    """Get all habits."""
    habits = load_habits()
    return jsonify(habits)

@app.route('/api/habits', methods=['POST'])
def add_habit():
    """Add a new habit."""
    data = request.get_json()
    habit_name = data.get('name')
    
    habits = load_habits()
    if habit_name in habits:
        return jsonify({'error': 'Habit already exists'}), 400
    
    habits[habit_name] = {
        'created_date': datetime.now().strftime('%Y-%m-%d'),
        'completed_dates': []
    }
    save_habits(habits)
    return jsonify({'success': True, 'habit': habits[habit_name]}), 201

@app.route('/api/habits/<habit_name>/log', methods=['POST'])
def log_habit(habit_name):
    """Log completion of a habit."""
    habits = load_habits()
    
    if habit_name not in habits:
        return jsonify({'error': 'Habit not found'}), 404
    
    date = datetime.now().strftime('%Y-%m-%d')
    if date in habits[habit_name]['completed_dates']:
        return jsonify({'error': 'Already logged for today'}), 400
    
    habits[habit_name]['completed_dates'].append(date)
    save_habits(habits)
    return jsonify({'success': True, 'habit': habits[habit_name]})

@app.route('/api/habits/<habit_name>', methods=['DELETE'])
def delete_habit(habit_name):
    """Delete a habit."""
    habits = load_habits()
    
    if habit_name not in habits:
        return jsonify({'error': 'Habit not found'}), 404
    
    del habits[habit_name]
    save_habits(habits)
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
