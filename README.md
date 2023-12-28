# plagarismChecker
Overview
The Plagiarism Checker is a Python-based web application built with Flask that offers functionalities to detect plagiarism between text documents. This tool allows users to compare text files, folders containing multiple files, or individual files against a master file, presenting similarity percentages based on the Levenshtein distance algorithm.

Features
Folder Comparison: Compare all files within a folder against a specified master file.
Pairwise Comparison: Check for plagiarism between two individual files.
Plagiarism Detection: Utilizes the Levenshtein distance algorithm to calculate similarity percentages.
User-friendly Interface: Web-based interface for easy interaction.
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/your_username/plagiarism-checker.git
cd plagiarism-checker
Install dependencies:

Copy code
pip install -r requirements.txt
Usage
Run the Flask app:

Copy code
python app.py
Access the app:
Open a web browser and go to http://localhost:5000.

Technologies Used
Python
Flask
HTML/CSS
JavaScript
Levenshtein distance algorithm (for plagiarism detection)
Contributing
Contributions are welcome! If you have any ideas, enhancements, or bug fixes, please submit a pull request or open an issue.

License
This project is licensed under the MIT License.
