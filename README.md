# Music Scraping 🎸

Scrape the website [Music3000](https://www.music3000.fr) to extract and organize guitar information into a properly formatted CSV file.

## Overview 📋
This project involves web scraping the Music3000 website to gather detailed information about guitars. The extracted data will be structured and saved into a CSV file for easy analysis and reference.


## Technologies Used 💻
- **Python**: Utilized for web scraping.
- **Beautiful Soup**: A Python library for pulling data out of HTML and XML files.
- **Requests**: A Python library for making HTTP requests.


## How it Works 🚀
1. The Python script sends HTTP requests to the Music3000 website.
2. The HTML content of the pages is parsed using Beautiful Soup.
3. Relevant information about guitars (e.g., model, price, specifications) is extracted.
4. The extracted data is organized and saved into a CSV file.


## Usage 🛠️
1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/Supr3mSushi/music-scrapping.git
    ```

2. Navigate to the project directory:

    ```bash
    cd music-scrapping
    ```

3. Run the Python script:

    ```bash
    python scrapping_music3000.py
    ```

4. Find the generated CSV file with the scraped guitar information.


## Contributing 🤝
Contributions and suggestions are welcome ! Feel free to open an issue or submit a pull request to enhance this project.


## Acknowledgments 🙏
- Special thanks to [Music3000](https://www.music3000.fr) for providing the guitar information.
