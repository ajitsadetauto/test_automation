import time
from playwright.sync_api import Playwright



def test_create_single_type_event(playwright:Playwright):
    bro=playwright.chromium.launch(headless=False)
    context=bro.new_context()
    page=context.new_page()
    page.goto("https://automationtesting.co.uk/fileupload.html", wait_until="domcontentloaded", timeout=60000)
    # Correct file path creation 
    page.screenshot(path="tests/screenshot/files.png")
    file_path = f"tests/test_data/celebration.jpg"
    #Selecting event image. 
    page.locator("#fileToUpload").set_input_files(file_path)
    
    page.screenshot(path="tests/screenshot/fullpage.jpg", full_page=True)
    print('File upload success')
    time.sleep(3)
    page.locator('//input[@name="submit"]').click()
    print('Submit button clicked successfully')
    time.sleep(3)

   