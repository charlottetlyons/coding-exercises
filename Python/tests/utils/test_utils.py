#  TEST UTILITY FUNCTIONS
def format_test_result(result):
    return "\033[32mPass\033[0m" if result else "\033[31mFail\033[0m"

def run_all_tests(test_configs):
    for test in test_configs:
        try:
            test_result = (test[1]())
        except:
            test_result = False
        finally:
            print(f"{test[0]}: {format_test_result(test_result)}")
