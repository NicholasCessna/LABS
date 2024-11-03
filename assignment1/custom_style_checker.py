# I wrote the project with all project requirements but I also extended the functionality so it Identifies, fixes and rewrites the script with
# correct class and method/function naming (This works well), adds a generic doc string to classes/method/functions if missing (not super useful but handy for debugging the required program), 
# and adds type annotations to functions and methods if missing (Decently accture but again handy for debugging the style report).
# The newly generated .py files naming of incorrect class and method/function names works great. The adding of type annotations also works pretty well but will add 'Any' as the type if it cant Identify particular type (I need better logic here to determine types).
# It outputs the "fixed" generated script in the same folder as fixed_{file_name}.py. 


import ast

class StyleBase:
    """Base class for handling common elements like classes and functions."""

    def __init__(self, name: str, docstring: str) -> None:
        self.name = name
        self.docstring = docstring

    def has_docstring(self) -> bool:
        return bool(self.docstring)

    def get_docstring_status(self) -> str:
        return f'"{self.docstring}"' if self.has_docstring() else "DocString not found"


class ClassInfo(StyleBase):
    """Handles docstrings and naming convention check for classes."""

    def __init__(self, name: str, docstring: str, methods: list["FunctionInfo"]) -> None:
        super().__init__(name, docstring)
        self.methods = methods

    def is_camel_case(self) -> bool:
        return self.name[0].isupper() and "_" not in self.name


class FunctionInfo(StyleBase):
    """Handles docstrings, naming convention checks, type annotation checks for functions and methods."""

    def __init__(self, name: str, docstring: str, annotations: list[ast.expr], return_hint: ast.expr) -> None:
        super().__init__(name, docstring)
        self.annotations = annotations
        self.return_hint = return_hint

    def is_snake_case(self) -> bool:
        return self.name.islower() and "_" in self.name

    def has_annotations(self) -> bool:
        has_param_annotations = all(ann is not None for ann in self.annotations)
        return has_param_annotations and self.return_hint is not None


