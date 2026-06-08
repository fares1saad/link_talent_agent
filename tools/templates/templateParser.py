# import os
# import importlib


# class TemplateParser:

#     def __init__(self, language: str = "en"):
#         self.language = language
#         self.base_path = "tools.templates.locales"

#         # mapping decision → module + attribute
#         self.template_map = {
#             "reject": ("rejection", "rejection"),
#             "accept": ("acceptance", "acceptance"),
#         }

#     def render(self, decision: str, vars: dict):
#         """
#         decision: 'reject' or 'accept'
#         vars: dict of template variables
#         """

#         if decision not in self.template_map:
#             raise ValueError(f"Unknown decision: {decision}")

#         module_name, template_key = self.template_map[decision]

#         # import module dynamically
#         module_path = f"{self.base_path}.{self.language}.{module_name}"
#         module = importlib.import_module(module_path)

#         # get template object
#         template = getattr(module, template_key, None)

#         if template is None:
#             raise ValueError(
#                 f"Template '{template_key}' not found in {module_path}"
#             )

#         # render template
#         return template.substitute(vars)




import os
import importlib

class TemplateParser:

    def __init__(self, language: str = "en"):
        self.language = language
        self.base_path = "tools.templates.locales"

    def render(self, email_type: str, context: dict):

        module_path = (
            f"{self.base_path}.{self.language}.{email_type}"
        )

        try:
            module = importlib.import_module(module_path)
        except ModuleNotFoundError:
            raise ValueError(
                f"Template file '{email_type}.py' not found"
            )

        template = getattr(module, email_type, None)

        if template is None:
            raise ValueError(
                f"Template variable '{email_type}' not found in {module_path}"
            )

        return template.substitute(context)