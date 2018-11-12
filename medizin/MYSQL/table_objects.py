class UserDetails(object):
    def __init__(self, USERID, CONTACT_NAME, ADDRESS, CONTACT_NO, GSTIN, B_ACCOUT_NO, IFSC_CODE, COMPANY_NAME, CITY,
                 ROLE, EMAIL_ID, CONTACT_NO_2=None):
        self.user_id = USERID
        self.contact_name = CONTACT_NAME
        self.address = ADDRESS
        self.contact_no = CONTACT_NO
        self.gstin = GSTIN
        self.bank_account_no = B_ACCOUT_NO
        self.ifsc_code = IFSC_CODE
        self.company_name = COMPANY_NAME
        self.city = CITY
        self.role = ROLE
        self.email_id = EMAIL_ID
        self.contanct_no2 = CONTACT_NO_2


class UserCredentials(object):
    def __init__(self, USERID, USERNAME, E_PASSWORD):
        self.user_id = USERID
        self.username = USERNAME
        self.encrypted_password = E_PASSWORD

    def display_user(self):
        return {
                "user_id": self.user_id,
                "username": self.username,
                "password": self.encrypted_password
            }
