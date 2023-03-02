# github-trending---web-scraping

### Description

This project was created with the aim to extract information about [trending pages](https://github.com/trending) on GitHub.

### The process

---

- Import the necessary libraries: such as requests, BeautifulSoup, and pandas to perform web scraping and data manipulation.
- Send a request to the GitHub trending page: used the requests library to send a GET request to the URL of the GitHub trending page.
- Parse the HTML content: used the BeautifulSoup library to parse the HTML content of the response. You can use the .prettify() method to view the structure of the HTML and identify the relevant tags and attributes.
- Extract the data: used the BeautifulSoup methods and attributes to extract the relevant data from the HTML. This includes the name, description, and number of stars for each repository.
