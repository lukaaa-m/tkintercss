from tkintercss import parse_css

def applyStyles(window, stylesheet_path):
    rulesets = []

    rulesets = getRulesets(stylesheet_path)