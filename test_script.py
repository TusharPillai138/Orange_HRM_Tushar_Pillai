from ObjectRepo import Login_PIM_page


def test_run_login_pim():
    test_run = Login_PIM_page.LoginPIM()
    test_run.test_login_negative()
    test_run.test_login_positive()
    test_run.add_employees()
    test_run.verify_added_employees()
    test_run.logout()
    test_run.quit_driver()

test_run_login_pim()