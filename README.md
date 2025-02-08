# BigBasket Grocery Price Comparison
Web scraping BigBasket products, cleaning and storing data in MySQL, and visualizing insights with a Power BI dashboard.

# Project Stages
  **Stage 1:** Scraping and Storing Raw Data
    * Scraped grocery product details (Product Name, Price, Discount, and Category) from BigBasket.
    * Stored the raw data in bigbasket.csv for further processing.  
  
  **Stage 2:** Data Preprocessing and Storing in MySQL
    * Cleaned and preprocessed the raw data (handling duplicates, missing values, and formatting).
    * Stored the cleaned data in bigbasket_cln.csv and directly inserted it into the MySQL database using Python and pymysql connector.
  
  **Stage 3:** Running Queries for Data Analysis
    * Executed SQL queries on MySQL to filter and analyze grocery pricing trends.
    * Extracted insights based on price variations, discount patterns, and category-wise comparisons.
  
  **Stage 4:** Data Visualization in Power BI
    * Retrieved processed data from MySQL into Power BI.
    * Built interactive dashboards to compare grocery prices, analyze affordability, and visualize trends effectively.

# Technologies Used
 * Python (for Web Scraping & Data Cleaning)
 * MySQL (for Data Storage & Querying)
 * Power BI (for Data Visualization)
 * Pandas, BeautifulSoup, pymysql (for data handling and database connection)

# Project Outcome
 * Successfully extracted grocery product data.
 * Stored and managed data efficiently in MySQL.
 * Built an insightful Power BI dashboard for comparative analysis.
