import ast

# All functions are purely functional using immutable variables with no global or internal side effects. 
# The main() handles taking the input and the output. 
# My relection is in a reflection.txt file in the same directory


def parse_file_content(file_content):
    code_tree = ast.parse(file_content)
    line_count = len(file_content.splitlines())
    return code_tree, line_count


def find_imports(code_tree):
    return tuple(
        name.name
        for item in ast.walk(code_tree)
        if isinstance(item, (ast.Import, ast.ImportFrom))
        for name in item.names
    )


def find_classes_and_functions(code_tree):
    def get_function_info(func_node):
        annotations = tuple(arg.annotation for arg in func_node.args.args if arg.arg != "self")
        return_hint = func_node.returns
        return {
            "name": func_node.name,
            "docstring": ast.get_docstring(func_node),
            "annotations": annotations,
            "return_hint": return_hint
        }
    
    def is_top_level_function(func_node):
        return not any(isinstance(parent, ast.ClassDef) for parent in ast.walk(code_tree) if func_node in getattr(parent, 'body', []))
    
    classes = [
        {
            "name": item.name,
            "docstring": ast.get_docstring(item),
            "methods": [
                get_function_info(method) for method in item.body if isinstance(method, ast.FunctionDef)
            ]
        }
        for item in ast.walk(code_tree) if isinstance(item, ast.ClassDef)
    ]
    
    functions = [
        get_function_info(item) for item in ast.walk(code_tree) if isinstance(item, ast.FunctionDef) and is_top_level_function(item)
    ]
    
    return tuple(classes), tuple(functions)


def check_annotations(classes, functions):
    def has_annotations(func):
        return all(annote is not None for annote in func["annotations"]) and func["return_hint"] is not None

    return tuple(
        f'{cls["name"]}.{method["name"]}' 
        for cls in classes 
        for method in cls["methods"] 
        if not has_annotations(method)) + tuple(func["name"] for func in functions if not has_annotations(func))


def check_naming_conventions(classes, functions):
    def is_camel_case(name):
        return name[0].isupper() and "_" not in name

    def is_snake_case(name):
        return name.islower() and "_" in name

    bad_class_names = tuple(cls["name"] for cls in classes if not is_camel_case(cls["name"]))
    bad_method_names = tuple(
        f'{cls["name"]}.{method["name"]}' 
        for cls in classes 
        for method in cls["methods"] 
        if not is_snake_case(method["name"])
    )
    bad_func_names = tuple(func["name"] for func in functions if not is_snake_case(func["name"]))
    return bad_class_names, bad_method_names, bad_func_names


def generate_report(data):
    line_count, imports, classes, functions, missing_annotations, naming_issues = data
    report_lines = []
    report_lines.append(f'Total number of lines: {line_count}')
    report_lines.append(f'Imports: {", ".join(imports)}\n')

    report_lines.append("Classes:")
    for cls in classes:
        report_lines.append(f'Class: {cls["name"]}, Docstring: {cls["docstring"] or "DocString not found"}')
        report_lines.append("  Methods:")
        for method in cls["methods"]:
            report_lines.append(f'    - Method: {method["name"]}, Docstring: {method["docstring"] or "DocString not found"}')

    report_lines.append("\nFunctions:")
    
    if functions:
        for func in functions:
            report_lines.append(f'- Function: {func["name"]}, Docstring: {func["docstring"] or "DocString not found"}')
    else:
        report_lines.append("No top-level functions found.")

    report_lines.append("\nType Annotations Check:")
    if missing_annotations:
        report_lines.append(f'❌ Missing annotations: {", ".join(missing_annotations)}')
    else:
        report_lines.append('🗸 All functions and methods have type annotations.')

    report_lines.append("\nNaming Convention Check:")
    bad_class_names, bad_method_names, bad_func_names = naming_issues
    if bad_class_names:
        report_lines.append(f'❌ Classes not in CamelCase: {", ".join(bad_class_names)}')
    else:
        report_lines.append('🗸 All class names use CamelCase.')

    if bad_method_names:
        report_lines.append(f'❌ Methods not in snake_case: {", ".join(bad_method_names)}')
    else:
        report_lines.append('🗸 All methods use snake_case.')

    if bad_func_names:
        report_lines.append(f'❌ Functions not in snake_case: {", ".join(bad_func_names)}')
    else:
        report_lines.append('🗸 All functions use snake_case.')

    return "\n".join(report_lines)


def main():
    file_name = input("Enter the .py file name to analyze: ")
    with open(file_name, "r") as file:
        file_content = file.read()

    code_tree, line_count = parse_file_content(file_content)
    imports = find_imports(code_tree)
    classes, functions = find_classes_and_functions(code_tree)
    missing_annotations = check_annotations(classes, functions)
    naming_issues = check_naming_conventions(classes, functions)

    report = generate_report((line_count, imports, classes, functions, missing_annotations, naming_issues))

    output_file = f"styl_report_{file_name.replace('.py', '')}.txt"
    with open(output_file, "w") as file:
        file.write(report)

    print(f"Style report for {file_name} generated as {output_file}.")


if __name__ == "__main__":
    main()
