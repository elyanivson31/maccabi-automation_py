import requests

def call_maccabi_search_api(driver, payload: dict):
    """
    Calls Maccabi's doctor search API using Selenium session cookies.

    :param driver: Selenium WebDriver (must be logged in)
    :param payload: Dict payload for API body
    :return: requests.Response object
    """
    cookies = {cookie['name']: cookie['value'] for cookie in driver.get_cookies()}

    headers = {
        "accept": "application/json, text/plain, */*",
        "content-type": "application/json",
        "origin": "https://online.maccabi4u.co.il",
        "referer": "https://online.maccabi4u.co.il/serguide/heb/doctors/",
        "user-agent": "Mozilla/5.0"
    }

    response = requests.post(
        url="https://online.maccabi4u.co.il/serguide/webapi/api/SearchPage/GetSearchPageSearch/",
        headers=headers,
        cookies=cookies,
        json=payload
    )

    return response
