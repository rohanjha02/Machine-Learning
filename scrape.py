from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import openpyxl

def scrape_imdb_top_movies():
    driver_path = r'C:\Users\asus\Downloads\edgedriver_win32\msedgedriver.exe'
    driver = webdriver.Edge(executable_path=driver_path)
    url = 'https://www.imdb.com/chart/top/?ref_=nv_mv_250'
    driver.get(url)
    time.sleep(3)

    # Set up Excel workbook and sheet
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    headers = ["Title", "Year", "Duration", "Rated As", "Genre", "Director", "Rating", "Stars", "Streaming On"]
    sheet.append(headers)

    try:
        buttons = WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, "button.ipc-icon-button.cli-info-icon.ipc-icon-button--base.ipc-icon-button--onAccent2"))
        )
        
        for index, button in enumerate(buttons):
            driver.execute_script("arguments[0].click();", button)
            time.sleep(2)

            modal = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.CLASS_NAME, "ipc-promptable-base__focus-lock"))
            )

            # Extract information with fallbacks for missing data
            title = modal.find_element(By.CSS_SELECTOR, "h3.ipc-title__text").text if modal.find_element(By.CSS_SELECTOR, "h3.ipc-title__text") else "N/A"
            details = modal.find_elements(By.CSS_SELECTOR, "li.ipc-inline-list__item")
            year = details[0].text if len(details) > 0 else "N/A"
            duration = details[1].text if len(details) > 1 else "N/A"
            rated_as = details[2].text if len(details) > 2 else "N/A"
            genre = details[3].text if len(details) > 3 else "N/A"
            rating = modal.find_element(By.CSS_SELECTOR, "span.ipc-rating-star--imdb").text if modal.find_element(By.CSS_SELECTOR, "span.ipc-rating-star--imdb") else "N/A"

            director_name = "N/A"
            try:
                director_container = modal.find_element(By.CSS_SELECTOR, "div[data-testid='p_ct_dr']")
                if director_container:
                    director_name = director_container.find_element(By.TAG_NAME, "a").text
            except:
                director_name = "N/A"

            stars = "N/A"
            try:
                stars_container = modal.find_element(By.CSS_SELECTOR, "div[data-testid='p_ct_cst']")
                if stars_container:
                    star_links = stars_container.find_elements(By.TAG_NAME, "a")
                    stars = ", ".join([star.text for star in star_links if star.text])
            except:
                stars = "N/A"

            streaming_services = "N/A"
            try:
                streaming_elements = modal.find_elements(By.CSS_SELECTOR, "div.sc-b2d8b824-6.hSxKeA")
                if streaming_elements:
                    streaming_services = ", ".join([element.text for element in streaming_elements if element.text])
            except:
                streaming_services = "N/A"

            # Append row to Excel sheet
            row = [title, year, duration, rated_as, genre, director_name, rating, stars, streaming_services]
            sheet.append(row)

            # Close the modal
            close_button = modal.find_element(By.CSS_SELECTOR, "button.ipc-icon-button.ipc-icon-button--baseAlt.ipc-icon-button--onBase")
            driver.execute_script("arguments[0].click();", close_button)
            WebDriverWait(driver, 10).until(EC.invisibility_of_element(modal))

    finally:
        driver.quit()
        # Save the Excel workbook
        workbook.save("IMDb_Top_250_Movies.xlsx")
        print("Data extraction and Excel file creation completed successfully.")

scrape_imdb_top_movies()
