class Name:
    def make_name(self, string):
        return string


class SnakeCaseName(Name):
    def make_name(self, string):
        return "_".join(string.lower().split())


class CapWordsName(Name):
    def make_name(self, string):
        return "".join(string.title().split())


class ModuleName(SnakeCaseName):
    def make_name(self, string):
        return super().make_name(string).replace("_", "") + '.py'


class FunctionName(SnakeCaseName):
    def make_name(self, string):
        return super().make_name(string) + '()'


class VariableName(SnakeCaseName):
    def make_name(self, string):
        return super().make_name(string)


class ConstantName(VariableName):
    def make_name(self, string):
        return super().make_name(string).upper()


class ListName(VariableName):
    def make_name(self, string):
        return super().make_name(string) + "[]"


class ClassName(CapWordsName):
    def make_name(self, string):
        return super().make_name(string)


def main():
    """
    >>> name = Name()
    >>> name.make_name('hello there')
    'hello there'
    >>> snake_case_name = SnakeCaseName()
    >>> snake_case_name.make_name('Hello there my friend')
    'hello_there_my_friend'
    >>> cap_words_name = CapWordsName()
    >>> cap_words_name.make_name('This is cap words')
    'ThisIsCapWords'
    >>> module_name = ModuleName()
    >>> module_name.make_name('Welcome module')
    'welcomemodule.py'
    >>> function_name = FunctionName()
    >>> function_name.make_name('Do this now')
    'do_this_now()'
    >>> constant_name = ConstantName()
    >>> constant_name.make_name('Change is the only constant')
    'CHANGE_IS_THE_ONLY_CONSTANT'
    >>> list_name = ListName()
    >>> list_name.make_name('Collection of movies')
    'collection_of_movies[]'
    >>> class_name = ClassName()
    >>> class_name.make_name('My class')
    'MyClass'
    """
    pass


if __name__ == '__main__':
    main()
