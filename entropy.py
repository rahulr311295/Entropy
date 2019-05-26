import jsbeautifier
import requests
opts = jsbeautifier.default_options()
opts.indent_size = 2
opts.space_in_empty_paren = True
res = jsbeautifier.beautify_file('some_file.js',opts)
print(res)