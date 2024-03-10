# Payment Receipt Generator

Welcome to the Payment Receipt Generator, a professional web application built with Flask. This tool empowers users to effortlessly create payment receipts by providing essential details about the transaction. Enhance your record-keeping and streamline your financial processes with this easy-to-use solution.

## Features

- **Intuitive User Input Form:** Fill out a comprehensive form with all the necessary information for generating a payment receipt.

- **Additional Information Fields:** Capture vital details such as invoice date, invoice number, buyer and seller information, and more.

- **Dynamic Receipt Generation:** Instantly generate a polished payment receipt based on the input provided.

- **Downloadable Receipts:** Conveniently download the generated receipt for your records.

## Getting Started

1. **Install Dependencies:**
   Ensure you have Python and Flask installed. If not, install Flask using the following command:

   ```bash
   pip install Flask
   ```

2. **Run the Application:**
   Execute the following command in the project directory to launch the Flask application:

   ```bash
   python app.py
   ```

3. **Access the Application:**
   Open your web browser and navigate to [http://127.0.0.1:5001/](http://127.0.0.1:5001/).

4. **Complete the Form:**
   Input the required information into the user-friendly form and click the "Generate Receipt" button.

5. **Download Your Receipt:**
   Once generated, download the receipt instantly by clicking the "Download Receipt" link.

## Project Structure

- **`app.py`:** Central hub containing the Flask application logic, including the receipt generation functionality.

- **`templates/index.html`:** HTML template defining the user interface's structure.

- **`static/style.css`:** CSS stylesheet for refining the aesthetics of the user interface.

- **`receipts/`:** Dedicated directory for storing all generated receipts.

## Dependencies

- Flask
- Python 3

