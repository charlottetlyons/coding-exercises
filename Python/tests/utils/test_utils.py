#  TEST UTILITY FUNCTIONS
def format_test_result(result):
    return "\033[32mPass\033[0m" if result else "\033[31mFail\033[0m"

# TODO: output number of failed tests
def run_all_tests(test_configs):
    for test in test_configs:
        try:
            test_result = (test[1]())
        except Exception as e:
            test_result = False
            print("Test run into an error: ", e)
        finally:
            print(f"{test[0]}: {format_test_result(test_result)}")

def test_sort(initializer, sort_name):
    results = []
    cases = {
        "empty": {
            "input": [], 
            "expected": [],
        },
        "one_element": {
            "input": [1],
            "expected": [1],
        },
        "two_elements": {
            "input": [2, 1],
            "expected": [1, 2],
        },
        "already_sorted": {
            "input": [1, 2, 3, 4, 5],
            "expected": [1, 2, 3, 4, 5],
        },
        "reverse_sorted": {
            "input": [5, 4, 3, 2, 1],
            "expected": [1, 2, 3, 4, 5],
        },
        "duplicates": {
            "input": [3, 2, 1, 2, 3],
            "expected": [1, 2, 2, 3, 3],
        },
        "all_equal": {
            "input": [2, 2, 2, 2, 2],
            "expected": [2, 2, 2, 2, 2],
        },
        "negatives_or_zero": {
            "input": [-1, 0, 1, -2],
            "expected": [-2, -1, 0, 1],
        },
    }
    for case in cases:
        input = cases[case]["input"]
        expected = cases[case]["expected"]
        result = []        
        list = initializer(custom_list=input)
        getattr(list, sort_name)()
        current = list.head        
        
        for _ in range(list.length):
            result.append(current.value)
            current = current.next
        results.append(result == expected)
    for result in results:
        if result is False:
            return False
    return True