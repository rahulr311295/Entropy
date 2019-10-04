import jsbeautifier
import requests
import sys

opts = jsbeautifier.default_options()
opts.indent_size = 2
opts.space_in_empty_paren = True

def beautify(file_to_beautify):
	res = jsbeautifier.beautify_file(file_to_beautify, opts)
	print(res)
	print("\n\nSaving beautified JavaScript code...")
	open('beautified_code.js', 'w+').write(res)
	print("\nFile saved as beautified_code.js")

def main():
	try:
		arg = sys.argv[1]
		if arg == 'help':
			print("\nUsage: python entropy.py javascript_file.js\n")
		else:
			file_to_beautify = str(sys.argv[1])
			beautify(file_to_beautify)
	except:
		print("\nYou can also use: python entropy.py javascript_file.js\n")
		file_to_beautify = raw_input("Enter the name fo the JavaScript file you want to Beautify: ")
		beautify(file_to_beautify)

if __name__ == '__main__':
	main()
