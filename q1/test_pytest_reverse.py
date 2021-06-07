import reverse
    
class TestClass:
    def test_one(self):
        str = ['have','a','good','summer']
        assert reverse.str_reverse(str) == "summer good a have "
