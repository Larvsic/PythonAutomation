from selenium.webdriver.common.by import By


class obj():

    # ======================Executable path ===================================================
    chromePath = "chromeDriver/chromedriver.exe"
    disable_notification = "--disable-notifications"

    # Elements by ID
    appleSimbol = "ac-gn-firstfocus"

    # Elements by name

    # Xpaths
    ipadButton = "/html/body/nav/div/ul[2]/li[3]/a"
    footer = "/html/body/footer/div/section[2]/div[3]/div[1]"
    airpodsMax = "/html/body/main/section[3]/div[6]/div/div/a"

# ======================Log in ===================================================
    loginButton = "/html/body/div[2]/div[2]/div/div/p[3]/button"
    userName = "testuser@example.com"
    password = "test123"

    txtbox_userName = "/html/body/div[2]/div[2]/div/div/p[1]/input"
    txtbox_password = "/html/body/div[2]/div[2]/div/div/p[2]/input"

    loginButton2 = "/html/body/div[2]/div[2]/div/div/p[3]/button[1]"

    myNotes = "/html/body/div[2]/div[1]/div/ul/li[2]/a"
