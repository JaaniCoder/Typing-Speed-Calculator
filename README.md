## Typing Speed Calculator

### Overview

The **Typing Speed Calculator** is a desktop application built using Python and Flet that measures the user's typing speed in WPM (Words Per Minute) and provides feedback on their typing accuracy. It includes an authentication system with sign-up and login functionality, allowing users to track their progress over time. The application is designed to help users improve their typing skills with real-time feedback.

### Features

- **Sign Up and Login:** Secure authentication system with sign-up and login functionality.
- **Typing Test:** A test that challenges users to type a given set of words or sentences.
- **Typing Speed Calculation:** Measures the typing speed in WPM (Words Per Minute).
- **Accuracy Feedback:** Provides feedback on the accuracy of the typed content.
- **User-Friendly Interface:** Easy-to-navigate interface built with Flet, designed for a smooth user experience.
- **JSON-Based Storage:** User data and typing results are stored in a JSON file for easy access and management.

### Tech Stack

- **Python:** Core programming language used for the application.
- **Flet:** Python framework used for creating the user interface.
- **JSON:** Used for storing user credentials and tracking typing results.

### Installation

Follow these steps to set up the Typing Speed Calculator on your local machine:

1. **Clone the repository:**

   ```
   git clone https://github.com/JaaniCoder/Typing-Speed-Calculator.git
   cd Typing-Speed-Calculator
   ```

2. **Install the required dependencies:**

   Ensure you have Python installed, then run:

   ```
   pip install flet
   ```

3. **Run the application:**

   Start the application with:

   ```
   python main.py
   ```

### Project Structure

- `main.py` - Main entry point of the application.
- `auth.py` - Handles user authentication (sign up and login).
- `typing_test.py` - Contains functions for calculating typing speed and accuracy.
- `users.json` - Stores user data and typing results in JSON format.

### Usage

1. **Sign Up / Login:** 
   - Upon launching the application, you'll be prompted to log in or sign up.
   
2. **Typing Test:**
   - After successful login, the main screen will display the typing test with a given text. 
   - Start typing the displayed text in the provided text box.

3. **Submit Your Test:**
   - Click the **Submit** button after completing the typing test to see your typing speed and accuracy.

### Screenshots
![image](https://github.com/user-attachments/assets/990baab7-bed4-47ca-9325-99a22f77dbad)
![image](https://github.com/user-attachments/assets/1e07d213-9d32-45bc-a813-6a0e32adc7b2)
![image](https://github.com/user-attachments/assets/828a80db-e0e5-43e2-80cc-5ea297bb972b)
![image](https://github.com/user-attachments/assets/7faed11a-6f7b-4c38-812b-a1494f3b8bc8)


### Contributing

Contributions are welcome! If you would like to improve the app or fix any issues, please feel free to fork the repository and submit a pull request.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/YourFeature`)
3. Commit your Changes (`git commit -m 'Add YourFeature'`)
4. Push to the Branch (`git push origin feature/YourFeature`)
5. Open a Pull Request

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Contact

If you have any questions or suggestions, please reach out at:

- **GitHub:** [JaaniCoder](https://github.com/JaaniCoder)
- **Email:** theshayarguyjaani@gmail.com
