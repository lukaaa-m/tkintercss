def getRulesets(stylesheet_path):
    raw_rulesets = []
    rulesets = []

    #'with' is used to ensure that the file instance is closed without having to wait for garbage collector
    with open(stylesheet_path, 'r') as file:
        stylesheet_content = file.read().replace('\n','')
        print(stylesheet_content)

    #stylesheet is split up into whole rulesets
    raw_rulesets = stylesheet_content.split('}')
    print(raw_rulesets)

    for r in raw_rulesets:
        print(r.split('{'))

    #ruleset is formatted: [[selector1,[prop1, prop2, ...]],[selector2,[prop1, prop2, ...]]]
    for i in range(len(raw_rulesets)):
        raw_rulesets[i].split('{')
        rulesets[i][0] = raw_rulesets[i][0]
        rulesets[i][1] = raw_rulesets[i][1].split(';')

    return rulesets

print(getRulesets('test.css'))



