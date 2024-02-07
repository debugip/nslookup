# NSLookup Script

This Python script takes a text file with one IP address per line as input, performs an nslookup for each IP address, and writes the results into a CSV file.

## How to Use

1. **Clone the Repository:**

    ```
    git clone https://github.com/your_username/nslookup-script.git
    cd nslookup-script
    ```

2. **Install Requirements:**

    Ensure you have Python installed on your system. No additional libraries are required.

3. **Run the Script:**

    Run the script by executing the following command:

    ```
    python nslookup_script.py
    ```

4. **Input File:**

    When prompted, enter the path to the input text file containing IP addresses. Each IP address should be on a separate line.

5. **Output File:**

    The script will automatically generate an output CSV file in the format "nslookup_<date>_<time>.csv", where `<date>` is the current date and `<time>` is the current time when the script is executed. The CSV file will contain two columns: "IP Address" and "DNS Name".

6. **View Results:**

    Once the script completes, you can find the output CSV file in the same directory as the script. Open the CSV file using a spreadsheet program like Microsoft Excel or Google Sheets to view the results.

## Script Functionality

The script uses the `socket` module in Python to perform DNS lookups for each IP address provided in the input file. It then writes the IP address and its corresponding DNS name into a CSV file.

Feel free to reach out if you have any questions or encounter any issues.
