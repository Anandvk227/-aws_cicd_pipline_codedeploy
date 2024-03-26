import time
import unittest
# from testCases.test_companySignUp import TestSignUp
from testCases.test_login import TestLogin
# from testCases.test_configuration import TestConfiguration
# from testCases.test_AddEmployees import addEmployees
# from testCases.test_EmployeeSignUp import TestEmployeeSignUp
# from testCases.test_networks import TestNetworks
# from SunithaTestCase.test_profilePage import TestMyProfile
# from SunithaTestCase.test_CompanyProfile import TestCompanyProfile
# from krishnatestCases.test_newsfeed import TestNewsFeed
# from krishnatestCases.test_resources import Test_Resources
# from krishnatestCases.test_certification import Test_Certification
# from Anand_TestCases.test_DealRegistrations import Test_Create_DealwithNetworkCompany
# from Anand_TestCases.test_Recognitions import Test_Create_Recognition
# from SunithaTestCase.test_Webinar import Test_Webinar
# from testCases.test_MediaDrive import TestMediaDrive


# get all tests from SearchText and HomePageTest class
# companySignUp_test = unittest.TestLoader().loadTestsFromTestCase(TestSignUp)
Test_Login = unittest.TestLoader().loadTestsFromTestCase(TestLogin)
# Test_Conf = unittest.TestLoader().loadTestsFromTestCase(TestConfiguration)
# Test_addEmp = unittest.TestLoader().loadTestsFromTestCase(addEmployees)
# Test_EmpSignUp = unittest.TestLoader().loadTestsFromTestCase(TestEmployeeSignUp)
# Test_Networks = unittest.TestLoader().loadTestsFromTestCase(TestNetworks)
# Test_MyProfile = unittest.TestLoader().loadTestsFromTestCase(TestMyProfile)
# Test_CompanyProfile = unittest.TestLoader().loadTestsFromTestCase(TestCompanyProfile)
# Test_NewsFeed = unittest.TestLoader().loadTestsFromTestCase(TestNewsFeed)
# Test_Resource = unittest.TestLoader().loadTestsFromTestCase(Test_Resources)
# Test_Certifications = unittest.TestLoader().loadTestsFromTestCase(Test_Certification)
# Test_DealRegistration = unittest.TestLoader().loadTestsFromTestCase(Test_Create_DealwithNetworkCompany)
# Test_Recognition = unittest.TestLoader().loadTestsFromTestCase(Test_Create_Recognition)
# Test_Training_Webinar = unittest.TestLoader().loadTestsFromTestCase(Test_Webinar)
# Test_MediaDrive = unittest.TestLoader().loadTestsFromTestCase(TestMediaDrive)


# create a test suite combining search_text and home_page_test

# test_suite = unittest.TestSuite([companySignUp_test, Test_Login,Test_Conf, Test_addEmp, Test_EmpSignUp, Test_Networks, Test_MyProfile, Test_CompanyProfile,Test_NewsFeed,Test_Resource,Test_Certifications,Test_DealRegistration,Test_Recognition,Test_Training_Webinar,Test_MediaDrive])

test_suite = unittest.TestSuite([Test_Login])

# test_suite = unittest.TestSuite([companySignUp_test, Test_Login,Test_Conf, Test_addEmp, Test_EmpSignUp, Test_Networks, Test_NewsFeed])
# test_suite = unittest.TestSuite([companySignUp_test, Test_Login])


# test_suite = unittest.TestSuite([companySignUp_test, Test_Login,Test_Conf, Test_addEmp, Test_EmpSignUp, Test_Networks, Test_MyProfile, Test_CompanyProfile,Test_NewsFeed,Test_Resource,Test_Certifications,Test_DealRegistration,Test_Recognition,Test_Training_Webinar,Test_MediaDrive])
# test_suite = unittest.TestSuite([Test_Certifications,Test_Training_Webinar])





# Run the suite
if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(test_suite)