class CodeAnalyzer:
    """Main class to analyze .py files and generate a style report."""
    
    def __init__(self, file_name: str) -> None:
        self.file_name = file_name
        self.class_list = []
        self.func_list = []
        self.imports = []
        self.line_count = 0
        self.code_tree = None

    def read_file(self) -> None:
        with open(self.file_name, 'r') as file:
            file_content = file.read()
            
        self.code_tree = ast.parse(file_content)
        self.line_count = len(file_content.splitlines())
        
        self.find_imports()
        self.find_classes_and_funcs()

    def find_imports(self) -> None:
        for item in ast.walk(self.code_tree):
            if isinstance(item, (ast.Import, ast.ImportFrom)):
                for name in item.names:
                    self.imports.append(name.name)

    def find_classes_and_funcs(self) -> None:
        """Find classes and functions in the AST."""
        for item in ast.walk(self.code_tree):
            if isinstance(item, ast.ClassDef):
                methods = [self.get_func_info(method) for method in item.body if isinstance(method, ast.FunctionDef)]
                class_info = ClassInfo(item.name, ast.get_docstring(item), methods)
                self.class_list.append(class_info)
            elif isinstance(item, ast.FunctionDef):
                if not any(isinstance(parent, ast.ClassDef) for parent in ast.walk(self.code_tree) if item in getattr(parent, 'body', [])):
                    func_info = self.get_func_info(item)
                    self.func_list.append(func_info)

    def get_func_info(self, item: ast.FunctionDef) -> FunctionInfo:
        annotations = [arg.annotation for arg in item.args.args if arg.arg != "self"] 
        return_hint = item.returns
        return FunctionInfo(item.name, ast.get_docstring(item), annotations, return_hint)

    def generate_report(self) -> None:
        report_name = f'style_report_{self.file_name.replace(".py", "")}.txt'
        with open(report_name, 'w') as report:
            report.write(f'Total number of lines: "{self.line_count}"\n')
            report.write(f'Imports: "{", ".join(self.imports)}"\n')

            report.write("\nClasses:\n")
            for cls in self.class_list:
                report.write(f'Class: {cls.name}, Class Docstring: {cls.get_docstring_status()}\n')
                report.write("  Methods:\n")
                for method in cls.methods:
                    report.write(f'    - Method: {method.name}, Method Docstring: {method.get_docstring_status()}\n')

            report.write("\nFunctions:\n")
            if self.func_list:
                for func in self.func_list:
                    report.write(f'- Function: {func.name}, Function Docstring: {func.get_docstring_status()}\n')
            else:
                report.write("No top-level functions found.\n")

            self.check_annotations(report)
            self.check_names(report)

    def check_annotations(self, report) -> None:
        report.write("\nType Annotations Check:\n")
        missing_annotations = []
        for cls in self.class_list:
            for method in cls.methods:
                if not method.has_annotations():
                    missing_annotations.append(f'{cls.name}.{method.name}')

        for func in self.func_list:
            if not func.has_annotations():
                missing_annotations.append(func.name)

        if missing_annotations:
            report.write(f'❌ Missing annotations: {", ".join(missing_annotations)}\n')
        else:
            report.write('🗸 All functions and methods have type annotations.\n')

    def check_names(self, report) -> None:
        report.write("\nNaming Convention Check:\n")
        bad_class_names = [cls.name for cls in self.class_list if not cls.is_camel_case()]
        bad_method_names = [
            f'{cls.name}.{method.name}' for cls in self.class_list for method in cls.methods if not method.is_snake_case()
        ]
        bad_func_names = [func.name for func in self.func_list if not func.is_snake_case()]

        if bad_class_names:
            report.write(f'❌ Classes not in CamelCase: {", ".join(bad_class_names)}\n')
        else:
            report.write('🗸 All class names use CamelCase.\n')
            
        if bad_method_names:
            report.write(f'❌ Methods not in snake_case: {", ".join(bad_method_names)}\n')
        else:
            report.write(f'🗸 All methods use snake_case.\n')
        
        if bad_func_names:
            report.write(f'❌ Functions not in snake_case: {", ".join(bad_func_names)}\n')
        else:
            report.write(f'🗸 All functions use snake_case.\n')

    # From here down starts the methods that are used to "fix" and regenerate the .py file. All above are the required assignment.  
        
    def apply_fixes(self) -> None:
        self.code_tree = self.fix_style(self.code_tree)
        fixed_code = ast.unparse(self.code_tree)
        fixed_file_name = f"fixed_{self.file_name}"
        with open(fixed_file_name, 'w') as file:
            file.write(fixed_code)
        print(f"Fixed file saved as {fixed_file_name}")

    def fix_style(self, item) -> ast.AST:
        for child in ast.iter_child_nodes(item):
            if isinstance(child, ast.ClassDef):
                child.name = self.to_camel_case(child.name)
                if not ast.get_docstring(child):
                    child.body.insert(0, ast.Expr(value=ast.Constant(value="Class docstring")))
                for method in child.body:
                    if isinstance(method, ast.FunctionDef):
                        if not method.name.startswith("__") or not method.name.endswith("__"):
                            method.name = self.to_snake_case(method.name)
                        if not ast.get_docstring(method):
                            method.body.insert(0, ast.Expr(value=ast.Constant(value="Method docstring")))
                        self.add_type_hints(method)
            elif isinstance(child, ast.FunctionDef):
                child.name = self.to_snake_case(child.name)
                if not ast.get_docstring(child):
                    child.body.insert(0, ast.Expr(value=ast.Constant(value="Function docstring")))
                self.add_type_hints(child)
            self.fix_style(child)
        return item

    def add_type_hints(self, func_item) -> None:
        for i, arg in enumerate(func_item.args.args):
            if i == 0 and arg.arg == "self":
                continue
            if arg.annotation is None:
                arg.annotation = ast.Name(id='Any', ctx=ast.Load())
        if func_item.returns is None:
            inferred_type = self.get_return_type(func_item)
            func_item.returns = ast.Name(id=inferred_type, ctx=ast.Load())

    def get_return_type(self, func_item) -> str:
        """Determine the return type based on return statements in the function."""
        return_type = None
        for stmt in ast.walk(func_item): 
            if isinstance(stmt, ast.Return) and stmt.value is not None:
                return_type = self.infer_type(stmt.value)
                if return_type:
                    break
        return return_type if return_type else 'None'

    def infer_type(self, value_item) -> str:
        """Use the Ast type of an instance to detrmine type."""
        if isinstance(value_item, ast.Constant):
            if isinstance(value_item.value, int):
                return 'int'
            elif isinstance(value_item.value, float):
                return 'float'
            elif isinstance(value_item.value, str):
                return 'str'
            elif isinstance(value_item.value, bool):
                return 'bool'
            elif value_item.value is None:
                return 'None'

        elif isinstance(value_item, ast.List):
            element_types = {self.infer_type(el) for el in value_item.elts}
            if len(element_types) == 1:
                return f'list[{element_types.pop()}]'
            return 'list'
        elif isinstance(value_item, ast.Dict):
            return 'dict'
        elif isinstance(value_item, ast.Set):
            return 'set'
        elif isinstance(value_item, ast.Tuple):
            element_types = {self.infer_type(el) for el in value_item.elts}
            if len(element_types) == 1:
                return f'tuple[{element_types.pop()}]'
            return 'tuple'
        elif isinstance(value_item, ast.Call):
            return 'Any'
        return 'Any'

    @staticmethod
    def to_camel_case(name) -> str:
        if "_" in name:
            return ''.join(word.capitalize() for word in name.split('_'))
        return name

    @staticmethod
    def to_snake_case(name) -> str:
        if name.startswith("__") and name.endswith("__"):
            return name
        return ''.join(['_' + c.lower() if c.isupper() else c for c in name]).lstrip('_')

if __name__ == "__main__":
    file_name = input("Enter the .py file name to analyze: ")
    analyzer = CodeAnalyzer(file_name)
    analyzer.read_file()
    analyzer.generate_report()
    analyzer.apply_fixes()
    print(f"Style report for {file_name} generated.")
    print(f"Fixed file saved as fixed_{file_name}")